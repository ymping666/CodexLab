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
