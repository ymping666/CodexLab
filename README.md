# CodexLab

**A Multi-Agent Research Lab for Codex.**

**Already have a Codex plan? Install one Skill and start a research lab in your current project—without another LLM API key.**

Many API-driven multi-agent frameworks ask you to configure model API credentials, pay for separate API calls, and integrate another orchestration runtime. CodexLab uses your signed-in Codex environment and its native subagents. Install the Skill, invoke `$codexlab` with your research direction, and keep working in the project you already opened.

Use your eligible existing Codex plan; normal quotas apply. The default path requires no ZIP download, workspace switch, Python installation, or terminal commands from you.

[GitHub](https://github.com/ymping666/CodexLab) · [简体中文](README.zh-CN.md) · [Installation guide](START_HERE.md) · [Skill instructions](skills/codexlab/SKILL.md) · [Roadmap](ROADMAP.md)

![CodexLab conceptual research workspace — synthetic example](assets/codexlab-concept-demo.png)

*Alpha · Concept image with synthetic example data. The [actual local dashboard screenshot](assets/codexlab-dashboard-actual.jpg) shows synthetic artifact status; it is a separate, optional read-only tool.*

## Install, then invoke

In Codex chat, ask the official `skill-installer` to install this repository's self-contained Skill:

```text
$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab
```

After installation completes, try it in your **next message**:

```text
$codexlab Research direction: reliable evaluation of long-horizon AI agents.
Start with scope and prior art. Use native subagents for focused research
tasks when available, and keep the evidence and handoffs in this project.
```

Replace the research direction with yours. If the client has not discovered the Skill, refresh its Skill list or follow its reload/restart guidance, then try again. [The official installer](https://github.com/openai/skills/tree/main/skills/.system/skill-installer) supports GitHub repository paths; installation is complete only after your own Codex confirms it.

CodexLab writes research artifacts under:

```text
your-current-project/
└── codexlab-runs/
    └── <topic-slug>/
```

The invocation session acts as PI and uses four focused worker roles as needed. You stay in the current project; the default Skill workflow does not require opening a separate lab workspace.

## Native workers with explicit research roles

| Role | Responsibility | Expected handoff |
|---|---|---|
| **PI / Lab Lead** | Set direction, delegate work, resolve disagreements | Research brief and synthesis |
| **Literature Scientist** | Verify sources, map prior art and collisions | Prior-art map and evidence ledger |
| **Method Scientist** | Turn a gap into a falsifiable method | Proposal and failure criteria |
| **Experiment Scientist** | Define baselines and record reproducible experiments | Evaluation plan, commands and results |
| **Reviewer** | Challenge claims, confounds and missing comparisons | Critical review and revision requests |

The Skill packages **instructions, role contracts, and templates**. The PI passes a role contract inside each native worker's task. Installing the Skill does **not** register four custom TOML `agent_types` or change your project configuration automatically.

Actual native-agent execution depends on the spawn/delegation tools exposed by your Codex client. Run records must distinguish real child threads from work completed in the root session. If those tools are unavailable, CodexLab uses a visibly labeled **serial fallback**, which is not native parallel execution. Human researchers retain direction and final decisions.

## Use the Codex runtime you already have

| Starting point | Many API-driven frameworks | CodexLab Skill |
|---|---|---|
| Model access | Configure model API keys and providers | Use your signed-in Codex environment |
| Model-call billing | Separate model API usage | Your eligible existing Codex plan and its quotas |
| Agent execution | Integrate an SDK or orchestration runtime | Native Codex workers when available |
| Research setup | Assemble roles and handoffs yourself | Install a Skill, invoke it in your current project |

No additional model API key does not mean unlimited or free execution. Experiment compute, datasets, and external services you choose remain your own resources.

## Keep the research handoffs inspectable

Research runs collect scope, prior art, method proposals, experiment plans and records, and reviewer feedback. Inspect the files to see which claims have sources, which experiments actually ran, and which objections remain unresolved.

An **eight-week sprint target** could be a prior-art map, a falsifiable proposal, a reproducible experiment package, and an evidence-backed draft. Feasibility depends on scope and resources; publication or acceptance is not guaranteed.

The alpha has not established complete scientific output or conference acceptance. Installation, actual child-thread execution, and scientific evidence are separate things to verify.

## Optional CLI and project configuration

Advanced users can still create a **separate project-configured lab** with four custom TOML roles. That route needs Python 3.11+ for the CLI and requires separately opening/trusting the generated project. It is an alternative to the default Skill workflow.

```bash
git clone https://github.com/ymping666/CodexLab.git
cd CodexLab
python -m pip install -e .
python -m codexlab doctor

# Advanced project-configured workspace; target must not exist
python -m codexlab init ./my-lab --topic "Reliable evaluation of long-horizon AI agents"
python -m codexlab prompt ./my-lab
python -m codexlab status ./my-lab
python -m codexlab gate ./my-lab literature

# Optional synthetic example and read-only artifact dashboard
python -m codexlab demo ./demo-lab
python -m codexlab serve ./demo-lab --port 8765
```

For this advanced route, review and trust `my-lab` as a separate Codex project, then start a new chat reading `research/kickoff.md`. Optional `status`, `gate`, and `serve` also accept Skill-generated run directories; `prompt` belongs to the project-configured route with its kickoff file. Structural checks do not prove scientific claims or live agent execution. Synthetic demos cannot pass research gates.

The dashboard at `http://127.0.0.1:8765` is **read-only and does not execute agents**. A separate local control UI is a future direction. See `python -m codexlab --help` for optional commands.

## Alpha delivery

- A self-contained [CodexLab Skill](skills/codexlab/SKILL.md) for the current-project workflow.
- PI instructions, four native worker role contracts, and research artifact templates.
- Explicit evidence handoffs and a clearly labeled serial fallback when native spawning is unavailable.
- An optional project-configured CLI, synthetic demo, structural checks, and read-only local dashboard.
- A [launch poster](assets/codexlab-launch-poster.png), [three Xiaohongshu posts](marketing/xiaohongshu.md), and [demo storyboard](marketing/demo-storyboard.md).

See [development notes](DEVELOPMENT.md) for verification and [the roadmap](ROADMAP.md) for planned work. Contributions are welcome for citation checks, reproducibility, reviewer feedback, and clearer handoffs. Code is licensed under [MIT](LICENSE).

CodexLab is an independent project, not an official OpenAI product. Relevant official references: [Skill installer](https://github.com/openai/skills/tree/main/skills/.system/skill-installer), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), and [authentication](https://learn.chatgpt.com/docs/auth).
