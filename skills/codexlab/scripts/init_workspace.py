"""Optional, standalone CodexLab Skill workspace initializer (Python 3.11+).

The default Skill workflow can copy assets with Codex file tools instead.
This helper neither imports CodexLab nor configures or executes agents.
"""

from __future__ import annotations

import argparse
import json
import re
import stat
import sys
from datetime import datetime, timezone
from pathlib import Path

RESEARCH_FILES = frozenset({
    "research/brief.md",
    "research/decisions.md",
    "literature/prior-art.md",
    "evidence/ledger.jsonl",
    "method/proposal.md",
    "experiments/plan.md",
    "experiments/results.md",
    "experiments/runs.jsonl",
    "review/report.md",
})
ALLOWED_TOKENS = {"{{PROJECT_NAME}}", "{{TOPIC}}"}


class InitError(ValueError):
    """A workspace cannot be initialized without violating its copy contract."""


def _check_path(path: Path) -> None:
    if ".." in str(path).replace("\\", "/").split("/"):
        raise InitError("Parent traversal ('..') is not allowed.")
    for item in (path, *path.parents):
        try:
            attributes = getattr(item.lstat(), "st_file_attributes", 0)
        except FileNotFoundError:
            attributes = 0
        if item.is_symlink() or attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
            raise InitError(f"Symlink and junction/reparse paths are not supported: {item}")


def initialize(target_value: str | Path, topic: str) -> Path:
    """Copy only the Skill's research artifacts into an exclusive new directory."""
    topic = topic.strip()
    if not topic:
        raise InitError("A nonempty research topic is required.")
    target_input = Path(target_value)
    _check_path(target_input)
    target = target_input.absolute()
    _check_path(target)
    if target.exists():
        raise InitError(f"Target already exists; nothing overwritten: {target}")
    if not target.parent.is_dir():
        raise InitError(f"Parent directory must already exist: {target.parent}. Create the research container first.")

    assets = Path(__file__).absolute().parent.parent / "assets" / "research"
    _check_path(assets)
    if not assets.is_dir():
        raise InitError(f"Skill research assets are missing: {assets}")
    contents: dict[str, str] = {}
    for source in sorted(assets.rglob("*")):
        _check_path(source)
        if not source.is_file():
            continue
        relative = source.relative_to(assets).as_posix()
        text = source.read_text(encoding="utf-8")
        unsupported = set(re.findall(r"\{\{[^}]*\}\}", text)) - ALLOWED_TOKENS
        if unsupported:
            raise InitError(f"Unsupported template tokens in {relative}: {', '.join(sorted(unsupported))}")
        contents[relative] = text.replace("{{PROJECT_NAME}}", target.name).replace("{{TOPIC}}", topic)
    if contents.keys() != RESEARCH_FILES:
        missing = sorted(RESEARCH_FILES - contents.keys())
        extra = sorted(contents.keys() - RESEARCH_FILES)
        raise InitError(f"Incomplete Skill research assets. Missing: {missing}; unexpected: {extra}")
    manifest = {
        "schema_version": 1,
        "codexlab_version": "0.1.0",
        "name": target.name,
        "topic": topic,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "synthetic_demo": False,
        "entrypoint": "skill",
    }
    contents[".codexlab.json"] = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"

    try:
        target.mkdir()
    except FileExistsError as error:
        raise InitError(f"Target already exists; nothing overwritten: {target}") from error
    try:
        directories = {target / Path(relative).parent for relative in contents if Path(relative).parent != Path(".")}
        for directory in sorted(directories, key=lambda value: (len(value.parts), str(value))):
            _check_path(directory)
            directory.mkdir()
        for relative, text in contents.items():
            destination = target / relative
            _check_path(destination)
            with destination.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
    except (OSError, InitError, UnicodeError) as error:
        # Preserve the partial directory instead of deleting unrelated/concurrent files.
        raise InitError(f"Copy incomplete at {target}; no files were removed. Inspect it before choosing a new target. {error}") from error
    return target.resolve()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create research artifacts from this installed CodexLab Skill.")
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init", help="Create a new directory; its parent must already exist")
    init.add_argument("target")
    init.add_argument("--topic", required=True)
    args = parser.parse_args(argv)
    try:
        target = initialize(args.target, args.topic)
    except (InitError, OSError, UnicodeError) as error:
        print(f"codexlab skill: {error}", file=sys.stderr)
        return 2
    print(f"Created CodexLab Skill research artifacts: {target}")
    print("Continue in the current Codex conversation using $codexlab. No project configuration was changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
