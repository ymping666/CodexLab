# 小红书发布包

仓库：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)。三版正文默认走 Skill 安装与当前项目调用，CLI 仅作进阶工具。

## 版本一：已有套餐

**标题：有 Codex 套餐，装个 Skill 做科研**

想用多智能体做科研，但不想为了搭框架，再开一套模型 API。

很多常见的 API 驱动框架，上手先要准备 Key、配置供应商、算额外调用费用，再接 SDK 和调度。

可我已经在用 Codex，它自己就有原生多智能体。

所以我们做了 CodexLab：
A Multi-Agent Research Lab for Codex。

直接在 Codex 聊天里装一个 Skill。下一条消息输入 $codexlab 和研究方向，在当前项目继续工作。

不用下载 ZIP、切换工作区、先装 Python，也不用你输入终端命令。框架无需额外 LLM API Key，正常消耗你已有合适套餐的 Codex 额度。

安装时发这句：

$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab

安装完成后，下一条消息：

$codexlab 研究方向：长程 AI 智能体的可靠评测。

如果没识别到 Skill，刷新列表或按客户端提示重新加载后再试。

当前会话当 PI，按需要把文献、方法、实验和 Reviewer 职责交给原生 worker。输出留在当前项目的 codexlab-runs/。

Skill 不会自动注册四个 TOML agent_types，而是把角色要求传入任务。没有原生 spawn 工具时会明确标记串行回退，不能当成原生并行执行。

目前 Alpha，配图是概念展示或合成数据的材料界面截图。真实原生执行和科学结论都要实际验证；无需额外 API Key，也不代表无限免费调用。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

#Codex #CodexLab #多智能体 #AI科研 #开源项目 #Skill

## 版本二：API 门槛

**标题：搭多 Agent，先别急着另开 API**

想试多智能体，却在教程第一步就卡住了：

API Key 去哪开？
额外模型调用怎么计费？
为什么还要接一套调度框架？

如果你已经有 Codex，我们想提供一条更直接的路径。

CodexLab：一个用 Codex 原生能力做科研的 Skill。

用官方 skill-installer 安装，下一条消息发：

$codexlab 研究方向：你的研究题目。

留在你正在用的项目里。PI 根据任务把文献、方法、实验和 Reviewer 的职责传给原生 worker，交接保存在 `codexlab-runs/<topic-slug>/`。

框架不用额外 LLM API Key，也不另外接模型 API 调度；使用已有合适套餐，额度正常消耗。默认不用下载仓库、换项目或先安装 Python。

先降低接入门槛，再组织科研分工。

你可以设一个八周目标：文献地图、可证伪方案、可复现实验包和证据支持的初稿。实际进展取决于题目与资源。

当前 Alpha。实际 child threads 需要观察和记录；没 spawn 工具时明确标记串行，不包装成原生并行。配图与 Demo 的概念/合成标记会保留。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

安装指令：
$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab

#Agent #多智能体 #Codex #AI研究 #开源 #研究生

## 版本三：当前项目里的 Lab

**标题：一个 Skill，让现有 Codex 做科研分工**

CodexLab 的出发点很简单：

你已经有 Codex 套餐。
Codex 已经有原生多智能体。
搭科研 Lab，能不能不用再接一套模型 API？

我们把入口做成一个 Skill。

先在 Codex 聊天安装：
$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab

安装完成后，在下一条消息输入：
$codexlab 研究方向：你想做的方向。

不需要先下载 ZIP 或切换 Lab 工作区。当前会话担任 PI，按需要给四个原生 worker 传入角色任务：文献、方法、实验、Reviewer。

指令、角色约定和模板一起装；不会自动注册四个自定义 TOML agent_types。输出写在当前项目的 codexlab-runs/。

人的重点是选方向、处理关键决策、核实结论。原生委派可用时查证实际子线程；不可用则标记串行回退，不假装有并行团队。

框架无需额外模型 API Key，已有合适套餐的 Codex 额度照常消耗。CLI、独立项目配置和只读仪表盘都是进阶可选路径，默认不用。

当前 Alpha，图片是标记清楚的概念展示或合成材料界面。完整科学成果仍需要真实数据、实验和审查。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

#CodexLab #Codex #原生多智能体 #AI科研 #开源日记 #Skill

## 配图说明

1. 封面：assets/codexlab-launch-poster.png，竖版五角色海报。
2. 第二张：assets/codexlab-concept-demo.png，横版概念图。
3. 可选第三张：assets/codexlab-dashboard-actual.jpg，另一项可选工具的实际只读材料仪表盘。

保留概念/合成标记。第三张配文：“进阶只读材料视图；合成 Demo 数据；不执行智能体，不显示实时 agent 状态”。

新的 Skill 安装、调用与原生子线程活动镜头按 marketing/demo-storyboard.md 待录制。现有图片不是 Skill 已安装、原生 worker 已执行或科研成果已验证的证明。
