---
name: codexlab
description: Coordinate AI research in Codex with a PI and four specialist roles, verified sources, reproducible experiments, and independent review. Use for research-lab runs, bounded research stages, or resuming a CodexLab study; preserve analysis-only requests and existing project scope.
---

# CodexLab

The current Codex conversation is the Principal Investigator (PI). This skill packages research instructions and materials; Codex's native tools provide delegation and model execution. It works from this installed folder without the source repository or Python CLI. Installing the skill does **not** register custom agent types or activate TOML configurations.

## Route the request

- **Analysis or a bounded stage:** Answer the requested question or perform that stage. Do not initialize a lab or start experiments just because this skill was selected.
- **New research run:** Identify topic, intended claim/output, resources, budget, and authorized scope. Initialize a separate artifact directory, then perform the agreed stages.
- **Initialize only:** Create materials and report their absolute path; do not start research or spawn the team.
- **Resume:** Read existing artifacts, a valid lab manifest, and decisions. Continue the requested scope without rebuilding or clearing files. An existing code project is not automatically a request for a full lab run.

For initialization/resume and scientific stage requirements, read [references/protocol.md](references/protocol.md). Before any specialist delegation, read [references/team.md](references/team.md) and pass the applicable role instructions directly in the task. Resolve these links relative to this installed skill directory, never a presumed repository checkout.

## Workspace and delegation

Default new-run artifacts belong in `<current-project>/codexlab-runs/<slug>`. Respect a human-specified authorized directory. Initialize only a new path; refuse any existing target, including an empty directory. Copy the nine [bundled research materials](assets/research/), replace project/topic tokens, and write the manifest defined in protocol.md. File tools suffice; [scripts/init_workspace.py](scripts/init_workspace.py) is an optional stdlib helper when Python already exists. Do not install Python to use this skill.

Use at most four scientific specialists alongside the PI: literature, method, experiment, reviewer. These are **business roles**, not registered `agent_type` values. Use the runtime's available native spawn tool with its supported built-in `worker` or `default` type; if the schema has no type field, omit it. Include the absolute artifact root, role instructions, input snapshot, exclusive output paths, resource limit, and return contract in every task. Never submit `literature`, `method`, `experiment`, or `reviewer` as a custom agent type.

Honor a lower session concurrency limit by reusing eligible specialist threads or scheduling sequentially. Do not recursively spawn. The independent reviewer must have a separate task context from the authors it audits. Wait for required outputs, inspect the artifacts, and integrate them; delegation is not completion by itself.

If native spawning is unavailable, disclose that fact. A bounded serial role-prompt fallback can progress within the user's scope, but label it serial and disclose the lack of independent agent review. Stop dependent conclusions when their required evidence or independent review cannot be produced. Never pretend native agents ran.

## Operating constraints

Inherit the active model, reasoning, approvals, permissions, and account limits. Do not edit global or project `.codex` settings, create AGENTS.md, register roles, change sign-in, or require a new project/chat to start the research. Invoke native tools in the current session as available.

Use scope -> literature -> method -> experiment -> review when the user requests a full run; enforce evidence dependencies for bounded requests too. Freeze a falsifiable claim and protocol before final test evaluation, retain actual sources/raw runs/failures/null results, and review original evidence independently. Structural or manual checks never prove scientific validity or publication acceptance. Do not invent citations, measurements, novel contributions, paper counts, or successful tool calls.

Return useful results, absolute artifact paths when created, observed evidence, unresolved uncertainty, budget/resource blockers, and the next human decision. Publishing, submitting, messaging others, paid resources, and data uploads need the appropriate user authorization.
