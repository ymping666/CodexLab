# 小红书发布包

仓库：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)。以下三版正文均以 Codex App 为默认入口，不要求读者先装 Python 或输入终端命令。

## 版本一：已有套餐

**标题：有 Codex 套餐，直接搭个科研 Lab**

想用多智能体做科研，但不想为了搭框架，再开一套模型 API。

很多常见的 API 驱动框架，上手先要准备 Key、配置供应商、算额外调用费用，再接 SDK 和调度。

可我已经在用 Codex，而且它自己就有原生多智能体。

所以我们做了 CodexLab：
A Multi-Agent Research Lab for Codex。

直接使用已登录的 Codex App 和原生子智能体。框架不需要另配 LLM API Key，正常消耗你已有合适套餐的 Codex 额度。

入门流程也放在 App 里：

① GitHub 选择 Code → Download ZIP，下载解压
② 在 Codex App 打开仓库，聊天说出主题，让它创建 my-lab
③ 再把 my-lab 单独作为项目打开，审阅并信任配置
④ 在新聊天读取 research/kickoff.md，开始科研

不用你先安装 Python，也不用你输入终端命令。注意要打开两次：仓库负责创建，Lab 负责研究。

然后，五个角色各自工作：
🧭 PI 管方向
📚 Literature 查文献
🧪 Method 做方法
⚙️ Experiment 做实验
🔍 Reviewer 找问题

文献、方案、实验记录和审查意见保存在同一个工作区。

当前 Alpha，配图是概念展示或使用合成数据的实际界面截图。无需额外 API Key，不代表无限免费运行，套餐额度照常消耗。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

#Codex #CodexLab #多智能体 #AI科研 #开源项目 #科研工具

## 版本二：API 门槛

**标题：搭多 Agent，先别急着另开 API**

想试多智能体，却在教程第一步就卡住了：

API Key 去哪开？
额外模型调用怎么计费？
为什么还要接一套调度框架？

如果你已经有 Codex，我们想提供一条更直接的路径。

CodexLab：用 Codex 原生子智能体搭科研 Lab，框架无需另配 LLM API Key，执行用你的已有合适套餐额度。

默认入口就是 Codex App。

从 GitHub 下载 ZIP，解压后打开仓库，把研究主题发给 Codex，让它按模板创建 my-lab。

创建完，再把 my-lab 独立打开、审阅并信任配置，在新聊天读取 research/kickoff.md。先创建，再研究；打开仓库不会自动加载子目录的科研角色。

整个默认上手流程不用你安装 Python，也不用你输入终端命令。

Lab 只保留五个角色：PI、文献、方法、实验、Reviewer。先降低接入门槛，再把科研分工组织起来。

你可以设一个八周目标：文献地图、可证伪方案、可复现实验包和证据支持的初稿。实际进展取决于题目与资源。

目前 Alpha。运行正常消耗 Codex 额度，概念图和合成 Demo 已作标记。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

#Agent #多智能体 #Codex #AI研究 #开源 #研究生

## 版本三：App 里的原生 Lab

**标题：在 Codex App 里，建一个科研小组**

CodexLab 的出发点很简单：

你已经有 Codex 套餐。
Codex 已经有原生多智能体。
为了搭科研框架，能不能不用再接一套模型 API？

我们选择直接使用已登录的 Codex App。框架无需额外 LLM API Key，不另造模型 API 调度，正常消耗现有合适套餐的额度。

这次把上手也放进 App：

下载 ZIP → 打开仓库 → 聊天创建 my-lab →
将 my-lab 独立打开并信任 → 新聊天读取 kickoff 开始。

不用先装 Python，也不用输入终端命令。两次打开是必要的：第一步生成配置，第二步在 Lab 自己的项目中使用配置。

研究团队只有五个角色：
PI、Literature、Method、Experiment、Reviewer。

人的重点是选方向、处理关键决策、核实结论。子智能体负责有边界的任务，交接材料留在共享文件里。

CLI 和本地只读仪表盘是可选工具。仪表盘看材料，不执行 agent；独立控制 UI 还在未来计划里。

当前 Alpha，概念图与合成 Demo 都有标记。完整科研产出仍需要真实数据、实验和审查。

如果你也想把已有 Codex 用在 AI 科研上，欢迎下载试用和共建。

GitHub：[ymping666/CodexLab](https://github.com/ymping666/CodexLab)

#CodexLab #CodexApp #原生多智能体 #AI科研 #开源日记 #BuildInPublic

## 配图说明

1. 封面：assets/codexlab-launch-poster.png，竖版海报。
2. 第二张：assets/codexlab-concept-demo.png，横版五角色概念图。
3. 可选第三张：assets/codexlab-dashboard-actual.jpg，已实现的本地只读材料仪表盘截图。

保留概念/合成标记。实际仪表盘截图配文：“可选只读材料视图；合成 Demo 数据；不执行智能体，不显示实时 agent 状态”。

App 入门截图按 marketing/demo-storyboard.md 新录制，显示仓库创建和 Lab 独立打开两个步骤。现有素材不冒充已录制的 App 端到端运行证明。
