"""Prepare a self-contained role-picker fragment from this installed Skill (stdlib only)."""

from __future__ import annotations

import argparse
import json
import re
import stat
import sys
from pathlib import Path

SLOTS = ("pi", "literature", "method", "experiment", "reviewer")


class PrepareError(ValueError):
    pass


def safe_path(value: str | Path) -> Path:
    path = Path(value)
    if ".." in str(path).replace("\\", "/").split("/"):
        raise PrepareError("Parent traversal is not supported.")
    path = path.absolute()
    for item in (path, *path.parents):
        try:
            attributes = getattr(item.lstat(), "st_file_attributes", 0)
        except FileNotFoundError:
            attributes = 0
        if item.is_symlink() or attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
            raise PrepareError(f"Symlink/junction/reparse paths are not supported: {item}")
    return path


def valid_selection(selection: object, categories: dict) -> bool:
    return (isinstance(selection, dict) and set(selection) == set(SLOTS)
            and all(selection[slot] is None and slot != "pi"
                    or selection[slot] in {profile["name"] for profile in categories[slot]["profiles"]}
                    for slot in SLOTS))


def validate_catalog(catalog: object) -> dict:
    if not isinstance(catalog, dict) or catalog.get("schema_version") != 2:
        raise PrepareError("Expected role catalog schema_version 2.")
    items = catalog.get("categories")
    if not isinstance(items, list) or len(items) != 5:
        raise PrepareError("Expected five research categories.")
    categories = {item["id"]: item for item in items}
    if set(categories) != set(SLOTS):
        raise PrepareError("Unexpected or duplicate role category IDs.")
    names: set[str] = set()
    for slot in SLOTS:
        category = categories[slot]
        if category.get("required") is not (slot == "pi"):
            raise PrepareError("Only PI is required.")
        profiles = category.get("profiles")
        if not isinstance(profiles, list) or not profiles:
            raise PrepareError(f"Expected at least one profile for {slot}.")
        for profile in profiles:
            if not all(profile.get(key) for key in ("name", "style", "summary", "deliverable", "instructions", "watch_out")):
                raise PrepareError(f"Incomplete profile in {slot}.")
            if profile["name"] in names:
                raise PrepareError("Profile names must be unique.")
            names.add(profile["name"])
        if category.get("default") not in {profile["name"] for profile in profiles}:
            raise PrepareError(f"Unknown category default for {slot}.")
    presets = catalog.get("presets")
    if not isinstance(presets, list) or not presets:
        raise PrepareError("Expected at least one recommendation.")
    preset_ids = set()
    for preset in presets:
        if not all(preset.get(key) for key in ("id", "label", "when", "tradeoff")) or not valid_selection(preset.get("selection"), categories):
            raise PrepareError("Incomplete or invalid preset.")
        if preset["id"] in preset_ids:
            raise PrepareError("Recommendation IDs must be unique.")
        preset_ids.add(preset["id"])
    entries = catalog.get("entry_points")
    if not isinstance(entries, list) or not entries:
        raise PrepareError("Expected at least one onboarding entry point.")
    entry_ids = set()
    for entry in entries:
        if not all(entry.get(key) for key in ("id", "title", "summary", "reason", "tradeoff")) or not valid_selection(entry.get("selection"), categories):
            raise PrepareError("Incomplete or invalid onboarding entry point.")
        if entry["id"] in entry_ids:
            raise PrepareError("Onboarding entry point IDs must be unique.")
        entry_ids.add(entry["id"])
    return categories


def embed(fragment: str, element_id: str, value: object) -> str:
    pattern = r'(<script id="' + re.escape(element_id) + r'" type="application/json">)(.*?)(</script>)'
    payload = json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    result, count = re.subn(pattern, lambda match: match[1] + payload + match[3], fragment, flags=re.S)
    if count != 1:
        raise PrepareError(f"Missing or duplicate embedded data element: {element_id}")
    return result


def prepare(output: str | Path, selection: object = None, ignore_saved_state: bool = False) -> Path:
    target = safe_path(output)
    if target.exists():
        raise PrepareError(f"Output already exists; nothing overwritten: {target}")
    if not target.parent.is_dir():
        raise PrepareError("Output parent must already exist; this helper creates no research directories.")
    skill = safe_path(Path(__file__).absolute().parent.parent)
    catalog = json.loads(safe_path(skill / "references/catalog.json").read_text(encoding="utf-8"))
    categories = validate_catalog(catalog)
    if selection is not None and not valid_selection(selection, categories):
        raise PrepareError("Selection must contain exactly five slots, a valid PI, and valid names or null specialists.")
    fragment = safe_path(skill / "assets/ui/role-picker.html").read_text(encoding="utf-8")
    fragment = embed(fragment, "codexlab-style-catalog", catalog)
    fragment = embed(fragment, "codexlab-picker-options", {
        "selection": selection,
        "ignoreSavedState": bool(ignore_saved_state or selection is not None),
    })
    with target.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(fragment)
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    parser.add_argument("--selection", help="JSON object with pi, literature, method, experiment, reviewer; null disables a specialist")
    parser.add_argument("--ignore-saved-state", action="store_true")
    args = parser.parse_args(argv)
    try:
        selection = json.loads(args.selection) if args.selection is not None else None
        target = prepare(args.output, selection, args.ignore_saved_state)
    except (PrepareError, OSError, ValueError, KeyError, TypeError) as error:
        print(f"codexlab role picker: {error}", file=sys.stderr)
        return 2
    print(f"Prepared configuration-only role picker: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
