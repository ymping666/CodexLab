"""Offline release checks for the installable Skill and optional legacy tooling."""
from pathlib import Path
import importlib.util
import json
import re
import sys
import tomllib
from urllib.parse import unquote


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = []
    required_documents = ("README.md", "README.zh-CN.md", "AGENTS.md", "START_HERE.md", "CONTRIBUTING.md", "docs/validation.md")
    for filename in required_documents:
        if not (root / filename).is_file():
            errors.append(f"Missing project onboarding document: {filename}")
    documents = set(root.glob("*.md")) | set((root / "docs").glob("*.md"))
    for source in sorted(documents):
        filename = source.relative_to(root).as_posix()
        if not source.is_file():
            continue
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
            target = target.strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target_path = unquote(target.split("#", 1)[0].split("?", 1)[0])
            candidate = source.parent / target_path
            if not candidate.exists():
                errors.append(f"{filename}: broken local link {target}")
    skill = root / "skills" / "codexlab"
    picker = skill / "assets" / "ui" / "role-picker.html"
    try:
        catalog = json.loads((skill / "references/catalog.json").read_text(encoding="utf-8"))
        spec = importlib.util.spec_from_file_location("release_picker", skill / "scripts/prepare_role_picker.py")
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        helper.validate_catalog(catalog)
        fragment = picker.read_text(encoding="utf-8")
        cached = re.search(r'<script id="codexlab-style-catalog" type="application/json">(.*?)</script>', fragment, re.S)
        if not cached or json.loads(cached[1]) != catalog:
            errors.append("Bundled role menu catalog differs from catalog.json")
        if len(fragment.encode("utf-8")) >= 1_000_000 or re.search(r"(?i)<!doctype|<html\b|<head\b|<body\b|https?://|fetch\s*\(|XMLHttpRequest|WebSocket", fragment):
            errors.append("Role menu must be a self-contained inline fragment under 1 MB")
        for path in skill.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".py", ".html", ".yaml", ".json"}:
                if "codexlab-v2" in path.read_text(encoding="utf-8"):
                    errors.append(f"Public Skill still invokes local-only name: {path.relative_to(root).as_posix()}")
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"Bundled role menu/catalog: {exc}")
    entry = skill / "SKILL.md"
    if not entry.is_file():
        errors.append("Installable Skill is missing skills/codexlab/SKILL.md")
    else:
        text = entry.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
        if not frontmatter:
            errors.append("Skill entrypoint requires YAML frontmatter")
        else:
            fields = frontmatter.group(1)
            name = re.search(r"^name:\s*([^\r\n]+)$", fields, re.M)
            description = re.search(r"^description:\s*([^\r\n]+)$", fields, re.M)
            if not name or name.group(1).strip().strip("\"'") != "codexlab":
                errors.append("Skill frontmatter name must be codexlab")
            if not description or not description.group(1).strip().strip("\"'"):
                errors.append("Skill frontmatter requires a nonempty description")
    linked_resources = set()
    for source in sorted(skill.rglob("*.md")):
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
            target = target.strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            candidate = (source.parent / unquote(target.split("#", 1)[0].split("?", 1)[0])).resolve()
            if not candidate.is_relative_to(skill.resolve()):
                errors.append(f"{source.relative_to(root).as_posix()}: Skill resource escapes its installed folder: {target}")
            elif not candidate.exists():
                errors.append(f"{source.relative_to(root).as_posix()}: missing bundled resource {target}")
            else:
                linked_resources.add(candidate)
    for relative in ("references/protocol.md", "references/team.md", "scripts/init_workspace.py", "assets/research"):
        candidate = (skill / relative).resolve()
        if not candidate.exists():
            errors.append(f"Skill is missing bundled {relative}")
        elif candidate not in linked_resources:
            errors.append(f"Skill instructions must link bundled {relative}")
    expected_assets = {
        "research/brief.md", "research/decisions.md", "literature/prior-art.md", "evidence/ledger.jsonl",
        "method/proposal.md", "experiments/plan.md", "experiments/results.md", "experiments/runs.jsonl", "review/report.md",
    }
    skill_assets = skill / "assets" / "research"
    actual_assets = {path.relative_to(skill_assets).as_posix() for path in skill_assets.rglob("*") if path.is_file()}
    if actual_assets != expected_assets:
        errors.append(f"Skill research assets must be self-contained: missing {sorted(expected_assets - actual_assets)}, unexpected {sorted(actual_assets - expected_assets)}")
    template = root / "codexlab" / "templates" / "research"
    allowed_tokens = {"{{PROJECT_NAME}}", "{{TOPIC}}"}
    found_tokens = set()
    for path in template.rglob("*"):
        if not path.is_file():
            continue
        tokens = set(re.findall(r"\{\{[^}]*\}\}", path.read_text(encoding="utf-8")))
        found_tokens.update(tokens)
        for token in sorted(tokens - allowed_tokens):
            errors.append(f"{path.relative_to(root).as_posix()}: unsupported interpolation token {token}")
    for token in sorted(allowed_tokens - found_tokens):
        errors.append(f"Research templates are missing the bootstrap interpolation token {token}")
    for path in skill_assets.rglob("*"):
        if path.is_file():
            unsupported = set(re.findall(r"\{\{[^}]*\}\}", path.read_text(encoding="utf-8"))) - allowed_tokens
            if unsupported:
                errors.append(f"{path.relative_to(root).as_posix()}: unsupported Skill interpolation tokens {sorted(unsupported)}")
    try:
        project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
        patterns = project.get("tool", {}).get("setuptools", {}).get("package-data", {}).get("codexlab", [])
        for required in ("templates/research/.codex/*", "templates/research/.codex/**/*"):
            if required not in patterns:
                errors.append(f"Package data must explicitly preserve hidden native config: {required}")
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"Package metadata: {exc}")
    agent_dir = template / ".codex" / "agents"
    role_files = sorted(agent_dir.glob("*.toml"))
    if len(role_files) != 4:
        errors.append(f"Expected four specialist manifests plus primary PI; found {len(role_files)}")
    names = set()
    for path in role_files:
        try:
            role = tomllib.loads(path.read_text(encoding="utf-8"))
            for key in ("name", "description", "developer_instructions"):
                if not isinstance(role.get(key), str) or not role[key].strip():
                    errors.append(f"{path.name}: missing nonempty {key}")
            name = role.get("name")
            if isinstance(name, str) and name in names:
                errors.append(f"Duplicate native role name: {name}")
            if isinstance(name, str):
                names.add(name)
            if "model" in role:
                errors.append(f"{path.name}: default template should inherit user's model")
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"{path.name}: {exc}")
    if names != {"literature", "method", "experiment", "reviewer"}:
        errors.append(f"Expected the documented native specialist names; found {sorted(names)}")
    try:
        config = tomllib.loads((template / ".codex" / "config.toml").read_text(encoding="utf-8"))
        agents = config.get("agents", {})
        if agents.get("enabled") is not True:
            errors.append("Native agents must be enabled")
        if agents.get("max_concurrent_threads_per_session") != 4:
            errors.append("Concurrency should allow four specialists, excluding primary PI")
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"Native project config: {exc}")
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS: self-contained Skill entry/resources/assets, documentation links, optional legacy native configuration and model inheritance")
    print("This offline check does not run Codex inference or establish research validity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
