# CodexLab

**A Multi-Agent Research Lab for Codex.**

**已经有 Codex 套餐？用原生多智能体搭一个科研 Lab，无需另配 LLM API Key。**

许多 API 驱动的多智能体框架，第一步就是配置模型 API、承担额外调用费用，再接 SDK 和调度运行时。CodexLab 直接用你已经登录的 Codex，让原生子智能体承担执行；框架本身无需额外模型 API Key，也无需再接一套模型 API 调度系统。

使用你已有、支持 Codex 的套餐，正常消耗该套餐额度。接下来才是科研分工：PI、文献、方法、实验、Reviewer，五个角色组成一个精简研究小组。

[GitHub 仓库](https://github.com/ymping666/CodexLab) · [English](README.md) · [产品说明](marketing/product-brief.md) · [Demo 分镜](marketing/demo-storyboard.md) · [路线图](ROADMAP.md)

![CodexLab 科研工作区概念图，使用合成示例](assets/codexlab-concept-demo.png)

*Alpha · 上图为概念展示，使用合成示例。也可查看 [实际本地仪表盘截图](assets/codexlab-dashboard-actual.jpg)：展示合成材料状态，不代表智能体实时运行。*

## 用你已经拥有的 Codex 运行多智能体

| 起点 | 许多 API 驱动框架 | CodexLab |
|---|---|---|
| 模型访问 | 配置模型 API Key 与供应商 | 使用已登录的 Codex |
| 模型调用计费 | 单独计算模型 API 调用费用 | 消耗已有合适套餐的 Codex 额度 |
| 智能体执行 | 接入 SDK 或搭建调度运行时 | 使用 Codex 原生子智能体 |
| 科研准备 | 自己组织角色和交接 | 生成五角色 Lab 与共享科研材料 |

Python CLI 负责创建工作区、检查材料，**真正运行智能体的是 Codex 自身**。无需额外模型 API Key，不代表无限免费运行；实际使用受套餐资格和额度约束。实验计算、数据和自行接入的外部服务仍使用你自己的资源。

## 五个角色，职责清楚

| 角色 | 负责什么 | 交付什么 |
|---|---|---|
| **PI / Lab Lead** | 确定方向、分配任务、整合争议、请求人的决策 | 研究简报与综合结论 |
| **Literature Scientist** | 查证来源、梳理已有工作、排查创新碰撞 | 文献地图与证据账本 |
| **Method Scientist** | 把研究空白变成可证伪的方法 | 方法方案与失败判据 |
| **Experiment Scientist** | 设计 baseline、实现实验、记录可复现运行 | 实验协议、命令与结果 |
| **Reviewer** | 挑战主张、混杂因素与缺失对照 | 批判审查与修改意见 |

PI 是根 Codex 会话，其余四个角色是配置的子智能体。五个角色是精简工作阵容，不要求每次全部同时启动；研究方向与最终结论由人负责。

## 启动你的实验室

需要 Python 3.11 或更高版本、本地 Codex CLI 及原生子智能体支持，以及可用的 Codex 登录。具体版本能力和套餐资格请以当前官方文档为准。

```bash
git clone https://github.com/ymping666/CodexLab.git
cd CodexLab

# Python 3.11+
python -m pip install -e .
python -m codexlab doctor

# 目标目录必须尚不存在
python -m codexlab init ./my-lab --topic "长程 AI 智能体的可靠评测"
python -m codexlab prompt ./my-lab

# 在科研工作区中打开 Codex
cd my-lab
codex
```

在 Codex 中打开生成的子工作区，先查看其 `AGENTS.md` 与 `.codex` 配置，并完成 Codex 对已审阅配置的原生信任提示；未信任工作区的项目配置可能被忽略。把 `prompt` 输出的启动提示粘贴到会话中。PI 将读取工作区、按职责委派原生子智能体，并在约定的决策点请求你的判断。如果本地 Codex 版本需要显式开启子智能体，请按该版本的官方说明配置。

```bash
# 回到仓库目录，查看工作区与阶段材料
python -m codexlab status ./my-lab
python -m codexlab gate ./my-lab literature

# 创建明确标注的合成示例
python -m codexlab demo ./demo-lab
python -m codexlab status ./demo-lab

# 打开实际实现的只读本地仪表盘
python -m codexlab serve ./demo-lab --port 8765
```

`init`、`demo` 不会覆盖已有目标目录。`doctor` 检查本地前置条件，不证明当前会话已认证或所有原生智能体实际运行成功。使用 `python -m codexlab --help` 查看完整命令。

## 科研交接，有材料可查

| 阶段 | 要检查的材料 |
|---|---|
| Scope | 问题、边界与成功/失败判据 |
| Literature | 文献报告与有来源的证据记录 |
| Method | 具体方法与可证伪假设 |
| Experiment | baseline、协议、结果和运行记录 |
| Review | 审查报告与未解决的反对意见 |

这些 gate 检查必要材料与文件结构。研究者负责查证科学主张，决定证据能支撑什么结论。合成 Demo 无法通过科研 gate。

一个可以尝试的**八周科研冲刺目标**：完成文献地图、可证伪方案、可复现实验包，以及依据实际证据组织的论文初稿。具体产出取决于方向、数据与计算资源，不承诺论文录用。

## 当前交付

- 无第三方运行依赖的 Python CLI：初始化、环境检查、状态、启动提示、合成 Demo 与结构检查。
- 本地 Codex 项目配置和四份专门子智能体指令，PI 在根会话协调。
- 共享科研材料和审查交接机制，方便人检查与修改。
- `http://127.0.0.1:8765` 的只读本地仪表盘，显示工作区状态与结构检查结果；外观与宣传概念图不同。
- 概念 Demo 图、发布文案和中英文说明。
- 一张竖版 [发布海报](assets/codexlab-launch-poster.png) 与三版 [小红书文案](marketing/xiaohongshu.md)。

当前 Alpha 交付工作区初始化、原生角色配置、材料检查和本地仪表盘。完整科研产出与顶会录用尚未验证。下一步计划见 [路线图](ROADMAP.md) 和 [开发说明](DEVELOPMENT.md)。

## 一起建设

欢迎围绕一个具体问题贡献：引用查证、实验复现、审稿反馈或角色交接。请提供可复现的小例子，并明确区分真实观察与合成测试数据。代码采用 [MIT 协议](LICENSE)。

实现参照 Codex 官方的 [子智能体配置](https://learn.chatgpt.com/docs/agent-configuration/subagents)、[认证](https://learn.chatgpt.com/docs/auth)、[非交互模式](https://learn.chatgpt.com/docs/non-interactive-mode) 和 [配置参考](https://learn.chatgpt.com/docs/config-file/config-reference)。CodexLab 是独立项目，不是 OpenAI 官方产品。
