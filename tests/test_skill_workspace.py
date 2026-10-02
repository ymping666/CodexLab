"""Behavioral checks for the separately installable Skill's optional helper."""

import importlib.util
import json
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from codexlab.workspace import load_workspace, workspace_status

SKILL = Path(__file__).resolve().parents[1] / "skills" / "codexlab"
spec = importlib.util.spec_from_file_location("skill_initializer", SKILL / "scripts" / "init_workspace.py")
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


class SkillWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def test_utf8_complete_artifacts_and_empty_ledgers_without_project_configuration(self):
        root = helper.initialize(self.base / "我的研究", "  科学问答中的可靠检索  ")
        files = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
        self.assertEqual(files, helper.RESEARCH_FILES | {".codexlab.json"})
        self.assertFalse((root / "AGENTS.md").exists())
        self.assertFalse((root / ".codex").exists())
        brief = (root / "research/brief.md").read_text(encoding="utf-8")
        self.assertIn("科学问答中的可靠检索", brief)
        self.assertIn("我的研究", brief)
        self.assertNotIn("{{TOPIC}}", brief)
        self.assertIn("TODO", brief)
        for relative in ("evidence/ledger.jsonl", "experiments/runs.jsonl"):
            self.assertEqual((root / relative).read_bytes(), b"")

    def test_manifest_is_recognized_by_existing_cli_without_claiming_results(self):
        root = helper.initialize(self.base / "lab", "Reliable retrieval")
        loaded_root, manifest = load_workspace(root)
        self.assertEqual(loaded_root, root)
        self.assertEqual(manifest["entrypoint"], "skill")
        self.assertFalse(manifest["synthetic_demo"])
        self.assertEqual(datetime.fromisoformat(manifest["created_at"]).utcoffset().total_seconds(), 0)
        status = workspace_status(loaded_root, manifest)
        self.assertEqual(status["topic"], "Reliable retrieval")
        self.assertTrue(all(not stage["passed"] for stage in status["gates"]))

    def test_refuses_existing_directory_and_preserves_research_data(self):
        target = self.base / "lab"
        target.mkdir()
        with self.assertRaisesRegex(helper.InitError, "already exists"):
            helper.initialize(target, "topic")
        data = target / "real-results.csv"
        data.write_bytes(b"accuracy,0.81\n")
        with self.assertRaises(helper.InitError):
            helper.initialize(target, "different topic")
        self.assertEqual(data.read_bytes(), b"accuracy,0.81\n")

    def test_rejects_traversal_missing_parent_and_empty_topic(self):
        for target, topic in ((self.base / "child" / ".." / "escape", "topic"), (self.base / "absent" / "lab", "topic"), (self.base / "blank", "   ")):
            with self.subTest(target=target), self.assertRaises(helper.InitError):
                helper.initialize(target, topic)
        self.assertFalse((self.base / "escape").exists())
        self.assertFalse((self.base / "absent").exists())
        self.assertFalse((self.base / "blank").exists())

    def test_actual_symlink_ancestor_is_rejected(self):
        directory = self.base / "directory"
        directory.mkdir()
        link = self.base / "link"
        try:
            link.symlink_to(directory, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("This account cannot create symlinks")
        with self.assertRaises(helper.InitError):
            helper.initialize(link / "lab", "topic")
        self.assertEqual(list(directory.iterdir()), [])

    def test_windows_reparse_ancestor_is_rejected(self):
        actual_lstat = Path.lstat

        def lstat(path):
            result = actual_lstat(path)
            if path == self.base:
                class Reparse:
                    st_file_attributes = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
                    st_mode = result.st_mode
                return Reparse()
            return result

        with patch.object(Path, "lstat", lstat), self.assertRaisesRegex(helper.InitError, "reparse"):
            helper.initialize(self.base / "lab", "topic")

    def test_partial_failure_preserves_other_files_and_reports_incomplete_copy(self):
        original_open = Path.open
        target = self.base / "lab"

        def interrupted_open(path, *args, **kwargs):
            if path == target / "research/brief.md" and args and args[0] == "x":
                with original_open(target / "user-notes.txt", "w", encoding="utf-8") as handle:
                    handle.write("Do not delete these concurrent notes")
                raise OSError("simulated disk write failure")
            return original_open(path, *args, **kwargs)

        with patch.object(Path, "open", interrupted_open), self.assertRaisesRegex(helper.InitError, "Copy incomplete"):
            helper.initialize(target, "topic")
        self.assertEqual((target / "user-notes.txt").read_text(), "Do not delete these concurrent notes")

    def test_installed_skill_runs_in_isolated_python_without_the_repository(self):
        installed = self.base / "installed-skill"
        shutil.copytree(SKILL, installed, ignore=shutil.ignore_patterns("__pycache__"))
        root = self.base / "independent-run"
        process = subprocess.run([sys.executable, "-I", str(installed / "scripts/init_workspace.py"), "init", str(root), "--topic", "独立安装研究"], cwd=self.base, capture_output=True, text=True, encoding="utf-8", timeout=10)
        self.assertEqual(process.returncode, 0, process.stderr)
        manifest = json.loads((root / ".codexlab.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["topic"], "独立安装研究")
        self.assertEqual(manifest["entrypoint"], "skill")
        self.assertEqual(len(list(root.rglob("*.md"))), 7)


if __name__ == "__main__":
    unittest.main()
