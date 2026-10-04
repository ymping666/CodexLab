# Start with the CodexLab Skill

In Codex chat, install the self-contained Skill:

```text
$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab
```

On your next message, in the project where you want to do research:

```text
$codexlab Study efficient retrieval for scientific question answering.
Inspect available data, tools and budget, then begin the scope stage.
```

The installed Skill contains its own workflow, team instructions, templates and optional initializer. You do not need the source checkout, a separate project opening, a Python installation or another model API key. Use an eligible existing Codex sign-in; quotas and feature availability still apply. See [installation examples](../START_HERE.md) and [official Skills documentation](https://learn.chatgpt.com/docs/build-skills). If discovery fails after installation, check the Skill list and refresh or restart your client.

The current conversation is PI. It passes role instructions to available native subagents; it does not assume that installing the Skill registered four custom agent types. Model, tools, permissions and concurrency inherit from the current session. If native delegation is unavailable, the PI reports that limit and labels any serial fallback.

## Optional team setup

```text
$codexlab Show the guided team menu. Configure only; do not start research.
```

Choose a purpose, review responsibilities and adjust styles, then confirm the complete instruction in chat. Inline HTML is optional and host-dependent; text selection works without it. All fifteen named profiles, five full presets, configuration-only behavior and update guidance are described in [team setup](teams.md) and [installation](../START_HERE.md). A direct scoped research request does not need this extra step.

## Create or resume materials

Default output is `codexlab-runs/<topic-slug>/` inside the current project. The PI reports the actual output path. You can specify another authorized directory, ask for initialization only, or request review of existing material without starting a complete study.

```text
$codexlab Initialize codexlab-runs/retrieval for scientific retrieval reliability.
Create materials only; do not start research yet.
```

```text
$codexlab Continue codexlab-runs/retrieval from the recorded decisions.
Preserve existing evidence and runs; do not reinitialize the directory.
```

Fresh initialization refuses an existing target, including an empty directory. Resume reads the existing brief, ledgers and decisions, identifies the unfinished stage, and preserves prior records. Materials contain a CLI-compatible `.codexlab.json`; they do not contain a new project configuration or override your project's AGENTS.md.

## Research handoffs

The PI resolves the question, authorized resources, budget, primary metric, falsification and scope boundaries before dependent work. Progress is recorded in `research/decisions.md` through `scope -> literature -> method -> experiment -> review`.

| Stage | Required materials relative to the run directory |
| --- | --- |
| scope | `research/brief.md` |
| literature | `literature/prior-art.md`, `evidence/ledger.jsonl` |
| method | `method/proposal.md` |
| experiment | `experiments/plan.md`, `experiments/results.md`, `experiments/runs.jsonl`, raw outputs |
| review | `review/report.md` |

Only opened sources enter the evidence ledger. Actual executed runs retain commands, seeds, numeric measurements, raw artifact paths, code/data identity, environment and deviations. Failed, negative and null results remain visible. Independent review checks original evidence, not just summaries. Read the bundled [research protocol](../skills/codexlab/references/protocol.md) for record fields and handoffs.

Without Python, PI inspects materials using available file tools and records a manual assessment. It must not report an automated gate PASS. Structural checks do not establish source truth, novelty or publication readiness.

## Optional CLI and standalone project roles

For users who already have Python 3.11+, the source package provides optional initialization, validation and a read-only artifact dashboard:

```console
python -m pip install -e .
python -m codexlab status codexlab-runs/retrieval
python -m codexlab gate codexlab-runs/retrieval literature
python -m codexlab serve codexlab-runs/retrieval --port 8765
```

Run these from the source checkout or an installed environment, with the correct absolute run path when the research project is elsewhere. The dashboard does not execute agents or show live native session telemetry.

The optional CLI also creates an independent project with four custom TOML agents:

```console
python -m codexlab init standalone-lab --topic "Scientific retrieval reliability"
python -m codexlab prompt standalone-lab
```

For this advanced path only, open the generated directory as a separate trusted Codex project and start a new chat with `research/kickoff.md`. The Skill path does not require this switch. See [compatibility](codex-compatibility.md).

Synthetic `demo` fixtures are barred from passing research gates. The [toy regression example](../examples/README.md) computes genuine offline synthetic measurements; it is not a research contribution or an inference test.
