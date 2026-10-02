"""Offline release checks for App onboarding, templates and native manifests."""
from pathlib import Path
import re
import sys
import tomllib
from urllib.parse import unquote


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = []
    required_documents = ("README.md", "README.zh-CN.md", "AGENTS.md", "START_HERE.md")
    for filename in required_documents:
        if not (root / filename).is_file():
            errors.append(f"Missing App onboarding document: {filename}")
    documents = set(root.glob("*.md")) | set((root / "docs").glob("*.md")) | set((root / "marketing").glob("*.md"))
    for source in sorted(documents):
        filename = source.relative_to(root).as_posix()
        if not source.is_file():
            continue
        local_targets = []
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
            target = target.strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target_path = unquote(target.split("#", 1)[0].split("?", 1)[0])
            candidate = source.parent / target_path
            local_targets.append(candidate.resolve())
            if not candidate.exists():
                errors.append(f"{filename}: broken local link {target}")
        if filename in ("README.md", "README.zh-CN.md") and (root / "START_HERE.md").resolve() not in local_targets:
            errors.append(f"{filename}: link to START_HERE.md is required for the App-first entry path")
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
    bootstrap = root / "AGENTS.md"
    if bootstrap.is_file():
        instructions = bootstrap.read_text(encoding="utf-8")
        for required in ("codexlab/templates/research", ".codex", *sorted(allowed_tokens)):
            if required not in instructions:
                errors.append(f"AGENTS.md: bootstrap must document the canonical copy contract {required}")
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
    print("PASS: App entry links, bootstrap interpolation contract, hidden native configuration, four roles, model inheritance and native concurrency")
    print("This offline check does not run Codex inference or establish research validity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
