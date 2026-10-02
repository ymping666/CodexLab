# CodexLab 产品简报 · Alpha

## 定位与入口

**已经有 Codex 套餐？安装一个 Skill，在当前项目直接搭科研 Lab，无需另配 LLM API Key。**

英文定位：**A Multi-Agent Research Lab for Codex.**

第一层卖点：**Your Codex plan. Native subagents. No extra LLM API key.**

默认入口：**Codex 聊天安装 Skill → 下一条消息调用 $codexlab。** 用户留在当前项目，无需下载 ZIP、打开仓库、切换 Lab 工作区或安装 Python。

第二层价值：**一个 PI、四个专门 worker 角色，将文献、方法、实验与审查接起来。**

仓库：[ymping666/CodexLab](https://github.com/ymping666/CodexLab) · [安装指南](../START_HERE.md) · [Skill 指令](../skills/codexlab/SKILL.md)。

## 用户与问题

第一批用户已经购买了支持 Codex 的套餐、登录了 Codex，也想用多智能体做 AI 科研。许多 API 驱动框架要求另外配置模型 API Key、承担独立调用费用，并接入 SDK 或调度运行时。已有套餐与另搭 API 框架之间的接入门槛，是 CodexLab 先要解决的问题。

CodexLab 使用已登录的 Codex 和原生子智能体能力。Skill 包含指令、角色任务约定与材料模板，不调用模型 API，也不另造编排运行时。实际执行正常消耗用户合适套餐中的 Codex 额度，不等于无限免费运行。

| 用户问题 | 默认 Skill 路径 |
|---|---|
| 还要开模型 API 吗？ | 无需额外 LLM API Key |
| 要下载代码、装 Python 吗？ | 在 Codex 聊天用官方 skill-installer 安装 |
| 需要换一个项目吗？ | 在当前项目调用 $codexlab |
| 原生角色怎么工作？ | PI 把职责约定传入 native worker 的任务 |
| 结果放在哪里？ | 当前项目的 `codexlab-runs/<topic-slug>/` |
| 调用怎么消耗？ | 已有合适套餐的 Codex 额度，资格与限制照常适用 |

实验计算、数据和自行接入的外部服务仍由用户提供。

## 默认闭环：安装与调用

1. 在 Codex 聊天发送下方官方安装器请求。
2. 等待安装完成，在下一条消息调用 $codexlab 并说明研究方向。
3. 若客户端尚未发现 Skill，刷新 Skill 列表，或按客户端重新加载/重启提示重试；不要求所有客户端一律重启。
4. 当前会话担任 PI，建立当前项目中的研究运行目录。
5. 可用时，通过原生 spawn/委派工具向 worker 传入文献、方法、实验与 Reviewer 的职责任务。
6. 研究输出留在 `codexlab-runs/<topic-slug>/`，人处理关键决策、查证主张并决定继续或返工。

```text
$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab
```

下一条消息示例：

```text
$codexlab 研究方向：长程 AI 智能体的可靠评测。
先梳理问题范围和已有工作，可用时使用原生子智能体，
将证据和交接材料保存在当前项目。
```

安装说明不代表已替用户安装到本机；实际成功以该用户的 Codex 安装结果为准。

## 五个角色的执行边界

| 角色 | 职责 | 交接材料 |
|---|---|---|
| PI / Lab Lead | 方向、委派、综合与人的决策 | 研究简报和综合结论 |
| Literature | 来源核实、已有工作与创新碰撞 | 文献地图和证据记录 |
| Method | 可证伪方案与方法假设 | 提案和失败判据 |
| Experiment | baseline、实验协议与复现 | 运行记录和结果 |
| Reviewer | 主张、混杂因素与缺失对照 | 审查和修改意见 |

PI 是当前调用的根会话，其余四个是任务角色。安装 Skill 不自动注册四个自定义 TOML agent_types；职责通过任务传给可用的原生 worker。按研究依赖分批委派，不要求四个角色全部同时运行。

真实原生执行要能观察到实际子线程活动，不能把根会话自己完成的角色文本当作四个 native agents。若没有 spawn/委派工具，明确记录串行回退，这不是原生并行执行。最终科研判断由人负责。

本次产品开发由 leader、产品经理和两位工程师共同推进；这是开发分工，与用户的五角色研究 Lab 分开。

## 当前范围与验收

| 能力 | 产品行为 | 验收边界 |
|---|---|---|
| Skill 安装 | 官方安装器接收仓库 Skill 路径 | 用户安装结果与下一条消息发现情况分别确认 |
| 当前项目调用 | $codexlab 创建研究材料目录 | 不要求重新打开项目或自动注册 TOML 类型 |
| 原生委派 | 角色职责传入实际 native worker 任务 | 查证真实子线程；无工具则标记串行 |
| 共享材料 | 文献、方法、实验和审查保存在运行目录 | 可检查交接，不等于科学结论已验证 |
| 进阶项目配置 | 可选 CLI 创建独立 TOML 配置式 Lab | 与默认 Skill 模式分开，需要独立信任项目 |
| 可选结构检查 | status/gate/serve 支持 Skill 运行目录与项目配置式 Lab | 不提供科学真实性认证；prompt 仅用于带 kickoff 的项目配置路径 |
| 可选只读仪表盘 | 显示材料状态与 gate 结果 | 不执行智能体，不显示实时 agent 遥测 |
| 合成 Demo 与视觉 | 标记合成数据、概念图或实际材料界面 | 不冒充真实科研或原生执行证明 |

CLI 需要 Python 3.11+，是进阶可选工具，不是默认 Skill 路径的用户前置条件。独立本地控制 UI 属于未来方向。安装、原生执行和科学结果应分别验证。

## 八周冲刺：目标示例

可以先比较三个候选方向，再选定一个主要问题；八周是可调整的研究目标。

| 周期 | 目标材料 | 人的判断 |
|---|---|---|
| 第 1—2 周 | 候选问题、文献地图、创新碰撞检查 | 哪个问题值得投入 |
| 第 3—4 周 | 方法草案、失败判据、小规模试验 | 假设是否站得住 |
| 第 5—6 周 | baseline、主要实验、消融与运行记录 | 对照与预算是否充分 |
| 第 7—8 周 | 审查意见、补充实验清单、证据支持的初稿 | 主张能否成立、是否继续或投稿 |

产出取决于方向与资源，不承诺论文数量或顶会录用。

## 发布叙事

首屏：“已经有 Codex 套餐？安装一个 Skill，在当前项目搭科研 Lab，无需另配 LLM API Key。”

操作：“用官方 skill-installer 安装，下一条消息输入 $codexlab 和研究方向。”

第二层：“PI 带队，四个原生 worker 按任务职责推进文献、方法、实验与审查，材料留在 codexlab-runs/。”

边界：“现有额度正常消耗；真实原生子线程要有实际记录，没有 spawn 工具则清楚标记串行回退。”

行动：“复制仓库安装指令，安装完成后把研究方向换成你的题目。”

## 发布检查

- README、START_HERE 与 Skill 指令的安装/调用路径一致。
- 不把 ZIP、工作区切换或 Python 写成默认前置条件。
- 不宣称安装 Skill 会注册四个自定义 TOML agent_types。
- 区分真实子线程、串行回退与科学结果验证。
- 只读仪表盘和概念图不冒充 agent 控制 UI 或执行证明。

依据：[官方 Skill 安装器](https://github.com/openai/skills/tree/main/skills/.system/skill-installer)、Codex [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) 与 [authentication](https://learn.chatgpt.com/docs/auth)。CodexLab 是独立项目。
