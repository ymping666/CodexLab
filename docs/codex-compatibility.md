# Skill and native-agent compatibility

The default distribution is `skills/codexlab`: install through Codex's `$skill-installer`, then invoke `$codexlab` in the current project. Official documentation supports installing Skills from other repositories, automatic discovery, and explicit `$skill-name` invocation. If a new Skill is not discovered, check the Skill list or restart the client. See [official Skills documentation](https://learn.chatgpt.com/docs/build-skills).

Use an eligible existing Codex account; no separate model API key is needed on that sign-in path. Account quotas, managed permissions, tools and feature availability still apply. See [official authentication documentation](https://learn.chatgpt.com/docs/auth).

## Skill roles and project agent manifests are different

The Skill does not install `.codex/config.toml` or register custom `agent_type` names. PI uses the current session's native delegation tools and supplies each specialist with its role instructions, absolute material root, exclusive output paths, budget and acceptance criteria. Literature, Method, Experiment and Reviewer are responsibilities assigned to native agents, not an assertion that four new runtime types were discovered.

The current session supplies model, permissions and concurrency. Use fewer simultaneous workers or reuse sessions if its limit is lower; do not change configuration to force a larger team. If delegation is unavailable, report the limitation and label serial role work as a fallback. See [official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

The optional CLI's standalone templates still include four custom TOML agents. That separate mode requires opening the generated project, reviewing/trusting configuration, and using a new session. Installing the Skill alone does not activate those manifests. Project trust behavior is described in [official advanced configuration](https://learn.chatgpt.com/docs/config-file/config-advanced).

## Team menu compatibility

The guided menu needs an explicitly available inline HTML rendering capability. Installing the Skill does not register a page in every Codex client. When that capability is absent, the same names, purposes and presets are available as text. Neither presentation needs a local server.

The optional chat bridge requests a complete configuration-only follow-up on a user click; clipboard/manual fallback lets the user send it themselves. Saved widget state is an unconfirmed draft, not authorization. Actual sending and confirmation depend on the host; automated browser checks use a simulated bridge. The menu does not start agents or control the read-only artifact dashboard.

## Verification boundaries

The [validation summary](validation.md) distinguishes Skill structure and installation checks, isolated initialization, optional CLI tests, and live research execution. A readable Skill or successful installation is not proof of correct delegation or research quality.

Historical runtime probe: local `codex-cli 0.159.2` on 2026-10-01 accepted the standalone project's configuration through `codex app-server --strict-config` and `config/read`, with enabled agents and a four-subagent limit. It used process-local trust, no inference turn and an independent sandbox profile. This is not a minimum supported version, an App account test, or validation of the new Skill workflow.

## Live client check

After installing, invoke `$codexlab` for a small bounded task in your research project. Ask PI to delegate one source inspection to a Literature worker, report the actual child thread and return a source-backed artifact. Inspect the child activity before claiming native execution. Compare returned paths to the run directory and check that existing project configuration was preserved.

No terminal command or project switch is required for that Skill check. Native dispatch and an end-to-end scientific study remain account/client-specific until observed. Manual material review must be labeled manual; the optional read-only dashboard is not an agent controller.
