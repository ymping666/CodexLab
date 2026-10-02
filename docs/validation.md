# Validation and limitations

Validation snapshot: 2026-10-02. Current automated results are available in [GitHub Actions](https://github.com/ymping666/CodexLab/actions).

## Verified

- The Skill passes the official skill-creator structure validator and the repository's resource/link checks.
- The official Skill installer downloads the public GitHub package. Local Codex discovers the installed Skill as enabled.
- The optional initializer works from an isolated installed folder without repository imports. It preserves UTF-8 and empty ledgers, rejects existing targets and unsafe paths, and produces a manifest compatible with optional artifact tools.
- Initialization-only and resume were exercised through file tools without Python. Resume preserved existing materials and changed only the decision log.
- The 25-test suite covers Skill initialization, existing-data protection, path confinement, malformed evidence, synthetic guards and read-only dashboard behavior. On the local Windows account, 23 passed and two real symlink tests were skipped for missing privileges; simulated reparse-point checks passed.
- GitHub Actions runs the checks on Windows and Linux with Python 3.11 and 3.13.
- The optional standalone project's TOML configuration was accepted by a local Codex runtime. This was a configuration check without model inference.

## Still to validate

Native specialist execution and complete scientific studies need observation in the user's eligible Codex session. Skill discovery and configuration parsing do not establish model execution, source truth, novelty, experimental validity or publication readiness.

The [concept image](../assets/codexlab-concept-demo.png) is a labeled illustration. The [dashboard screenshot](../assets/codexlab-dashboard-actual.jpg) shows the implemented read-only artifact view with synthetic data, not live agent activity. The toy example demonstrates experiment plumbing rather than a new research result.

The browser dashboard cannot start agents. Manual material assessment must be labeled manual; an automated structural gate pass is limited to the fields and files actually checked. See [compatibility](codex-compatibility.md) for a live client check.
