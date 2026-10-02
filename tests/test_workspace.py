import contextlib
import io
import json
import os
import stat
import tempfile
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch

from codexlab.cli import _render_dashboard, doctor, main
from codexlab.workspace import STAGES, WorkspaceError, artifact_path, check_gate, create_workspace, load_workspace, workspace_status


CONTENT = "# Completed research artifact\n\n" + ("The held-out comparison has a fixed budget, recorded provenance, and a testable rejection criterion. " * 3)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = create_workspace(self.base / "lab", "Reliable scientific question answering")
        _, self.manifest = load_workspace(self.root)

    def write(self, relative, content=CONTENT):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_init_is_self_contained_and_substitutes_topic(self):
        self.assertEqual(self.manifest["topic"], "Reliable scientific question answering")
        self.assertIn(self.manifest["topic"], (self.root / "research/brief.md").read_text(encoding="utf-8"))
        self.assertTrue((self.root / "AGENTS.md").is_file())
        self.assertFalse(self.manifest["synthetic_demo"])

    def test_init_never_overwrites_existing_target(self):
        self.write("sentinel.txt", "keep me")
        with self.assertRaisesRegex(WorkspaceError, "already exists"):
            create_workspace(self.root, "new topic")
        self.assertEqual((self.root / "sentinel.txt").read_text(), "keep me")
        empty = self.base / "empty"
        empty.mkdir()
        with self.assertRaises(WorkspaceError):
            create_workspace(empty, "topic")

    def test_init_rejects_parent_traversal_empty_topic_missing_parent(self):
        for target, topic in ((self.base / "child" / ".." / "escape", "topic"), (self.base / "blank", "  "), (self.base / "absent" / "lab", "topic")):
            with self.subTest(target=target), self.assertRaises(WorkspaceError):
                create_workspace(target, topic)

    def test_artifacts_cannot_escape(self):
        for value in ("../secret", "..\\secret", str(self.base / "secret"), "C:\\secret", 12, [], ""):
            with self.subTest(value=value), self.assertRaises(WorkspaceError):
                artifact_path(self.root, value)

    def test_symlink_rejected(self):
        link = self.base / "link"
        try:
            link.symlink_to(self.root, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Creating symlinks is not available for this account")
        with self.assertRaises(WorkspaceError):
            load_workspace(link)
        with self.assertRaises(WorkspaceError):
            create_workspace(link / "nested", "topic")

    def test_windows_junction_reparse_attributes_rejected(self):
        real_lstat = Path.lstat

        def fake_lstat(path):
            result = real_lstat(path)
            if path == self.root:
                class Reparse:
                    st_file_attributes = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
                    st_mode = result.st_mode
                return Reparse()
            return result

        with patch.object(Path, "lstat", fake_lstat), self.assertRaisesRegex(WorkspaceError, "junction"):
            load_workspace(self.root)

    def test_all_initial_gates_block_placeholders_or_empty_ledgers(self):
        for stage in STAGES:
            with self.subTest(stage=stage):
                result = check_gate(self.root, self.manifest, stage)
                self.assertFalse(result["passed"])
                self.assertTrue(result["issues"])

    def test_scope_accepts_completed_body_but_not_headings_empty_or_placeholders(self):
        for text in ("", "# Heading " * 30, CONTENT + "\nTODO resolve", CONTENT + "{{TOPIC}}", "# Body\n\nshort"):
            self.write("research/brief.md", text)
            self.assertFalse(check_gate(self.root, self.manifest, "scope")["passed"])
        self.write("research/brief.md")
        self.assertTrue(check_gate(self.root, self.manifest, "scope")["passed"])

    def test_literature_requires_well_formed_real_source_ledger(self):
        self.write("literature/prior-art.md")
        self.write("evidence/ledger.jsonl", json.dumps({"title": "Primary source", "url": "https://arxiv.org/abs/1706.03762", "checked_at": "2026-10-01", "claim": "The source is linked to a specific comparison claim."}) + "\n")
        self.assertTrue(check_gate(self.root, self.manifest, "literature")["passed"])
        for entry in ("not JSON", "[]", '{"title":"unfinished"}', json.dumps({"title": 1, "url": "https://a.test", "checked_at": "2026-10-01", "claim": "text"}), json.dumps({"title": "title", "url": "file:///secret", "checked_at": "bad", "claim": "text"})):
            self.write("evidence/ledger.jsonl", entry)
            self.assertFalse(check_gate(self.root, self.manifest, "literature")["passed"])

    def run_record(self):
        return {"run_id": "run-001", "command": "python experiments/train.py --seed 7", "seed": 7, "metrics": {"accuracy": 0.8}, "artifact_path": "experiments/output.json"}

    def test_malformed_source_url_is_reported_without_breaking_status(self):
        self.write("literature/prior-art.md")
        record = {"title": "Primary source", "url": "https://[broken", "checked_at": "2026-10-01", "claim": "A source claim."}
        raw = json.dumps(record) + "\n"
        self.write("evidence/ledger.jsonl", raw)
        gate = check_gate(self.root, self.manifest, "literature")
        self.assertFalse(gate["passed"])
        self.assertIn("line 1: source URL", str(gate["issues"]))
        self.assertIn("source URL", _render_dashboard(workspace_status(self.root, self.manifest)))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(["status", str(self.root), "--json"]), 0)
        self.assertIn("source URL", str(json.loads(out.getvalue())["gates"]))
        self.assertEqual((self.root / "evidence/ledger.jsonl").read_text(encoding="utf-8"), raw)

    def test_null_run_artifact_path_is_reported_without_breaking_status(self):
        self.complete_experiment()
        record = self.run_record() | {"artifact_path": "experiments/bad\0.json"}
        raw = json.dumps(record) + "\n"
        self.write("experiments/runs.jsonl", raw)
        with self.assertRaises(WorkspaceError):
            artifact_path(self.root, record["artifact_path"])
        gate = check_gate(self.root, self.manifest, "experiment")
        self.assertFalse(gate["passed"])
        self.assertIn("line 1: unsafe run artifact path", str(gate["issues"]))
        self.assertIn("unsafe run artifact path", _render_dashboard(workspace_status(self.root, self.manifest)))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(main(["gate", str(self.root), "experiment"]), 1)
            self.assertEqual(main(["status", str(self.root), "--json"]), 0)
        self.assertEqual((self.root / "experiments/runs.jsonl").read_text(encoding="utf-8"), raw)

    def complete_experiment(self):
        self.write("experiments/plan.md")
        self.write("experiments/results.md")
        self.write("experiments/output.json", '{"accuracy": 0.8}')
        self.write("experiments/runs.jsonl", json.dumps(self.run_record()) + "\n")

    def test_experiment_requires_real_artifact_and_metrics(self):
        self.complete_experiment()
        self.assertTrue(check_gate(self.root, self.manifest, "experiment")["passed"])
        (self.root / "experiments/output.json").unlink()
        result = check_gate(self.root, self.manifest, "experiment")
        self.assertFalse(result["passed"])
        self.assertIn("run artifact missing", str(result["issues"]))

    def test_experiment_rejects_malformed_paths_nonfinite_and_synthetic(self):
        self.complete_experiment()
        changes = [{"artifact_path": []}, {"artifact_path": 12}, {"artifact_path": "../secret"}, {"artifact_path": str(self.base / "output.json")}, {"metrics": {"x": float("nan")}}, {"metrics": {"x": float("inf")}}, {"metrics": {"x": True}}, {"seed": True}, {"synthetic": True}, {"run_id": " "}, {"command": " "}]
        for change in changes:
            with self.subTest(change=change):
                record = self.run_record() | change
                self.write("experiments/runs.jsonl", json.dumps(record))
                self.assertFalse(check_gate(self.root, self.manifest, "experiment")["passed"])

    def test_run_artifact_placeholders_are_rejected(self):
        self.complete_experiment()
        self.write("experiments/output.json", '{"accuracy": "TODO actual result"}')
        gate = check_gate(self.root, self.manifest, "experiment")
        self.assertFalse(gate["passed"])
        self.assertIn("run artifact contains unresolved placeholders", str(gate["issues"]))

    def test_demo_is_conspicuously_synthetic_and_cannot_pass(self):
        root = create_workspace(self.base / "demo", "synthetic", demo=True)
        root, manifest = load_workspace(root)
        self.assertTrue(manifest["synthetic_demo"])
        self.assertIn("SYNTHETIC DEMO", (root / "experiments/results.md").read_text(encoding="utf-8"))
        for stage in STAGES:
            self.assertFalse(check_gate(root, manifest, stage)["passed"])

    def test_toml_roles_and_configs_are_parseable(self):
        config = tomllib.loads((self.root / ".codex/config.toml").read_text(encoding="utf-8"))
        self.assertIsInstance(config, dict)
        roles = list((self.root / ".codex/agents").glob("*.toml"))
        self.assertEqual({role.stem for role in roles}, {"literature", "method", "experiment", "reviewer"})
        for role in roles:
            data = tomllib.loads(role.read_text(encoding="utf-8"))
            self.assertTrue(data.get("developer_instructions"))

    def test_dashboard_escapes_project_text_and_marks_demo(self):
        status = workspace_status(self.root, self.manifest)
        status["name"] = '<script>alert("x")</script>'
        status["synthetic_demo"] = True
        page = _render_dashboard(status)
        self.assertNotIn('<script>alert', page)
        self.assertIn("&lt;script&gt;", page)
        self.assertIn("SYNTHETIC DEMO", page)

    def test_cli_exit_codes_prompt_default_workspace_and_json(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(["status", str(self.root), "--json"]), 0)
        self.assertEqual(json.loads(out.getvalue())["topic"], self.manifest["topic"])
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(main(["gate", str(self.root), "scope"]), 1)
            self.assertEqual(main(["prompt", str(self.root)]), 0)
        previous = Path.cwd()
        try:
            os.chdir(self.root)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(["gate", "scope"]), 1)
        finally:
            os.chdir(previous)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(["init", str(self.root), "--topic", "other"]), 2)

    def test_doctor_only_checks_executable_no_authentication(self):
        with patch("codexlab.cli.shutil.which", return_value=None), patch("codexlab.cli.subprocess.run") as process:
            result = doctor()
            self.assertFalse(result["ready"])
            process.assert_not_called()
        with patch("codexlab.cli.shutil.which", return_value="codex"), patch("codexlab.cli.subprocess.run") as process:
            process.return_value.returncode = 0
            process.return_value.stdout = "codex 1.0"
            process.return_value.stderr = ""
            self.assertTrue(doctor()["ready"])
            self.assertEqual(process.call_args.args[0], ["codex", "--version"])


if __name__ == "__main__":
    unittest.main()
