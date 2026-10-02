# Start a new Codex App chat in this research project

Open this generated directory as a separate App project, review its `.codex` configuration and project trust, then start a new chat. Do not assume the repository's earlier chat loaded this directory's roles. Python, pip and CLI are optional, and no separate model API key is required for the eligible existing Codex sign-in path.

```text
Run CodexLab for this project. Read AGENTS.md and research/brief.md.
Act as PI and use the four native agents literature, method, experiment,
and reviewer for bounded specialist tasks; no recursive delegation.
First inspect resources and the brief, then begin the scope stage.
Explicitly report any unsupported named-agent/client behavior.
Give every specialist inputs, exclusive output paths, budget, and evidence requirements.
Follow scope -> literature -> method -> experiment -> review in dependency order.
Parallelize independent reads, and keep shared-file writes serialized.
Freeze the hypothesis and evaluation plan before final test evaluation.
Preserve actual sources, raw runs, failures, null results, and deviations.
If Python and CodexLab are already available, use CLI gates for structural checks.
Otherwise inspect materials manually through App file tools and record that fact.
Never claim an automated gate passed when only manual assessment occurred.
Use PI judgment for scientific decisions in either case.
An independent reviewer must inspect original evidence before final delivery.
Stop at the agreed budget or a concrete evidence/resource blocker.
Return artifact paths, observed results, uncertainties, and the next human decision.
```

This prompt explicitly requests native specialist delegation in the current App conversation. Verify actual role discovery and visible child threads; report unsupported behavior. Workspace creation only copied files and did not start the scientific team. The optional CLI inspects materials; it does not spawn model sessions itself.
