# CodexLab

**A Multi-Agent Research Lab for Codex.**

**已经有 Codex 套餐？用原生多智能体搭科研 Lab，无需另配 LLM API Key。**

许多 API 驱动的多智能体框架，需要额外配置模型 API、承担独立调用费用，再接 SDK 和调度运行时。CodexLab 从你已经登录的 **Codex App** 出发：下载项目，用聊天创建 Lab，再到独立工作区开始科研。

使用你已有、支持 Codex 的套餐，正常消耗该套餐额度。默认上手流程**不用你安装 Python，也不用你输入终端命令**。

[GitHub 仓库](https://github.com/ymping666/CodexLab) · [English](README.md) · [开始使用](START_HERE.md) · [产品说明](marketing/product-brief.md) · [路线图](ROADMAP.md)

![CodexLab 科研工作区概念图，使用合成示例](assets/codexlab-concept-demo.png)

*Alpha · 上图为概念展示，使用合成示例。[实际本地仪表盘截图](assets/codexlab-dashboard-actual.jpg) 展示的是合成材料状态，不代表智能体实时运行。*

## 直接在 Codex App 中开始

需要已登录的 Codex App，以及原生子智能体支持。版本能力与套餐资格请以当前官方文档为准。

1. 打开 [GitHub 仓库](https://github.com/ymping666/CodexLab)，选择 **Code → Download ZIP**，下载并解压。
2. 在 Codex App 中把解压后的**仓库目录**作为项目打开，新建聊天，粘贴下方创建提示并替换研究主题。
3. Codex 按模板创建一个新 `my-lab` 目录。该目录若已存在，应换一个名字，不覆盖原有内容。
4. 再将生成的 **`my-lab` 文件夹作为独立项目打开**。查看其中的 `AGENTS.md` 和 `.codex` 配置，完成 Codex 对已审阅配置的原生信任提示。
5. 在 **Lab 项目中的新聊天**粘贴下方科研启动提示。

这里有**两次打开**：先打开仓库完成初始化，再打开 `my-lab` 开始研究。打开仓库不会自动加载子目录 Lab 的角色配置；未信任的工作区配置也可能被忽略。

**创建提示——粘贴到仓库项目的聊天中：**

```text
先阅读 START_HERE.md 和仓库根目录的 AGENTS.md。
使用本仓库的科研模板，为研究主题“[替换为你的研究主题]”
创建一个新的 ./my-lab 工作区。

用 Codex 的文件工具完成，不要求我安装 Python 或输入终端命令。
不要覆盖已有目录。生成完整 Lab 配置、四份原生子智能体角色文件、
科研材料和 research/kickoff.md。

检查生成配置与相对角色路径是否一致。
这次仓库会话只负责创建工作区，不开始科研。
最后告诉我 my-lab 的绝对路径，提醒我将它作为独立项目
在 Codex App 中打开、审阅并信任配置，再在新聊天中开始。
```

**科研启动提示——粘贴到单独打开的 `my-lab` 项目新聊天中：**

```text
阅读当前工作区的 AGENTS.md 和 research/kickoff.md，
按 kickoff 的指引担任 PI / Lab Lead，从 Scope 阶段开始。
需要时将明确任务委派给已配置的原生子智能体，
在流程规定的决策点请求我的判断。
把证据与交接材料保存在这个工作区。
如果原生角色不可用，先说明配置问题。
```

## 用已有 Codex，组织五个科研角色

| 起点 | 许多 API 驱动框架 | CodexLab |
|---|---|---|
| 模型访问 | 配置模型 API Key 与供应商 | 使用已登录的 Codex App |
| 模型调用计费 | 单独计算模型 API 调用费用 | 消耗已有合适套餐的 Codex 额度 |
| 智能体执行 | 接入 SDK 或搭建调度运行时 | 使用 Codex 原生子智能体 |
| 科研准备 | 自己组织角色和交接 | 在聊天中按模板创建五角色 Lab |

**运行智能体的是 Codex 自身。** CodexLab 提供项目指令、原生角色配置和共享科研材料。无需额外模型 API Key，不代表无限免费运行；实际使用受套餐资格与额度约束。实验计算、数据和自行接入的外部服务仍使用你自己的资源。

| 角色 | 负责什么 | 交付什么 |
|---|---|---|
| **PI / Lab Lead** | 确定方向、分配任务、整合争议 | 研究简报与综合结论 |
| **Literature Scientist** | 查证来源、梳理已有工作、排查创新碰撞 | 文献地图与证据账本 |
| **Method Scientist** | 将研究空白变成可证伪方法 | 方法方案与失败判据 |
| **Experiment Scientist** | 设计 baseline、记录可复现实验 | 实验协议、命令与结果 |
| **Reviewer** | 挑战主张、混杂因素与缺失对照 | 审查报告与修改意见 |

PI 是根 Codex 会话，其余四个角色是原生子智能体。按当前任务调用需要的角色，不要求全部同时启动。研究方向与最终判断由人负责。

## 科研交接，有材料可查

| 阶段 | 要检查的材料 |
|---|---|
| Scope | 问题、边界与成功/失败判据 |
| Literature | 文献报告与有来源的证据记录 |
| Method | 具体方法与可证伪假设 |
| Experiment | baseline、协议、结果和运行记录 |
| Review | 审查报告与未解决的反对意见 |

研究文件让交接有据可查。可选结构 gate 检查必要材料，研究者负责查证科学主张。合成 Demo 无法通过科研 gate。

一个**八周科研冲刺目标**可以是文献地图、可证伪方案、可复现实验包和证据支持的初稿。可行性取决于研究范围与资源，不承诺论文录用。

## 可选 CLI 与材料仪表盘

想用命令行初始化工作区或做结构检查时，可以使用无第三方运行依赖的 CLI，需要 **Python 3.11+**。上述 App 入门流程不依赖它。

```bash
git clone https://github.com/ymping666/CodexLab.git
cd CodexLab
python -m pip install -e .
python -m codexlab doctor

# 另一种创建方式：目标目录必须尚不存在
python -m codexlab init ./my-lab --topic "长程 AI 智能体的可靠评测"
python -m codexlab prompt ./my-lab

# 查看材料与阶段要求
python -m codexlab status ./my-lab
python -m codexlab gate ./my-lab literature

# 在只读本地仪表盘中查看合成示例
python -m codexlab demo ./demo-lab
python -m codexlab serve ./demo-lab --port 8765
```

用 CLI 创建后，同样要在 Codex App 中将 `my-lab` 独立打开、审阅并信任配置，再开新科研聊天。`init`、`demo` 拒绝覆盖已有目标。`doctor` 检查 Python 和本地 Codex 可执行文件，不验证 App 登录或实际智能体执行。完整命令见 `python -m codexlab --help`。

`http://127.0.0.1:8765` 仪表盘显示材料状态和 gate 结果，**只读，不执行智能体**。独立的本地控制 UI 是后续方向，目前未交付。

## Alpha 交付

- 以 Codex App 为主入口的说明与仓库级聊天初始化流程。
- 包含根会话 PI 和四个原生子智能体配置的科研工作区。
- 共享证据、方法方案、实验记录与审查交接材料。
- 可选 Python CLI、合成 Demo、结构检查和只读本地仪表盘。
- [发布海报](assets/codexlab-launch-poster.png)、[三版小红书文案](marketing/xiaohongshu.md) 与 [Demo 分镜](marketing/demo-storyboard.md)。

完整科研产出与顶会录用尚未验证。实际检查见 [开发说明](DEVELOPMENT.md)，后续计划见 [路线图](ROADMAP.md)。

欢迎贡献引用查证、实验复现、Reviewer 反馈或角色交接方面的改进，并提供可复现的小例子，区分真实观察与合成数据。代码采用 [MIT 协议](LICENSE)。

实现参照 Codex 官方 [子智能体](https://learn.chatgpt.com/docs/agent-configuration/subagents)、[认证](https://learn.chatgpt.com/docs/auth) 与 [配置参考](https://learn.chatgpt.com/docs/config-file/config-reference)。CodexLab 是独立项目，不是 OpenAI 官方产品。
