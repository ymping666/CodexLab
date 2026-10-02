# Codex App compatibility and verification

The default entry point is the Codex App: open the downloaded source folder, request a new lab in chat, then open the generated lab as a separate project and start a new chat. Python, pip, a separately installed CLI, and a model API key are not user prerequisites for this file-copy and native-chat workflow. Use App sign-in with your eligible account; account quotas, workspace controls, and client feature availability still apply. See [official authentication documentation](https://learn.chatgpt.com/docs/auth).

Official documentation describes requesting subagents in App chats and inspecting their threads. The scaffold supplies four named specialists with `name`, `description`, and `developer_instructions`; model and reasoning settings inherit. Actual named-agent discovery and execution must be confirmed in your client. See [official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Project `.codex/config.toml` enables agents with a four-subagent limit, excluding the primary PI session. See [official configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference). Project-local configuration loads only for trusted projects. Review the generated files and use the App's trust controls before starting a new chat in the generated directory. Copying files or opening the source repository alone does not establish activation; current-chat hot loading is not promised. See [official advanced configuration](https://learn.chatgpt.com/docs/config-file/config-advanced).

## Verified scope

- Observed local runtime: `codex-cli 0.159.2` on 2026-10-01. This is not a minimum supported version promise or a guarantee about every App distribution.
- All template TOML files parsed, including four required role schemas.
- Generated project configuration was accepted by `codex app-server --strict-config`; `config/read` returned enabled agents and the four-subagent limit. A process-local trust override was used without persistent config edits or an inference turn. Before trust, the project layer was disabled.
- The shell sandbox had an independent runtime profile, so that check did not validate the human account's App session.
- Offline scaffold, artifact checks, packaging, and toy calculations were tested separately. They do not verify native model execution.
- The App-first guide is a file-copy/chat handoff contract. Live named-agent discovery, account entitlement, concurrent scientific work, and end-to-end research quality remain unverified until exercised in a real eligible App session.

## App smoke check

Open the newly generated lab as its own App project, review trust, and start a fresh chat. Ask Codex to read `research/kickoff.md`, delegate a tiny source inspection to `literature`, and return the discovered role, child thread, and output artifact. Inspect the actual thread before claiming native execution works. No terminal command is necessary for this check.

If the client cannot discover a role, report its actual behavior. A serial role-prompt fallback must be labeled as such; it is not evidence of native parallel execution. Without Python, PI may inspect materials manually and record that fact, but must not report an automated CLI gate pass.

CLI and read-only dashboard checks are optional developer tools. Manually copied folders require a valid `.codexlab.json` before those tools recognize the workspace. CodexLab does not change global authentication, disable permissions, or bypass quotas.
