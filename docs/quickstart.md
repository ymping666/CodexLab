# Start a research workspace

Use Codex's native subagents through your existing eligible Codex sign-in. CodexLab's default workflow does not require a separate model API key or an API-based agent scheduler; your Codex usage limits still apply.

You need Python 3.11+ and a local Codex client that supports the native subagent configuration. See [compatibility and verification](codex-compatibility.md) for the observed client version and limits of validation.

From this repository root:

```console
python -m codexlab doctor
python -m codexlab init my-lab --topic "Efficient retrieval for scientific question answering"
python -m codexlab prompt my-lab
python -m codexlab status my-lab
```

`init` creates a new directory and refuses an existing target. It copies the five-role contract, four custom agent files, kickoff prompt, and incomplete research artifacts. It does not call a model or start a Codex session. For a reusable installed command, install the local package with `python -m pip install -e .`; then `codexlab` works from other directories. No runtime Python dependencies are required.

Open **the generated `my-lab` directory** as the project in Codex. Inspect its generated `.codex` configuration and complete Codex's project trust prompt for this vetted workspace. An untrusted project's local configuration may be disabled. Opening the source repository alone does not activate agent files nested inside a separate generated lab.

Fill `research/brief.md` with the exact question, available data/model/compute access, time budget, success/falsification criteria, and exclusions. Keep unfilled `TODO` markers visible until decisions are made. Read `research/kickoff.md`, paste its code-block prompt into the new project's Codex chat, and explicitly request the named agents. The primary session becomes PI; literature, method, experiment, and reviewer are native specialists. Inspect actual child threads to confirm your client's support.

If sign-in is needed, use `codex login` and your eligible ChatGPT account. [Official authentication documentation](https://learn.chatgpt.com/docs/auth) describes the supported sign-in paths. CodexLab does not read credentials or replace your account limits.

## Inspect progress and gates

From the repository root or an installed environment:

```console
python -m codexlab gate my-lab scope
python -m codexlab gate my-lab literature
python -m codexlab gate my-lab method
python -m codexlab gate my-lab experiment
python -m codexlab gate my-lab review
python -m codexlab serve my-lab --port 8765
```

Open the printed loopback URL for the read-only dashboard. It shows workspace artifacts and structural checks; it does not execute agents. Stop it with Ctrl+C. `--json` is available for `doctor`, `status`, and `gate`.

Fresh artifacts fail gates until substantive content and evidence replace the template markers. The PI enforces the dependency order `scope -> literature -> method -> experiment -> review` and checks prerequisite decisions before continuing. CLI gates inspect each stage independently; they do not persist an advancement state. Passing a gate proves only the checked structural requirements. The PI reads the contents, decides when to continue, and records reasons in `research/decisions.md`. There is no `advance` command or autonomous paper-submission flow.

## Evidence records

The literature agent appends one JSON object per opened source to `evidence/ledger.jsonl`. Required keys are `title`, `url`, `checked_at`, and `claim`. Example schema below is illustrative; do not copy it as verified evidence:

```json
{"title":"Actual opened primary paper title","url":"https://actual-primary-source.example/paper","checked_at":"2026-10-01","claim":"A precise claim supported by the opened source","id":"E001","source_location":"Section or figure","limitations":"What this source cannot establish"}
```

The experiment agent appends actual executed runs to `experiments/runs.jsonl`, with `run_id`, `command`, `seed`, numeric `metrics`, and an existing relative `artifact_path`. Preserve code/data hashes, environment and deviations too. A valid null result has real measurements; a crashed run must retain its failure log and must not acquire invented metrics to pass a gate.

The reviewer reads original evidence and run artifacts, checks closest prior art, and attempts reproduction within the agreed budget. A final report can recommend revise, stop, or ready for human review. It cannot guarantee publication.

## Demo and real toy measurements

```console
python -m codexlab demo demo-lab
python -m codexlab serve demo-lab
python examples/toy_regression.py --output examples/output/toy-regression
```

The `demo` workspace contains invented illustrative fixtures labeled synthetic and is deliberately barred from passing research gates. The separate toy regression script genuinely computes offline synthetic measurements and writes reproducible raw records. Neither verifies native model execution or a research contribution. See [example details](../examples/README.md).
