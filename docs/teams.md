# Choose your research team

CodexLab v0.2 keeps the same installation path and `$codexlab` command. Team configuration is optional: a direct request with a topic and task goes straight to that scope. For a menu:

```text
$codexlab Help me choose a research team. Configure only; do not start research.
```

## Start with a purpose

| 用途 / Purpose | Suggested starting team | Boundary |
|---|---|---|
| 读论文，找研究方向 / Explore literature | Orion · Atlas · Nova | No experiment or independent review yet |
| 打磨一个研究想法 / Refine an idea | Quinn · Flint · Mira · Rook | No experiment; novelty still needs verified sources |
| 设计或推进实验 / Plan or advance experiments | Aster · Atlas · Nova · Forge · Sage | Execution still requires a task, resources and budget |
| 检查结果或复现问题 / Audit or reproduce | Aster · Flint · Mira · Forge · Trace | Inspect the actual supplied evidence; reproduction is not novelty |

These entry points choose candidate teams, not scientific stages. Selecting an experiment-oriented team does not authorize running experiments. When independent review is inactive, it remains pending; PI self-check does not replace it.

The optional HTML menu defaults to English. Its **English / 中文** select changes purpose cards, responsibilities, styles, presets, status messages and the full configuration instruction together, preserving members and the current view. You can explicitly request a Chinese menu in chat. Text menus and replies follow your requested or conversational language.

The menu first asks what you want to do, then shows responsibilities and members together. Adjust a single row, return to the summary, and confirm the complete configuration in chat. Going back preserves adjustments; selecting a different purpose or a full preset replaces the candidate team.

Interactive rendering requires a host with inline HTML support. Otherwise Codex shows a text menu. A supported chat bridge can request a follow-up; other hosts offer copy or manual text selection. Send that instruction in chat to confirm. Saved menu state and copying alone are unconfirmed drafts. No local server, package installation or Python is needed for the ready menu.

## Five responsibilities, fifteen styles

| 职责 / Responsibility | Profiles |
|---|---|
| PI, current chat / 研究负责人 | Aster Synthesis · Orion Exploration · Quinn Decision focus |
| Literature / 文献科学家 | Atlas Systematic mapping · Scout Frontier scan · Flint Counterevidence |
| Method / 方法科学家 | Nova Mechanisms · Theo Theoretical constraints · Mira Minimal empirical test |
| Experiment / 实验科学家 | Forge Engineering reproduction · Vector Statistical robustness · Pulse Small pilots |
| Reviewer / 独立审查员 | Sage Comprehensive audit · Rook Adversarial critique · Trace Reproduction audit |

Choose one PI style and normally at most one profile per specialist responsibility. Other responsibilities may be inactive. The current chat remains PI; runtime concurrency may require scheduling fewer workers at once. Names represent fictional instruction profiles, not real scholars, separate models, registered agent types or persistent memories.

See the bundled [style contracts](../skills/codexlab/references/styles.md), [catalog](../skills/codexlab/references/catalog.json) and [scholarly design references](../skills/codexlab/references/style-foundations.md). Styles change strategies and deliverables while preserving evidence, resource and independent-review requirements. Their effectiveness has not been established by comparative experiments.

## Five full presets

The menu keeps these under an optional section rather than asking newcomers to choose among all profiles immediately.

| 组合 / Preset | PI · Literature · Method · Experiment · Reviewer |
|---|---|
| 均衡推进 / Balanced | Aster · Atlas · Nova · Forge · Sage |
| 前沿探索 / Frontier | Orion · Scout · Nova · Pulse · Rook |
| 有限预算 / Lean | Quinn · Atlas · Mira · Pulse · Sage |
| 严谨验证 / Rigorous | Quinn · Atlas · Theo · Vector · Trace |
| 复现诊断 / Reproduction | Aster · Flint · Mira · Forge · Trace |

These are adjustable design heuristics, not proven best teams. Small pilots cannot establish final validity; theoretical checks need actual assumptions and proofs. Preset selection does not promise conference acceptance or paper counts.

## Explicit configuration and bounded tasks

```text
$codexlab Team configuration: PI=Orion; Literature=Atlas; Method=Theo; Experiment=inactive; Reviewer=inactive. Configure the team only; do not start research.
```

Then supply your topic, available material and requested scope, for example:

```text
$codexlab Use the configured team to analyze my supplied hypothesis.
Analysis only: do not initialize directories or run experiments. State missing sources or proofs.
```

You can configure and request a task together. Explicit names and exclusions prevail over recommendations. A scoped team change preserves other slots:

```text
$codexlab Switch Method to Mira; keep other roles unchanged. Configure only.
```

To resume a managed run, name its original directory and preserve evidence. Never initialize over an existing run. Original names Aster / Atlas / Nova / Forge / Sage and legacy manifests remain supported; see [installation and update guidance](../START_HERE.md).
