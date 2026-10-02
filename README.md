# CodexLab

**A Multi-Agent Research Lab for Codex.**

**Already using Codex? Build your research lab on its native subagents—without another LLM API key.**

Many API-driven multi-agent frameworks ask you to configure model API credentials, pay for separate API calls, and wire up an orchestration runtime. CodexLab starts in the **Codex App you already sign in to**. Download the project, ask Codex to create your lab, and run the research in its own workspace.

Use your eligible existing Codex plan; normal quotas still apply. The default setup requires **no Python installation and no terminal commands from you**.

[GitHub](https://github.com/ymping666/CodexLab) · [简体中文](README.zh-CN.md) · [Start here](START_HERE.md) · [Product brief](marketing/product-brief.md) · [Roadmap](ROADMAP.md)

![CodexLab conceptual research workspace — synthetic example](assets/codexlab-concept-demo.png)

*Alpha · Concept image with synthetic example data. The [actual local dashboard screenshot](assets/codexlab-dashboard-actual.jpg) shows synthetic artifact status, not live agents.*

## Start in the Codex App

You need a signed-in Codex App with access to native subagents. Check support and plan eligibility against the current official documentation.

1. Go to [CodexLab on GitHub](https://github.com/ymping666/CodexLab), select **Code → Download ZIP**, and extract it.
2. Open the extracted **repository folder** as a project in the Codex App. Start a chat and paste the creation prompt below, replacing the topic.
3. Codex creates a new `my-lab` directory using the project templates. If that directory already exists, choose another name; creation must not overwrite it.
4. Open the generated **`my-lab` folder as a separate project** in the Codex App. Review its `AGENTS.md` and `.codex` configuration and complete the native trust prompt for the configuration you reviewed.
5. In a **new chat in that lab project**, paste the research-start prompt below.

There are **two project openings**: the repository for setup, then `my-lab` for research. Opening the repository does not load the nested lab's agent configuration. Project configuration may be ignored until the lab workspace is trusted.

**Creation prompt — in the repository project:**

```text
Read START_HERE.md and the repository-root AGENTS.md.
Using this repository's research templates, create a new ./my-lab
workspace for the topic: [YOUR RESEARCH TOPIC].

Use Codex's file tools. Do not require me to install Python or type
terminal commands. Do not overwrite an existing directory.
Generate the complete lab configuration, four native subagent role
files, and research artifacts, including research/kickoff.md.

Check that the generated configuration and relative role paths agree.
Do not start research in this repository session.
Report the absolute path of my-lab and tell me to open that folder
as a separate Codex App project, review/trust its configuration,
and start a new chat there.
```

**Research-start prompt — in the separately opened `my-lab` project:**

```text
Read this workspace's AGENTS.md and research/kickoff.md.
Follow the kickoff instructions and act as the PI / Lab Lead.
Start with the scope stage and delegate focused work to the configured
native subagents when useful. Ask me for the research decisions
specified in the workflow. Keep evidence and handoffs in this workspace.
If native roles are unavailable, explain the configuration issue.
```

## Your Codex runtime, five research roles

| Starting point | Many API-driven frameworks | CodexLab |
|---|---|---|
| Model access | Configure model API keys and providers | Use your signed-in Codex App |
| Model-call billing | Separate model API usage | Your eligible existing Codex plan and its quotas |
| Agent execution | Integrate an SDK or orchestration runtime | Codex's native subagents |
| Research setup | Assemble roles and handoffs yourself | Create a five-role lab from chat |

**Codex runs the agents.** CodexLab supplies project instructions, native-role configuration, and shared research artifacts. No additional model API key does not mean unlimited or free execution. Experiment compute, datasets, and external services you choose remain your own resources.

| Role | Responsibility | Expected handoff |
|---|---|---|
| **PI / Lab Lead** | Set direction, assign work, resolve disagreements | Research brief and synthesis |
| **Literature Scientist** | Verify sources, map prior art and collisions | Prior-art map and evidence ledger |
| **Method Scientist** | Turn a gap into a falsifiable method | Proposal and failure criteria |
| **Experiment Scientist** | Define baselines and record reproducible experiments | Evaluation plan, commands and results |
| **Reviewer** | Challenge claims, confounds and missing comparisons | Critical review and revision requests |

The PI is the root Codex session; the other four roles are native subagents. Use the roles needed for the current task rather than launching every role at once. Human researchers retain direction and final decisions.

## Keep the research handoffs inspectable

| Stage | Evidence requested |
|---|---|
| Scope | Clear question, boundaries and success/failure criteria |
| Literature | Prior-art report and source-backed ledger |
| Method | Concrete proposal and falsifiable assumptions |
| Experiment | Baselines, protocol, results and recorded runs |
| Review | Critical report and unresolved objections |

Research files make handoffs inspectable. Optional structural gates check required artifacts; human researchers verify scientific claims. Synthetic demos cannot pass those gates.

An **eight-week sprint target** could be a prior-art map, a falsifiable proposal, a reproducible experiment package, and an evidence-backed draft. Feasibility depends on scope and resources; publication or acceptance is not guaranteed.

## Optional CLI and artifact dashboard

For researchers who want command-line scaffolding or structural checks, the dependency-free CLI needs **Python 3.11+**. It is optional for the App setup above.

```bash
git clone https://github.com/ymping666/CodexLab.git
cd CodexLab
python -m pip install -e .
python -m codexlab doctor

# Alternative setup: use a new, non-existing target
python -m codexlab init ./my-lab --topic "Reliable evaluation of long-horizon AI agents"
python -m codexlab prompt ./my-lab

# Inspect artifacts and structural requirements
python -m codexlab status ./my-lab
python -m codexlab gate ./my-lab literature

# Explore synthetic data in a local read-only dashboard
python -m codexlab demo ./demo-lab
python -m codexlab serve ./demo-lab --port 8765
```

After CLI initialization, open `my-lab` as a separate trusted project in the Codex App and start a new research chat there. `init` and `demo` refuse to overwrite existing targets. `doctor` checks Python and the local Codex binary; it does not verify a live App session or actual agent execution. See `python -m codexlab --help`.

The dashboard at `http://127.0.0.1:8765` displays artifact status and gate results. It is **read-only and does not execute agents**. A separate local control UI is a future direction, not a delivered feature.

## Alpha delivery

- App-first setup instructions and a repository-level chat initialization workflow.
- A generated research workspace with a PI root session and four native subagent roles.
- Shared evidence, proposals, experiment records, and review handoffs.
- Optional Python CLI, synthetic demo, structural checks, and a read-only local dashboard.
- A [launch poster](assets/codexlab-launch-poster.png), [three Xiaohongshu posts](marketing/xiaohongshu.md), and [demo storyboard](marketing/demo-storyboard.md).

This alpha has not validated end-to-end scientific output or conference acceptance. See [development notes](DEVELOPMENT.md) for verification and [the roadmap](ROADMAP.md) for planned work.

Contributions are welcome for citation verification, reproducibility, reviewer feedback, and clearer handoffs. Include a reproducible example and distinguish observations from synthetic fixtures. Code is licensed under [MIT](LICENSE).

Implementation targets the official Codex [subagent](https://learn.chatgpt.com/docs/agent-configuration/subagents), [authentication](https://learn.chatgpt.com/docs/auth), and [configuration](https://learn.chatgpt.com/docs/config-file/config-reference) surfaces. CodexLab is an independent project, not an official OpenAI product.
