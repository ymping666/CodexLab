# 小红书发布包

仓库：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)。以下三版正文可直接发布，主线都是“已有 Codex 套餐，使用原生多智能体，无需另配模型 API Key”。

## 版本一：已有套餐

**标题：有 Codex 套餐，还想搭科研 Agent？**

我想做多智能体科研，但不想为了搭框架，再开一套模型 API。

很多常见框架的上手路径是：准备 API Key、配置模型供应商、算额外调用费用，再接 SDK 和调度逻辑。

可我已经在用 Codex 了。而且 Codex 自己就有原生多智能体。

所以我们做了 CodexLab：
A Multi-Agent Research Lab for Codex。

直接使用已登录的 Codex 和它的原生子智能体。框架本身不用另配 LLM API Key，也不用自己再接一套模型 API 调度。

已有支持 Codex 的套餐，就在自己的额度内使用。无需额外 API Key，不等于无限免费调用，正常消耗 Codex 额度。

在这个基础上，我们再搭一个精简科研 Lab：

🧭 PI 管方向与整合
📚 Literature 查文献与证据
🧪 Method 做方法与假设
⚙️ Experiment 做实验与复现
🔍 Reviewer 做审查与质疑

五个角色，共享文献、方案、实验记录和审查意见。从给一个研究方向开始，把分工落到文件里。

第一版已经有工作区初始化、角色配置、启动提示、阶段材料检查和本地只读仪表盘。当前 Alpha，配图是概念展示或使用合成数据的实际界面截图。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

#Codex #CodexLab #多智能体 #AI科研 #开源项目 #科研工具

## 版本二：API 门槛

**标题：想玩多 Agent，先别急着开 API**

多智能体很吸引人。
但很多人一看常见 API 框架的教程，就卡在了第一步：

API Key 去哪开？
模型调用怎么计费？
为什么还要搭一套调度？

如果你已经在用 Codex，我们想提供另一条上手路径。

CodexLab：基于 Codex 原生子智能体的科研 Lab。

继续用你已经登录的 Codex。框架不需要额外模型 API Key，也不另造一个 API 编排运行时。实际执行交给 Codex，使用你已有合适套餐的额度。

然后把科研工作组织成五个角色：
PI → 文献 → 方法 → 实验 → Reviewer。

PI 在根会话协调，其余四个是专门子智能体。每个角色都有交付材料：来源、假设、实验命令、结果和审查意见。

先降低接入门槛，再把科研流程组织起来。这就是项目的出发点。

你可以给它一个八周冲刺目标：文献地图、可证伪方案、可复现实验包和依据证据整理的初稿。具体能推进多远，取决于题目与实验资源。

当前是 Alpha。没有额外模型 API Key，仍会正常消耗 Codex 额度；概念图与 Demo 都有状态标记。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

#Agent #多智能体 #Codex #AI研究 #开源 #研究生

## 版本三：原生科研 Lab

**标题：把已有 Codex 套餐，变成科研 Lab**

我们开始做 CodexLab，最先确定的是运行方式：

用 Codex 自带的多智能体。
用用户已经登录的 Codex。
不要求为了这个框架，再开一个 LLM API Key。

很多 API 驱动框架需要额外模型调用计费和编排设置。CodexLab 把执行交给 Codex 原生 subagents，让已有合适套餐成为起点，额度按正常规则消耗。

第一版主要做这些：

① 一个命令创建科研工作区
② 生成 PI 和四个原生子智能体的职责配置
③ 输出可直接交给 Codex 的启动提示
④ 用共享文件承接文献、方法、实验与审查
⑤ 用 CLI 和本地仪表盘检查阶段材料

科研团队只保留五个角色：PI、Literature、Method、Experiment、Reviewer。人的主要工作是选方向、处理关键决策、核实结论。

项目仍在 Alpha。现在展示的是已实现的工作区工具，以及明确标记的概念图和合成 Demo；真实科学成果需要自己的数据、实验和审查。

如果你也已经有 Codex，想把原生多智能体用在 AI 科研上，欢迎一起试、一起改。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

#CodexLab #Codex #原生多智能体 #AI科研 #开源日记 #BuildInPublic

## 配图说明

1. 封面：assets/codexlab-launch-poster.png，竖版海报。
2. 第二张：assets/codexlab-concept-demo.png，横版五角色概念图。
3. 第三张：assets/codexlab-dashboard-actual.jpg，实际本地仪表盘截图。

保留概念/合成标记。实际截图配文：“实际本地材料仪表盘；合成 Demo 数据；非智能体实时状态”。后续真实终端截图按 marketing/demo-storyboard.md 捕获。
