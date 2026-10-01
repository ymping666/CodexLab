"""Offline release checks for documentation links and native role manifests."""
from pathlib import Path
import re
import sys
import tomllib


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = []
    for filename in ("README.md", "README.zh-CN.md"):
        source = root / filename
        if not source.is_file():
            errors.append(f"Missing {filename}")
            continue
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
            target = target.strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            candidate = source.parent / target.split("#", 1)[0]
            if not candidate.exists():
                errors.append(f"{filename}: broken local link {target}")
    template = root / "codexlab" / "templates" / "research"
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
            if name in names:
                errors.append(f"Duplicate native role name: {name}")
            names.add(name)
            if "model" in role:
                errors.append(f"{path.name}: default template should inherit user's model")
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"{path.name}: {exc}")
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
    print("PASS: README local links, four role manifests, model inheritance and native concurrency configuration")
    print("This offline check does not run Codex inference or establish research validity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
