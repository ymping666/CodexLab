# Responsibilities, styles and team selection

The single selection directory is [catalog.json](catalog.json). It has five responsibility categories and three named profiles per category. Canonical descriptions and style instructions are English; `translations.zh-CN` provides Chinese display labels, summaries and cautions. See [styles.md](styles.md) for strategies and recommendation tradeoffs, [style-foundations.md](style-foundations.md) for scholarly design references, and [team.md](team.md) for the non-negotiable scientific contracts.

Names are fictional task identities, not real researchers, endorsements, distinct models, custom agent types or persistent memories. Published research practices inspire the strategies; they do not establish that these agents emulate their authors or improve scientific outcomes.

## Category and profile mapping

| Category ID | Responsibility / 中文职责 | Profiles and English working styles |
| --- | --- | --- |
| pi | Principal Investigator, current chat / 研究负责人 | Aster Synthesis / Orion Exploration / Quinn Decision focus |
| literature | Literature Scientist / 文献科学家 | Atlas Systematic mapping / Scout Frontier scan / Flint Counterevidence |
| method | Method Scientist / 方法科学家 | Nova Mechanisms / Theo Theoretical constraints / Mira Minimal empirical test |
| experiment | Experiment Scientist / 实验科学家 | Forge Engineering reproduction / Vector Statistical robustness / Pulse Small pilots |
| reviewer | Independent Reviewer / 独立审查员 | Sage Comprehensive audit / Rook Adversarial critique / Trace Reproduction audit |

The current chat remains PI whichever PI profile is selected. Default PI is Aster. Remaining categories may be inactive. Normally choose one profile per category, so a complete team is still five responsibilities with at most four child agents; honor lower runtime limits and stage dependencies. Do not spawn all selectable profiles.

## Resolve a selection

- Accept a name case-insensitively. A canonical category ID, English responsibility or Chinese responsibility selects its original default profile (Aster/Atlas/Nova/Forge/Sage), unless a style is specified. Resolve English or Chinese style phrases within the named category; ambiguous requests such as “reproduction style” without a category need clarification.
- Preserve old named requests and historical records. Atlas + Nova maps to literature + method with Aster coordinating, not a full team. Legacy preset aliases remain: 找方向=Aster+Atlas+Nova; 推实验=Aster+Nova+Forge+Sage; 帮我审=Aster+Sage; 完整团队=the five original profiles.
- Explicit names and exclusions prevail over a recommendation. A complete slot instruction such as `PI=Quinn; Literature=Flint; Method=Mira; Experiment=Pulse; Reviewer=Trace` confirms exactly those choices; Chinese slot labels remain supported. `inactive` or `不启用` means an inactive specialist slot; PI cannot be inactive. Do not silently fill omitted specialist slots in a new explicit named list. For a scoped change to an existing team, preserve unchanged slots.
- Two profiles from one category in a single-team request, an unknown name, or incompatible selections require resolving that conflict before dependent work. Do not silently discard, rename or spawn duplicates. An explicitly requested multi-perspective comparison can use bounded sequential passes within resources; it is not a default team-size change and must retain review independence.
- A recommendation may suggest a catalog preset with its scenario and tradeoff. Without context, provide a clearly labelled provisional suggestion, not a mandatory questionnaire. Recommendations are design heuristics, not experimentally proven best combinations or predictions of paper acceptance.

## Selection and execution

1. A menu/configuration request without science is configuration-only. Follow [presentation.md](presentation.md), show choices and usable chat instructions, then end. Create no research material, search no papers, run no experiment and spawn no researcher. A task-owned UI copy is permitted only for presentation. UI state is an unconfirmed draft; only an explicit user message confirms a team.
2. For a bounded task, map each name to its canonical responsibility and append its style overlay. Perform only the requested stage. Style does not add stages, relax evidence or authorize paid compute or experimentation.
3. For ordinary research without named selection, infer the smallest relevant team and mention the choice. A full run can use the original balanced profiles stage by stage; do not demand a menu first or spawn everyone simultaneously.
4. Missing prerequisites remain missing regardless of style. Inspect supplied evidence, state limits and offer a bounded plan; do not silently add an unselected profile or fabricate literature, theory, data or results. Small pilots are not final validation. Formal-looking reasoning is not a proven theorem.
5. Any reviewer style retains the full independent-review contract. With the reviewer slot inactive, mark independent review pending; PI self-check is not independent. Before a reviewed full-run verdict, resolve independent/human review. Respect explicitly requested pre-review stopping points.
6. Reuse author contexts where suitable, but review needs a context separate from the authors. If a review profile previously authored the artifacts, use a fresh review context. Names do not confer independence or memory.
7. For configuration-only work keep confirmed slots in chat. In an existing managed run, append explicitly requested team changes to research/decisions.md with names, categories, styles and catalog version; retain old decisions, artifacts and raw evidence. Resume reads existing choices; don't reinitialize. Older records without style metadata remain valid.

Report dispatch only after actual native calls. Pass canonical contracts into the runtime's built-in/default worker; these names and category IDs are not newly registered agent_type values. Disclose serial fallback and actual concurrency limits.

## Examples

```text
$codexlab 展示分类和不同风格，先不开始研究。
```

```text
$codexlab 推荐适合有限预算的搭配，先只配置团队。
```

```text
$codexlab 团队配置：PI=Quinn；文献=Flint；方法=Mira；实验=Pulse；审查=Trace。先只配置团队，不开始研究。
```

```text
$codexlab 让 Theo 检查我给出的假设能否支持这个命题，只做分析，不写文件或运行实验。
```

```text
$codexlab 继续 codexlab-runs/my-study，把审查风格改为 Rook，其余保持原样。保留已有证据，只核对团队配置。
```
