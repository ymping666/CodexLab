# CodexLab repository instructions

This directory distributes CodexLab source and templates. It is not an initialized research lab. Read START_HERE.md for study setup. Requests to develop, review, explain, test, or maintain CodexLab do not trigger this study bootstrap. Temporary test fixtures are permitted as part of authorized maintenance.

## App-native workspace bootstrap

Bootstrap only when the human explicitly asks to create a new research workspace and supplies a topic. Use the requested relative directory, defaulting to `my-lab`. Ask for a missing topic; do not invent one. The existing Codex App conversation and file tools perform the copy. The user needs no Python, pip, CLI, terminal commands, or separate model API key. Do not install a runtime to create a lab.

1. Resolve `codexlab/templates/research/` and destination to absolute paths. Keep the destination within this repository unless the human explicitly names another authorized workspace. Reject `..` traversal, symlinks, junctions/reparse points in source/destination ancestry, a missing parent, an empty topic, and any existing destination, including an empty folder. Do not merge, overwrite, or delete existing labs; report the conflict and request a new name.
2. Recursively enumerate **every file**, including dot directories and empty files. Preserve relative paths, especially `.codex/config.toml` and all four `.codex/agents/*.toml` files. Read UTF-8 text and prepare contents before writing: replace every literal `{{PROJECT_NAME}}` with the destination basename, and every literal `{{TOPIC}}` with the trimmed human topic. Keep remaining research `TODO` markers; do not fabricate evidence or decisions.
3. Exclusively create the new destination directory and each file; stop if another process creates the target first. Write UTF-8 and preserve empty ledgers. Use file tools or an available local shell internally without asking the user to type commands. Do not edit source templates, global Codex config, authentication, permissions, or model defaults. If blocked by permissions, report the actual blocker and offer START_HERE.md's manual-copy route.
4. Create valid `.codexlab.json` containing `schema_version: 1`, `codexlab_version` read from `codexlab/__init__.py` (currently `0.1.0`), `name` equal to target basename, `topic` equal to trimmed topic, `created_at` as the actual current ISO UTC timestamp, and `synthetic_demo: false`. This supports optional CLI inspection; it does not execute models.
5. Verify exact source/destination relative file sets plus manifest, UTF-8 readability, absence of substituted tokens, four role files, project config, and empty evidence/run ledgers. Report incomplete copying honestly. Do not silently continue or recursively delete a partial target. Remove only files certainly created by this operation when cleanup is authorized.
6. Return the generated directory's **absolute path** and a short file summary. Tell the human to open it as a separate Codex App project, review generated project config and App trust controls, then start a **new chat** asking Codex to read `research/kickoff.md`. End bootstrap at that handoff. Do not begin research, spawn the scientific team, or start another model process during the copy. Do not promise current-chat hot loading of another directory's configuration.

## Research workspace boundary

When the active directory contains its own `AGENTS.md` research contract and `research/brief.md` (normally also `.codexlab.json`), its closer instructions define the PI workflow. This includes manually copied workspaces awaiting a manifest. Do not reinitialize it or apply repository bootstrap there. A nested lab's own research contract takes precedence for lab work. Research artifacts belong in that lab, not the source repository. Creating another lab is a separate explicit request in the repository context.

## Project maintenance

Keep App setup usable without user-managed Python. The optional Python CLI copies and inspects materials and serves a read-only dashboard; native execution belongs to Codex. Preserve no-overwrite behavior and evidence provenance. Distinguish configuration tests, toy measurements, and live account-specific agent execution. Never label a manual material check an automated gate pass.
