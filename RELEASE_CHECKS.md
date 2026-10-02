# CodexLab v0.1.0 alpha validation

Validated locally on 2026-10-01 (Asia/Shanghai): Windows, Python 3.14.7, Codex CLI 0.159.2.

## Passed

- 17 unit tests: 16 passed; one actual symbolic-link test skipped because this Windows account cannot create symlinks. Simulated Windows reparse-point rejection passed.
- Fresh workspace scaffolding, topic substitution, overwrite refusal and artifact confinement.
- Empty templates, malformed ledgers, missing raw artifacts, nonfinite metrics and synthetic evidence rejected with actionable diagnostics.
- English and Chinese README local links; four native role manifests; model inheritance; four-subagent concurrency configuration.
- Wheel build and isolated local installation. Installed CLI initializes the complete workspace, including hidden `.codex` configuration and role files.
- CLI doctor reads executable availability/version only; it does not inspect credentials.
- Loopback dashboard returns HTML and JSON, rejects unrecognized paths, and does not accept write requests. Project text is HTML-escaped.
- Actual browser rendering of the local dashboard captured in `assets/codexlab-dashboard-actual.jpg`. Its data is an explicitly synthetic demo, not live agent activity.
- Toy regression example: five paired seeds reproduced from the saved raw measurements. This designed linear synthetic problem demonstrates experiment plumbing only.
- The generated project's `.codex/config.toml` was accepted by real `codex app-server --strict-config` and `config/read`. The enabled project layer returned `agents.enabled = true` and `max_concurrent_threads_per_session = 4`. Project trust was supplied only to that temporary process, without editing global configuration.

## Remaining validation

Native named-agent discovery, user-account model execution, and a complete real research workflow have not been validated. The shell environment uses an independent runtime profile; successful configuration parsing does not establish authentication or model entitlement. Open a generated workspace in the user's Codex, complete its native trust flow, and inspect the actual specialist threads when running the kickoff prompt.

At the time of this local validation, Python 3.11/3.13 and Linux checks were configured in GitHub Actions but had not run remotely. The local wheel was tested on Python 3.14.7. GitHub publication to https://github.com/ymping666/CodexLab was authorized subsequently; see the repository's Actions tab for current remote validation. No package registry or social post was published during this validation.

Structural research gates do not certify scientific validity, source accuracy, novelty, reviewer independence or conference readiness. These remain human research decisions.

## Earlier App-first onboarding update — 2026-10-02

- Default onboarding now uses Codex App chat to create a lab, followed by opening the generated lab as a separate project, reviewing/trusting its configuration, and starting a new chat. Python and terminal commands are optional user-facing tools.
- The expanded offline release check passes: App entry links, template interpolation contract, explicit hidden native configuration in package data, and all four specialist manifests.
- A local file-copy smoke check followed the bootstrap contract using PowerShell without Python for creation: all 16 template files, hidden `.codex` files, empty ledgers, UTF-8 topic replacement, and `.codexlab.json` were preserved. An existing target was refused without changing its content. The optional CLI subsequently recognized the resulting workspace and correctly reported its unfinished stages.
- Existing unit checks still pass: 16 passed and one real Windows symlink test skipped.
- Rebuilt the optional wheel and tested an isolated installation: updated App kickoff, optional-CLI research instructions, and all four hidden native roles are included.
- This is an offline contract check, not a captured end-to-end Codex App setup conversation. Live named-agent dispatch and model execution still require validation in the user's client and account.
- The shipped browser dashboard remains read-only. A separate CodexLab controller using App Server is planned, not implemented by this onboarding update.

## Skill-first distribution — 2026-10-02

The default entry is now the self-contained `skills/codexlab` package: install through `$skill-installer`, then invoke `$codexlab` in the current project. The earlier two-project onboarding is retained only for optional standalone TOML-agent workspaces.

- The official skill-creator `quick_validate.py` passed. Its authoring-only YAML dependency was placed in an ignored temporary validation directory; the distributed initializer uses the standard library only.
- Release checks passed for Skill frontmatter, internal resource links, exact nine-file research assets, interpolation tokens and optional legacy configuration.
- 25 unit tests ran: 23 passed, two actual Windows symlink tests skipped for missing account privileges. Simulated reparse-point checks passed.
- An isolated copy of the Skill initialized UTF-8 materials without repository imports. The compatible manifest supports optional `status`, `gate` and `serve`; it has no standalone kickoff file for `prompt`.
- Existing directories and real data were preserved; incomplete copying reported a blocker without recursively deleting concurrent notes.
- Independent Skill execution in a temporary fixture used PowerShell file tools without Python to initialize the nine materials and manifest. Initialization-only performed no research or agent delegation.
- No configuration edit or custom agent-type registration is required by this Skill. Native specialist delegation and complete scientific output remain separate live-client checks; filesystem tests do not establish them.
