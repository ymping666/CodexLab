"""Workspace creation and offline evidence checks. No network or credential access."""

from __future__ import annotations

import json
import math
import re
import stat
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from . import __version__

MANIFEST = ".codexlab.json"
STAGES = {
    "scope": ("research/brief.md",),
    "literature": ("literature/prior-art.md", "evidence/ledger.jsonl"),
    "method": ("method/proposal.md",),
    "experiment": ("experiments/plan.md", "experiments/results.md", "experiments/runs.jsonl"),
    "review": ("review/report.md",),
}
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|REPLACE_ME|PLACEHOLDER)\b|\{\{[^}]*\}\}|<fill[^>]*>", re.I)


class WorkspaceError(ValueError):
    """A safe, user-actionable workspace error."""


def _reject_traversal(value: str) -> None:
    if ".." in value.replace("\\", "/").split("/"):
        raise WorkspaceError("Parent traversal ('..') is not allowed in workspace or artifact paths.")


def _no_symlinks(path: Path) -> None:
    for item in (path, *path.parents):
        try:
            attributes = getattr(item.lstat(), "st_file_attributes", 0)
        except FileNotFoundError:
            attributes = 0
        if item.is_symlink() or attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
            raise WorkspaceError(f"Symlink and junction paths are not supported: {item}")


def artifact_path(root: Path, relative: str) -> Path:
    """Resolve an artifact only inside this workspace, rejecting links and traversal."""
    if not isinstance(relative, str):
        raise WorkspaceError("Artifact path must be a string.")
    _reject_traversal(relative)
    normalized = relative.replace("\\", "/")
    candidate = Path(normalized)
    if candidate.is_absolute() or ":" in normalized or not normalized:
        raise WorkspaceError(f"Artifact path must be relative: {relative}")
    result = root / candidate
    _no_symlinks(result)
    if not result.resolve().is_relative_to(root.resolve()):
        raise WorkspaceError(f"Artifact escapes workspace: {relative}")
    return result


def load_workspace(value: str | Path = ".") -> tuple[Path, dict]:
    _reject_traversal(str(value))
    path = Path(value).absolute()
    _no_symlinks(path)
    root = path.resolve()
    manifest = artifact_path(root, MANIFEST)
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise WorkspaceError(f"No valid CodexLab workspace at {root}. Run 'codexlab init NEW_PATH --topic ...'.") from error
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("topic"), str):
        raise WorkspaceError(f"Unsupported or malformed workspace manifest: {manifest}")
    return root, data


def create_workspace(value: str | Path, topic: str, *, demo: bool = False) -> Path:
    _reject_traversal(str(value))
    if not topic.strip():
        raise WorkspaceError("Research topic must contain text.")
    target = Path(value).absolute()
    _no_symlinks(target)
    if target.exists():
        raise WorkspaceError(f"Target already exists; nothing overwritten: {target}")
    if not target.parent.is_dir():
        raise WorkspaceError(f"Parent directory does not exist: {target.parent}")
    template_root = Path(__file__).parent / "templates" / "research"
    if not template_root.is_dir():
        raise WorkspaceError("Research templates are missing from this installation.")
    files: dict[str, str] = {}
    for source in sorted(template_root.rglob("*")):
        _no_symlinks(source)
        if not source.is_file():
            continue
        relative = source.relative_to(template_root).as_posix()
        content = source.read_text(encoding="utf-8")
        files[relative] = content.replace("{{PROJECT_NAME}}", target.name).replace("{{TOPIC}}", topic.strip())
    if not files:
        raise WorkspaceError("Research templates are empty.")
    manifest = {
        "schema_version": 1,
        "codexlab_version": __version__,
        "name": target.name,
        "topic": topic.strip(),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "synthetic_demo": demo,
    }
    files[MANIFEST] = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    if demo:
        files.update(_demo_files())
    # mkdir is exclusive, including when another process creates the target first.
    try:
        target.mkdir()
    except FileExistsError as error:
        raise WorkspaceError(f"Target already exists; nothing overwritten: {target}") from error
    created: list[Path] = []
    try:
        for relative, content in files.items():
            destination = artifact_path(target, relative)
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
            created.append(destination)
    except Exception:
        # Remove only files created by this call; never recursively delete a target.
        for file in reversed(created):
            if file.is_file() and not file.is_symlink():
                file.unlink()
        for directory in sorted((p for p in target.rglob("*") if p.is_dir() and not p.is_symlink()), key=lambda p: len(p.parts), reverse=True):
            try:
                directory.rmdir()
            except OSError:
                pass
        try:
            target.rmdir()
        except OSError:
            pass
        raise
    return target.resolve()


def _demo_files() -> dict[str, str]:
    """An invented fixture illustrating the workflow, never empirical evidence."""
    banner = "> SYNTHETIC DEMO — invented scenario and numbers; not research evidence.\n\n"
    return {
        "research/brief.md": banner + "# Research brief\n\nStudy whether a retrieval confidence signal helps an agent abstain from unsupported scientific claims. The target is fewer unsupported answers at matched coverage. Success requires a held-out, provenance-tracked evaluation and reproducible paired baselines. No experiment has been executed.\n",
        "literature/prior-art.md": banner + "# Prior-art map\n\nThis fixture compares a direct-answer baseline, a retrieval baseline, and a confidence-guided abstention proposal. Entries are invented labels for showing the lab handoff. A real project must replace them with verified primary sources, explicit collision checks, and a claim-to-source ledger.\n",
        "evidence/ledger.jsonl": json.dumps({"title": "Synthetic retrieval baseline", "url": "https://example.invalid/synthetic-demo", "checked_at": "2026-01-01", "claim": "Invented source for layout demonstration", "synthetic": True}) + "\n",
        "method/proposal.md": banner + "# Method proposal\n\nUse retrieval agreement to decide whether to answer or abstain. Compare at fixed coverage against a threshold-only baseline. Falsification: reject the method if improvements disappear after matching coverage or controlling retrieval quality. This is an illustrative hypothesis, not a novelty claim.\n",
        "experiments/plan.md": banner + "# Experiment plan\n\nUse paired prompts and a held-out test split with three seeds. Report accuracy, unsupported-claim rate, and coverage; include uncertainty estimates and all failed runs. Freeze the dataset and retrieval configuration before evaluation. This synthetic fixture has no real dataset or execution.\n",
        "experiments/results.md": banner + "# Illustrative results\n\n| System | Unsupported claims | Coverage |\n|---|---:|---:|\n| Synthetic baseline | 24% | 80% |\n| Synthetic proposal | 18% | 80% |\n\nAll values are invented to demonstrate artifact flow. No performance conclusion or publication promise follows from this fixture.\n",
        "experiments/runs.jsonl": json.dumps({"run_id": "synthetic-001", "command": "illustration only; not executed", "seed": 0, "metrics": {"unsupported_claim_rate": 0.18, "coverage": 0.8}, "artifact_path": "experiments/synthetic-run.json", "synthetic": True}) + "\n",
        "experiments/synthetic-run.json": json.dumps({"synthetic": True, "executed": False, "note": "Invented fixture, not empirical output"}, indent=2) + "\n",
        "review/report.md": banner + "# Independent review\n\nVerdict: DEMO ONLY. The proposal has a clear comparison and falsification condition, but no verified prior art, real runs, or uncertainty estimates. A reviewer should block any empirical claim until provenance, real artifacts, matched budgets, and evaluation leakage checks are complete.\n",
    }


def _text_issues(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ["missing or unreadable"]
    if not text.strip():
        return ["empty"]
    issues = []
    if PLACEHOLDER.search(text):
        issues.append("contains unresolved template placeholders")
    body = " ".join(line for line in text.splitlines() if line.strip() and not line.lstrip().startswith(("#", "<!--", "|---")))
    if len(body.strip()) < 80:
        issues.append("requires at least 80 characters of substantive content")
    return issues


def _ledger_issues(root: Path, relative: str, *, runs: bool) -> list[str]:
    path = artifact_path(root, relative)
    try:
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, UnicodeError):
        return ["missing or unreadable"]
    if not lines:
        return ["empty; at least one evidence record is required"]
    issues: list[str] = []
    required = ("run_id", "command", "seed", "metrics", "artifact_path") if runs else ("title", "url", "checked_at", "claim")
    for index, line in enumerate(lines, 1):
        try:
            record = json.loads(line)
        except ValueError:
            issues.append(f"line {index}: invalid JSON")
            continue
        if not isinstance(record, dict):
            issues.append(f"line {index}: expected a JSON object")
            continue
        missing = [key for key in required if key not in record or record[key] in (None, "", {}, [])]
        if missing:
            issues.append(f"line {index}: missing fields {', '.join(missing)}")
            continue
        if PLACEHOLDER.search(line):
            issues.append(f"line {index}: unresolved placeholders")
        if record.get("synthetic"):
            issues.append(f"line {index}: synthetic evidence cannot pass a research gate")
        if runs:
            if any(not isinstance(record[key], str) or not record[key].strip() for key in ("run_id", "command")):
                issues.append(f"line {index}: run_id and command must be nonempty strings")
            if not isinstance(record["seed"], int) or isinstance(record["seed"], bool):
                issues.append(f"line {index}: seed must be an integer")
            metrics = record["metrics"]
            if not isinstance(metrics, dict) or not metrics or any(not isinstance(v, (int, float)) or isinstance(v, bool) or isinstance(v, float) and not math.isfinite(v) for v in metrics.values()):
                issues.append(f"line {index}: metrics must contain finite numeric values")
            try:
                output = artifact_path(root, record["artifact_path"])
                if not output.is_file() or output.stat().st_size == 0:
                    issues.append(f"line {index}: run artifact missing or empty")
                elif output.suffix.lower() in (".json", ".jsonl", ".txt", ".md", ".csv", ".tsv", ".log", ".yaml", ".yml", ".toml"):
                    try:
                        if PLACEHOLDER.search(output.read_text(encoding="utf-8")):
                            issues.append(f"line {index}: run artifact contains unresolved placeholders")
                    except UnicodeError:
                        issues.append(f"line {index}: text run artifact is not valid UTF-8")
            except (WorkspaceError, TypeError):
                issues.append(f"line {index}: unsafe run artifact path")
        else:
            if any(not isinstance(record[k], str) or not record[k].strip() for k in required):
                issues.append(f"line {index}: source fields must be nonempty strings")
                continue
            parsed = urlparse(record["url"])
            if parsed.scheme not in ("http", "https") or not parsed.netloc or parsed.hostname == "example.invalid":
                issues.append(f"line {index}: source URL must be an actual HTTP(S) source")
            try:
                datetime.fromisoformat(record["checked_at"].replace("Z", "+00:00"))
            except ValueError:
                issues.append(f"line {index}: checked_at must be an ISO date or timestamp")
    return issues


def check_gate(root: Path, manifest: dict, stage: str) -> dict:
    if stage not in STAGES:
        raise WorkspaceError(f"Unknown stage: {stage}")
    findings: dict[str, list[str]] = {}
    if manifest.get("synthetic_demo"):
        findings[MANIFEST] = ["synthetic demo workspaces cannot pass research gates"]
    for relative in STAGES[stage]:
        try:
            if relative.endswith(".jsonl"):
                issues = _ledger_issues(root, relative, runs=relative.endswith("runs.jsonl"))
            else:
                issues = _text_issues(artifact_path(root, relative))
        except WorkspaceError as error:
            issues = [str(error)]
        if issues:
            findings[relative] = issues
    return {"stage": stage, "passed": not findings, "required_artifacts": list(STAGES[stage]), "issues": findings, "note": "Offline structural checks only; this does not verify scientific claims or certify peer review."}


def workspace_status(root: Path, manifest: dict) -> dict:
    return {"workspace": str(root), "name": manifest.get("name", root.name), "topic": manifest["topic"], "synthetic_demo": bool(manifest.get("synthetic_demo")), "gates": [check_gate(root, manifest, stage) for stage in STAGES]}
