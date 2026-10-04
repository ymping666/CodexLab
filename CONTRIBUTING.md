# Contributing to CodexLab

Contributions are welcome for research role handoffs, source verification, reproducible experiments and artifact validation. Include a small reproducible example, describe the observed behavior, and distinguish real measurements from synthetic fixtures.

## Development setup

The optional Python tooling requires Python 3.11+. From the repository root:

```console
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/check_release.py
```

GitHub Actions checks Windows and Linux with Python 3.11 and 3.13.

## Project structure

- `skills/codexlab/`: independently installable Skill, role contracts, protocol, materials and optional initializer. Keep all runtime resources inside this folder.
- `codexlab/`: optional CLI, structural checks, read-only dashboard and standalone project templates.
- `tests/`: behavioral checks for artifact safety, evidence handling and isolated Skill initialization.
- `docs/` and `START_HERE.md`: installation, architecture, compatibility and validation guidance.
- `examples/`: reproducible toy demonstrations with clearly identified synthetic data.

Keep initialization exclusive: do not overwrite existing directories or research records. Preserve UTF-8, empty ledgers and manifest compatibility. Role instructions inherit the active Codex runtime's permissions and model settings. Structural checks must not be presented as scientific verification.

For Skill changes, exercise relevant behavior from a separate installed copy without repository imports. Update both README languages when user-facing behavior changes. Keep public documentation focused on usage and implementation.

The role catalog lives in `skills/codexlab/references/catalog.json`; refresh the embedded catalog in `assets/ui/role-picker.html` after changes. `scripts/check_release.py` checks their equality and validates the catalog. The optional preparation helper writes a new self-contained fragment and refuses overwrites.

Browser regression checks use Playwright as a development dependency, not a user installation prerequisite:

```console
npm install --no-save --package-lock=false playwright@1.62.1
npx playwright install chromium
node scripts/check_role_picker.cjs
```

To use an existing Edge installation, set `CHROMIUM_CHANNEL=msedge` in your shell. The script reads the public Skill (or an isolated Skill path supplied as its first argument) and writes screenshots/results to a new temporary directory. It exercises local selection, keyboard and narrow-screen layout, delayed state, copy fallback and a simulated chat bridge. It never sends a real chat message or starts research.
