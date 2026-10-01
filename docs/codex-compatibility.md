# Codex compatibility and verification

Checked on 2026-10-01 with local `codex-cli 0.159.2`. This is an observed version, not a minimum supported version claim. OpenAI may change configuration or availability; inspect your client's behavior before relying on it.

CodexLab uses project `.codex/config.toml` with `[agents]`, `enabled = true`, and `max_concurrent_threads_per_session = 4`. This limit excludes the primary PI session. See the [official configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).

Each standalone `.codex/agents/*.toml` declares `name`, `description`, and `developer_instructions`. The four specialists omit model overrides. Ask for named specialist delegation in the kickoff prompt and inspect the client-visible agent threads. See [official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Eligible users can authenticate Codex with their ChatGPT account; CodexLab does not require an API key for that path. Account quotas, workspace permissions, client support, and feature availability still apply. Optional paid services or data providers may have their own credentials. See [official authentication documentation](https://learn.chatgpt.com/docs/auth).

## What has and has not been tested

- Local CLI version was read directly.
- Template TOML is checked for syntax and required role fields.
- Offline scaffold, artifact checks, packaging, and toy measurements can be validated without inference.
- On `0.159.2`, the generated project's configuration was accepted by `codex app-server --strict-config`; `config/read` returned effective `agents.enabled = true` and a four-subagent limit. This used a process-local project trust override with no persistent configuration edits and no inference turn. Before trust, that project layer was disabled.
- The shell sandbox used an independent runtime profile, so this check did not verify the human user's account session. A successful config read confirms parsing/effective configuration only.
- Native named-agent discovery, model execution, parallel task completion, and account entitlement require a live Codex session. Do not infer them from a TOML parse or toy experiment.

## Client smoke check

Run `codex --version` and `codex login status`. If needed, run `codex login` and complete the existing ChatGPT sign-in flow. Open the initialized research workspace in Codex and paste `research/kickoff.md`'s prompt. Ask the PI to delegate a tiny source inspection to `literature`, then report the discovered role name and artifact. Inspect the actual child thread before claiming native execution works for your setup.

If a client ignores project configuration or cannot load a custom role, report the concrete behavior and use serial role prompts explicitly as a fallback. Do not silently label that run native parallel orchestration. CodexLab does not disable approval/sandbox policy, handle credentials, or provide quota bypasses.
