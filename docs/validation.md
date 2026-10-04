# Validation and limitations

Validation snapshot: 2026-10-04, v0.2 alpha. Automated results after publication are available in [GitHub Actions](https://github.com/ymping666/CodexLab/actions).

## Package and artifact checks

- The public Skill is self-contained and passes the official skill-creator structure validator and repository link/resource checks. The role catalog is validated and matches the embedded HTML copy. Public instructions invoke `$codexlab`, not the private trial name.
- Before this update, the official Skill installer downloaded the public GitHub package and local Codex discovered it as enabled. This release retains the same install path and Skill name; that earlier installation check is not a fresh download of v0.2.
- The 34-test Python suite passes with 32 successes and two real symlink tests skipped because the local Windows account lacks privileges. Simulated reparse-point checks pass. Tests cover isolated Skill initialization and menu preparation, UTF-8, empty ledgers, existing-data protection, path confinement, malformed evidence, synthetic guards and read-only dashboard behavior.
- The initializer and menu preparation helper work from isolated copies without repository imports. Menu preparation rejects invalid or cross-responsibility selections, incomplete entries, traversal and existing output files. The manifest remains schema version 1 and compatible with optional artifact tools.
- Initialization-only and resume were previously exercised through file tools without Python. Resume preserved materials and changed only the decision log.
- CI runs Python checks on Windows and Linux with Python 3.11 and 3.13. Browser interaction checks are included as a separate job. Configuring CI does not imply the remote jobs have already passed.

## Team-menu behavior

The public menu is checked in a real Edge browser against an isolated Skill copy. The checks cover four purpose entries without a preselection, per-responsibility adjustments, all five full presets, required PI, inactive specialists, keyboard operation, preserved choices when returning, explicit confirmed inputs, compatible legacy drafts, and delayed host-state updates.

Clipboard success, denial and absence are exercised. A simulated chat bridge verifies explicit submission, pending-state controls, duplicate prevention and manual retry after failure. There are no automatic sends or research calls. The checks cover 320 / 390 / 736px layouts and dark mode; they observe no JavaScript errors or horizontal overflow. Scripts write screenshots and results to temporary development storage, not research runs.

A separate independent first-use walkthrough of the local candidate selected literature exploration, changed the method style to Theo, returned to the summary and prepared the full instruction without starting research. The issue it identified with copy-button wording was corrected. These are development checks and an agent walkthrough, not a human usability study or a measurement of setup speed.

## Execution and scientific boundaries

Inline HTML and actual chat sending depend on the user's host. Text menus remain available when inline presentation is absent. Real host confirmation sending has not been automated by the browser suite; its bridge is simulated.

Local bounded v2 exercises observed native task handoffs and scoped analysis/review of supplied toy materials. Those observations do not establish that every user's client exposes delegation, that all fifteen styles execute equivalently, or that a complete scientific study succeeds. Installing or parsing a Skill does not establish source truth, novelty, experimental validity or publication readiness. Style effectiveness and preset quality need comparative evaluations.

The [team-menu screenshot](../assets/codexlab-team-setup.png) shows the implemented configuration UI. The [concept image](../assets/codexlab-concept-demo.png) remains a labeled illustration, and the [dashboard screenshot](../assets/codexlab-dashboard-actual.jpg) shows a separate read-only artifact tool with synthetic data. The toy example demonstrates experiment plumbing rather than a research contribution.

The dashboard cannot start agents. Manual assessment must be labeled manual; an automated structural gate pass is limited to the fields and files actually checked. Human researchers retain scientific and publishing decisions. See [compatibility](codex-compatibility.md) and [team setup](teams.md).
