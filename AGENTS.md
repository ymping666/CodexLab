# CodexLab repository instructions

This repository develops and distributes the self-contained Skill at `skills/codexlab/`, plus optional Python CLI tooling. The source checkout is not an active research lab. Development, documentation, installation guidance, and tests must not automatically start a scientific project. Temporary test fixtures are permitted for authorized maintenance.

## Product entry

Default onboarding is `$skill-installer` with the GitHub path to `skills/codexlab`, then `$codexlab` in the user's existing research project. See START_HERE.md. Keep the installed folder self-contained: all references, roles, templates and optional scripts must resolve inside it, without requiring this repository or an installed Python package.

The active session is PI. The Skill passes Literature, Method, Experiment and Reviewer instructions into native subagent tasks. These are research responsibilities, not newly registered custom `agent_type` names. Installing a Skill does not register `.codex/agents` manifests. Inherit the session's model, permissions, tools and concurrency limits; do not edit project/global Codex config to make the Skill work.

## Research versus maintenance

For a research request, follow the explicitly selected Skill or the user's active lab contract. Match the user's requested scope, including analysis-only, initialization-only or resume. Keep generated artifacts separate from source files, normally under `codexlab-runs/<topic-slug>/`. Never reinitialize or clear an existing run to resume it.

An existing standalone research workspace's closer AGENTS.md remains its PI contract. The original templates at `codexlab/templates/research` and optional CLI remain supported for that advanced path; project-scoped TOML roles require their own trusted project/session. Do not impose that setup on Skill users.

## Maintenance checks

Keep the public repository focused on installable code, tests, user documentation and contributor guidance. Promotion drafts, social posts, image-generation prompts and internal coordination notes belong in ignored local storage.

Run the appropriate existing tests and `python scripts/check_release.py`. Preserve template placeholders `{{PROJECT_NAME}}` and `{{TOPIC}}`, empty ledgers, no-overwrite behavior, manifest compatibility and UTF-8 text. Test the Skill from an isolated copy that contains no surrounding repository. Do not treat parse checks, file-copy tests or manual material reviews as proof of model execution or scientific validity. The browser dashboard remains read-only.
