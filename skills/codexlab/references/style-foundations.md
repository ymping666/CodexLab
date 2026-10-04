# 学术方法与风格设计依据

核验日期：2026-10-03。以下公开论文与官方指南提供工作方法上的设计参考。风格名称、十五个档案和五种组合是 CodexLab 的设计抽象；尚未通过对比实验证明它们提高科研效率、可靠性或成果数量。每个档案继承完整职责合同，只调整问题优先级、行动顺序和交付重点。

## 已核验的来源与设计映射

| 公开来源 | 来源中的方法重点 | 本产品的设计推导 |
| --- | --- | --- |
| [George Heilmeier / DARPA：Heilmeier Catechism](https://www.darpa.mil/about/heilmeier-catechism) | 将目标、现有局限、价值、风险、投入、时间与检验节点连在一起。 | Aster 重整体交接；Quinn 优先会改变决定的信息。两者均记录预算和停止条件。 |
| [John R. Platt：Strong Inference，1964](https://pages.cs.wisc.edu/~markhill/science64_strong_inference.pdf) | 明确竞争假设，通过能区分它们的检查收窄解释。所链接版本为大学托管的原论文转录件。 | Orion 保留候选问题；Nova 设计机制区分；Flint 检索反证；Rook 查替代解释。这里不采纳论文中关于普适速度优势的主张。 |
| [Matthew Page 等：PRISMA 2020](https://www.prisma-statement.org/prisma-2020-statement) | 系统综述报告检索、筛选、流程与限制，提高证据过程的透明度。 | Atlas 明确范围、纳入条件和覆盖缺口。PRISMA 来自系统综述报告指南，在计算机科研中借鉴其透明流程，不强制每个任务做完整系统综述。 |
| [Claes Wohlin：Guidelines for Snowballing，2014](https://www.wohlin.eu/ease14.pdf) | 通过前向与后向引用迭代扩展来源，并记录起点及筛选过程。 | Scout 沿近期线索和引用网络探索；Atlas 关注覆盖。Scout 同时补查早期近邻，避免把近期热度当成可靠性。 |
| [Chris Olah 等：The Building Blocks of Interpretability，2018](https://distill.pub/2018/building-blocks/) | 组合可解释性方法，观察内部表示及其对输出的关系，并讨论解释界面的可靠性。 | Nova 从现象追问机制，把解释转为预测和区分检查。可视化或合理叙事本身不足以证实因果机制。 |
| [Zachary Lipton、Jacob Steinhardt：Troubling Trends in Machine Learning Scholarship，2018](https://arxiv.org/abs/1807.03341) | 讨论解释与猜测混淆、贡献归因困难、形式与实质脱节等研究报告问题。 | Mira 先检查简单强基线和组件必要性；Nova 明示竞争解释；Theo 标明假设边界；Sage/Rook 检查结论与证据是否相符。 |
| [Peter Bartlett、Shahar Mendelson：Rademacher and Gaussian Complexities，2002](https://www.jmlr.org/papers/volume3/bartlett02a/bartlett02a.pdf) | 风险界依赖明确的样本、损失与函数类条件。 | Theo 列清变量、前提、推导与反例，核对真实任务是否满足条件。不把特定理论界自动迁移到任意 AI 实验。 |
| [Nils Reimers、Iryna Gurevych：Reporting Score Distributions Makes a Difference，2017](https://aclanthology.org/D17-1035/) | 在所研究的随机训练任务中，单次分数可能误导方法比较。 | Vector 关注独立单位、多次运行的分布与不确定性；重复数应按任务及预算确定，不设统一的“充分种子数”。 |
| [Rishabh Agarwal 等：Deep RL at the Edge of the Statistical Precipice，2021](https://arxiv.org/abs/2108.13264) | 小运行次数和高方差下，需要体现评测不确定性。 | Vector 避免把单次变化写成稳健优势。RL 论文中的聚合方法需先核对是否适用于当前实验设计。 |
| [Greg Wilson 等：Best Practices for Scientific Computing，2014](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745) | 自动化工作流、保留参数及来源、版本控制、小步迭代反馈。 | Forge 优先完整运行链；Pulse 优先低成本前提检查。试跑与确认性评测分开，不反复偷看测试集筛选结果。 |
| [ACM SIGIR：Artifact Badging 官方指南](https://sigir.org/general-information/acm-sigir-artifact-badging/) | 区分材料可获取、可运行及他人实际重现结果等检查范围。 | Trace 区分记录核查、运行尝试与已完成复现；Sage 做整体证据审查。模型口头判断不能授予 ACM 徽章或替代外部审计。 |

## 同一职责的差异如何落地

- PI：整体组织、保留探索空间、决策收敛分别服务不同阶段；三者都承担预算、整合和阶段决定。
- 文献：系统覆盖、前沿追踪、反证优先改变检索顺序；三者都打开原始来源、保留范围及访问限制。
- 方法：机制解释、理论条件、最小实证改变论证入口；三者都保留竞争解释、公平对照和失败判据。
- 实验：工程执行链、统计精度、小步可行性改变检查重点；三者都保留原始数据、失败和偏离，服从已授权资源。
- 审查：综合覆盖、对抗检查、复现审计改变优先发现；三者都使用独立上下文并执行完整审查合同。

推荐组合按研究场景匹配这些策略，并注明协调成本、探索遗漏或确认性证据不足等取舍。用户的明确名单及排除项优先；选择组合不启动研究。具体档案在 [catalog.json](catalog.json)，操作与交接规则见 [styles.md](styles.md)。
