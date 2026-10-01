# How CodexLab works

Many API-driven multi-agent frameworks require model credentials, separate inference billing, and an external orchestration runtime. CodexLab takes the native Codex route: researchers use their existing eligible Codex sign-in and native subagents, with no separate model API key on that path. Model usage remains subject to the user's Codex account and limits.

CodexLab is a local research workspace scaffold, workflow contract, and artifact validator. Codex supplies model execution and delegation. The Python CLI copies the scaffold, displays a kickoff prompt, checks files, and shows stage requirements. It does not implement a separate inference service or claim to control Codex sessions through an undocumented API.

The lab contains five roles: a PI in the primary Codex session and four specialists. The PI assigns bounded work and integrates evidence. Literature checks primary sources and collisions; method proposes a falsifiable approach; experiment implements and preserves raw runs; reviewer independently audits the original artifacts. Model and reasoning choices inherit from the active session. Role count is a design constraint, not an obligation to run all specialists simultaneously.

```mermaid
flowchart LR
  User[Human research owner] --> PI[PI: primary Codex session]
  PI --> L[Literature]
  PI --> M[Method]
  PI --> E[Experiment]
  PI --> R[Independent reviewer]
  L --> Sources[Verified evidence ledger]
  M --> Protocol[Falsifiable method]
  E --> Runs[Raw reproducible runs]
  Sources --> R
  Protocol --> R
  Runs --> R
  R --> PI
  PI --> Decision[Human review / revise / stop]
```

## Stage contracts

| Stage | Owner | Required artifacts | Scientific decision |
| --- | --- | --- | --- |
| Scope | PI | `research/brief.md` | Is the question measurable with available resources? |
| Literature | Literature | `literature/prior-art.md`, `evidence/ledger.jsonl` | Is the distinction plausible given the closest verified work? |
| Method | Method | `method/proposal.md` | Is the mechanism implementable and falsifiable? |
| Experiment | Experiment | `experiments/plan.md`, `experiments/results.md`, `experiments/runs.jsonl` | Do actual measurements support the bounded claim? |
| Review | Reviewer | `review/report.md` | Are evidence, baselines, protocol, and interpretation defensible? |

The validator detects incomplete templates, malformed records, and missing artifacts. It checks individual stages; the PI enforces dependency order and records stage decisions. It cannot determine whether an algorithm is sound, a paper is understood correctly, or a result generalizes. A structural pass remains subject to PI judgment and independent review. A successful experiment can produce a negative or null effect; a crashed process provides a failure log, not a fabricated successful metric.

## Evidence ownership and handoffs

Each specialist receives an input snapshot, output paths, exclusive write ownership, limits, and completion checks. Independent reads can run in parallel. Shared ledger writes are serialized. Review reads the original sources, code, and raw runs; it does not silently repair the evidence it evaluates. Every handoff carries file paths, evidence/run identifiers, observed facts, interpretations, uncertainty, and blockers.

`research/decisions.md` preserves scope changes, frozen protocols, deviations, and stage decisions. Paper text never becomes the only record of an experiment. Raw evidence includes actual commands, random seeds, code/data identity, environment, missing/failed runs, and outputs. Bounded searches preserve query/date limitations rather than assert proven novelty.

Stop at budget exhaustion, unavailable resources, invalidating leakage, unverified essential evidence, or a prior-art collision that defeats the claim. Keep the blocker and recovery action visible. Null results and baseline wins belong in the deliverable. Human researchers remain accountable for scientific claims and publishing decisions.
