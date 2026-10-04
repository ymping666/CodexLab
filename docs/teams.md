# Choose your research team

CodexLab v0.2 keeps the same installation path and `$codexlab` command. Team configuration is optional: a direct request with a topic and task goes straight to that scope. For a menu:

```text
$codexlab 帮我选择研究团队，先只配置团队，不开始研究。
```

## Start with a purpose

| 用途 / Purpose | Suggested starting team | Boundary |
|---|---|---|
| 读论文，找研究方向 / Explore literature | Orion · Atlas · Nova | No experiment or independent review yet |
| 打磨一个研究想法 / Refine an idea | Quinn · Flint · Mira · Rook | No experiment; novelty still needs verified sources |
| 设计或推进实验 / Plan or advance experiments | Aster · Atlas · Nova · Forge · Sage | Execution still requires a task, resources and budget |
| 检查结果或复现问题 / Audit or reproduce | Aster · Flint · Mira · Forge · Trace | Inspect the actual supplied evidence; reproduction is not novelty |

These entry points choose candidate teams, not scientific stages. Selecting an experiment-oriented team does not authorize running experiments. When independent review is inactive, it remains pending; PI self-check does not replace it.

The optional HTML menu first asks what you want to do, then shows responsibilities and members together. Adjust a single row, return to the summary, and confirm the complete configuration in chat. Going back preserves adjustments; selecting a different purpose or a full preset replaces the candidate team.

Interactive rendering requires a host with inline HTML support. Otherwise Codex shows a text menu. A supported chat bridge can request a follow-up; other hosts offer copy or manual text selection. Send that instruction in chat to confirm. Saved menu state and copying alone are unconfirmed drafts. No local server, package installation or Python is needed for the ready menu.

## Five responsibilities, fifteen styles

| 职责 / Responsibility | Profiles |
|---|---|
| 研究负责人 / PI, current chat | Aster 综合统筹 · Orion 探索驱动 · Quinn 决策收敛 |
| 文献科学家 / Literature | Atlas 系统综述 · Scout 前沿雷达 · Flint 反证检索 |
| 方法科学家 / Method | Nova 机制驱动 · Theo 理论约束 · Mira 极简实证 |
| 实验科学家 / Experiment | Forge 工程复现 · Vector 统计稳健 · Pulse 小步验证 |
| 独立审查员 / Reviewer | Sage 综合审查 · Rook 对抗挑错 · Trace 复现审计 |

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
$codexlab 团队配置：PI=Orion；文献=Atlas；方法=Theo；实验=不启用；审查=不启用。先只配置团队，不开始研究。
```

Then supply your topic, available material and requested scope, for example:

```text
$codexlab 使用刚才的团队分析我提供的研究假设。
只做分析，不初始化目录、不运行实验。缺少来源或证明时明确指出。
```

You can configure and request a task together. Explicit names and exclusions prevail over recommendations. A scoped team change preserves other slots:

```text
$codexlab 把方法风格改为 Mira，其余保持原样。先只配置团队。
```

To resume a managed run, name its original directory and preserve evidence. Never initialize over an existing run. Original names Aster / Atlas / Nova / Forge / Sage and legacy manifests remain supported; see [installation and update guidance](../START_HERE.md).
