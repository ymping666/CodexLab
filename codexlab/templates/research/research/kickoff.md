# Copy this prompt into Codex in this project

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
Use CodexLab gates for structural checks and PI judgment for scientific decisions.
An independent reviewer must inspect original evidence before final delivery.
Stop at the agreed budget or a concrete evidence/resource blocker.
Return artifact paths, observed results, uncertainties, and the next human decision.
```

This prompt begins a native Codex conversation. The CLI initializes files and checks artifacts; it does not spawn model sessions itself.
