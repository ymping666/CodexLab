# CodexLab development

## First release

Build a small, inspectable research lab on native Codex orchestration. A user's signed-in Codex owns model execution; CodexLab owns project scaffolding, role instructions, handoff contracts and local evidence checks.

Primary product problem: many multi-agent frameworks ask researchers to configure model API keys, manage usage-based inference billing, and run an additional orchestration stack. CodexLab uses native Codex subagents in the user's existing eligible signed-in environment. Subscription usage limits still apply; the default path requires no separate model API key.

Development team: leader (integration and acceptance), product manager (positioning and launch assets), engineer 1 (Python tooling), engineer 2 (Codex templates and research protocol). This four-person build team is separate from the five research roles in the product.

## Decisions

- Five research roles: PI as the primary agent, Literature Researcher, Method Researcher, Experiment Engineer, Reviewer. The PI owns prioritization and synthesis, and closes or reuses subagent sessions to stay within the configured concurrency cap.
- No separate inference service, API SDK, credential scraping, quota workaround, or public shared subscription endpoint.
- Default models inherit from the user's Codex session. Account access and limits remain with Codex.
- The default product entry is an installable Skill: `$skill-installer` once, then `$codexlab` in the user's existing project. The installed `skills/codexlab` folder contains all role instructions, protocol, templates and the optional initializer. Do not require a checkout, project switch, or Python for user onboarding.
- Skill specialists use role instructions in native tasks rather than newly registered custom agent types. Installing the Skill does not change Codex configuration. Existing project-scoped TOML roles remain an advanced CLI path with separate trust/session requirements.
- Keep the Python 3.11+ standard-library CLI as optional tooling for repeatable setup and structural validation. Packaging may use setuptools; it does not become an inference dependency.
- Research gates check artifact completeness. Scientific validity, novelty and submission readiness require human assessment.
- Demo state and conceptual dashboard images are explicitly marked synthetic. Toy experiments demonstrate reproducibility, not a new scientific result.
- The project's target repository is https://github.com/ymping666/CodexLab. Social launch material is prepared locally for review.

## Acceptance

1. A fresh research workspace initializes without modifying the user's global Codex configuration.
2. Repeating initialization never overwrites a user's existing project.
3. Native agent TOML parses and matches the documented schema.
4. Empty templates and missing evidence fail gates with actionable diagnostics.
5. All documented CLI commands run from source and from an installed package.
6. Tests exercise real failure cases, including traversal and invalid workspace state.
7. README, Chinese onboarding, launch posts and PNG demo assets agree on implemented capabilities.
8. Validation distinguishes local tests, CLI configuration checks and live model sessions.
9. Skill initialization refuses existing targets, preserves empty ledgers and UTF-8, creates a compatible artifact manifest, and writes no `.codex` or AGENTS.md. Manual PI checks remain distinct from automated gate results.
10. An isolated installed Skill works without importing this repository. Test the public GitHub path through the official Skill installer, and independently exercise initialization-only and resume behavior in temporary fixtures.

Run the test suite with `python -m unittest discover -s tests -v`. See the final validation record in `RELEASE_CHECKS.md`.
