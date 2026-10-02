# CodexLab 产品简报 · Alpha

## 定位与入口

**已经有 Codex 套餐，就用原生多智能体搭科研 Lab，无需另配 LLM API Key。**

英文定位：**A Multi-Agent Research Lab for Codex.**

第一层卖点：**Your Codex plan. Native subagents. No extra LLM API key.**

默认产品入口：**Codex App。下载项目，在聊天中创建 Lab，再打开 Lab 开始研究。** 不要求用户先安装 Python 或输入终端命令。

第二层价值：**五个科研角色，把文献、方法、实验与审查接起来。**

仓库：[ymping666/CodexLab](https://github.com/ymping666/CodexLab) · 使用说明：[START_HERE.md](../START_HERE.md)。

## 用户与问题

第一批用户已经购买了支持 Codex 的套餐、登录了 Codex，也想用多智能体做 AI 科研。许多 API 驱动框架要求另外配置模型 API Key、承担独立调用费用，并接入 SDK 或调度运行时。已有套餐与另搭 API 框架之间的接入门槛，是 CodexLab 要先解决的问题。

CodexLab 使用用户已登录的 Codex App 和原生子智能体。框架本身不调用模型 API，也不另造编排运行时，所以无需额外 LLM API Key。实际执行正常消耗用户合适套餐中的 Codex 额度，不等于无限或免费运行。

在这条路径上，再提供科研团队的组织方式：PI 和四个专门角色、共享材料与阶段检查。实验数据、计算资源和自行接入的外部服务仍由用户提供。

| 用户上手问题 | CodexLab 的回答 |
|---|---|
| 还要开模型 API 吗？ | 无需额外模型 API Key，使用已登录的 Codex |
| 我不想先装 Python、用终端怎么办？ | 默认下载 ZIP，在 Codex App 聊天中创建工作区 |
| 智能体由谁执行？ | Codex 原生子智能体 |
| 调用从哪里消耗？ | 已有合适套餐的 Codex 额度，资格和限制照常适用 |
| 科研如何分工？ | 根会话 PI 加文献、方法、实验、Reviewer 四个子智能体 |

## 默认闭环：两次打开

1. 在 GitHub 选择 **Code → Download ZIP**，下载并解压。
2. 将解压后的**仓库目录**作为项目在 Codex App 中打开，在聊天中说明主题并请求创建一个新的 `my-lab`。Codex 读取根 `AGENTS.md` 和 `START_HERE.md`，按模板生成工作区。
3. 创建阶段保留模板结构、隐藏 `.codex` 配置与四份角色文件，生成 `research/kickoff.md`；已有目标目录拒绝覆盖。创建完返回目标绝对路径，不在仓库会话开始科研。
4. 将生成的 **`my-lab` 作为独立项目打开**，审阅 `AGENTS.md` 和 `.codex` 配置，完成原生信任提示。
5. 在 **Lab 项目的新聊天**要求读取 `research/kickoff.md`，由 PI 从 Scope 开始，再按需要委派原生子智能体。
6. 科研输出留在 Lab 的共享文件中；研究者处理关键决策、查证主张并决定继续或返工。

这不是“打开仓库就自动加载子目录角色”。初始化与科研是两个项目上下文；未信任的工作区配置可能被忽略，也不承诺同一仓库会话热加载新角色。

中英文可复制的创建与科研启动提示放在两份 README 中，默认目标为 `my-lab`，研究主题由用户替换。

## 科研角色与开发团队

用户的科研团队有五个角色：

| 角色 | 职责 | 交接材料 |
|---|---|---|
| PI / Lab Lead | 方向、委派、综合与人的决策 | 研究简报和综合结论 |
| Literature | 来源核实、已有工作与创新碰撞 | 文献地图和证据记录 |
| Method | 可证伪方案与方法假设 | 提案和失败判据 |
| Experiment | baseline、实验协议与复现 | 运行记录和结果 |
| Reviewer | 主张、混杂因素与缺失对照 | 审查和修改意见 |

PI 是根 Codex 会话，另四个是原生子智能体；按任务需要启动，不要求全部同时运行。最终科研判断由人负责。

本次产品开发团队则为四个角色：leader、产品经理、两位工程师。这与用户使用的五角色科研 Lab 分开。

## 当前范围与验收

| 能力 | 产品行为 | 验收边界 |
|---|---|---|
| App 聊天初始化 | 根指令引导 Codex 从模板创建新 Lab | 不覆盖目标，包含隐藏配置，返回独立打开步骤 |
| 原生角色配置 | Lab 包含根 PI 指令和四份子智能体配置 | 独立打开、信任配置后使用；不声称同会话自动生效 |
| 科研启动 | Lab 新聊天读取 `research/kickoff.md` | PI 从 Scope 开始，按需要委派 |
| 共享材料 | 文献、提案、实验和审查落到文件 | 可检查交接，不等于主张已被证实 |
| 可选 Python CLI | `init/doctor/status/prompt/demo/gate/serve` | 需要 Python 3.11+，不是默认 App 路径前置条件 |
| 可选只读仪表盘 | 本地查看材料状态与 gate 结果 | 不执行智能体，不显示实时 agent 遥测 |
| 结构 gate | 检查必要材料和字段 | 不提供科学真实性或投稿标准认证 |
| 合成 Demo 与视觉 | 明确标注合成材料、概念图或实际界面 | 合成数据不能通过科研 gate，不冒充成果 |

独立本地控制 UI 属于未来方向；当前执行界面是 Codex App，现有本地仪表盘仅用于只读查看。真实 App 操作、原生角色执行和科研结果的验证应分别报告。

## 八周冲刺：目标示例

八周是可调整的研究管理目标。可以先比较三个候选方向，再选定一个主要问题。

| 周期 | 目标材料 | 人的判断 |
|---|---|---|
| 第 1—2 周 | 候选问题、文献地图、创新碰撞检查 | 哪个问题值得投入 |
| 第 3—4 周 | 方法草案、失败判据、小规模试验 | 假设是否站得住 |
| 第 5—6 周 | baseline、主要实验、消融与运行记录 | 对照与预算是否充分 |
| 第 7—8 周 | 审查意见、补充实验清单、证据支持的初稿 | 主张能否成立、是否继续或投稿 |

产出取决于方向与资源，不能将此目标写成顶会录用或论文数量承诺。

## 发布叙事

首屏：“已经有 Codex 套餐？用原生多智能体搭科研 Lab，无需另配 LLM API Key。”

下一句：“下载 ZIP，在 Codex App 中聊天创建 Lab；不用先安装 Python，也不用输入终端命令。”

操作说明：“先打开仓库创建，再将生成的 my-lab 独立打开并信任，在新聊天开始科研。”

第二层价值：“PI 带队，文献、方法、实验和 Reviewer 各自负责，证据与交接留在一个工作区。”

行动：“到 GitHub 下载 CodexLab，替换创建提示中的研究主题。”

## 发布检查

- README、START_HERE 和根指令中的两次打开流程一致。
- 不将 Python 或 CLI 安装写成 App 默认前置条件。
- 不把只读仪表盘或概念图写成智能体执行控制 UI。
- 区分文件生成验证、App 原生角色实际执行与科学结果验证。
- 保留套餐额度说明和图片/数据状态；不虚构成果、背书或用户规模。

实现参照 Codex 官方 [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)、[authentication](https://learn.chatgpt.com/docs/auth) 与 [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)。CodexLab 是独立项目。
