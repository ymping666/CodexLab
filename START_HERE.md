# 安装一次，在当前项目调用 CodexLab

默认入口是可安装的 Codex Skill。无需先下载整个仓库、创建另一份项目再切换目录，也无需用户先安装 Python。使用已有、具备 Codex 权限的账号；模型使用照常消耗账号额度，无需另配 LLM API Key。

## 1. 在 Codex 聊天中安装

```text
$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab
```

这是 Codex 的 Skill 指令，不是终端命令。官方安装器支持从其他 GitHub 仓库安装 Skill。安装完成后，在下一条消息中尝试调用；若没有出现，查看客户端的 Skill 列表，按客户端提示刷新或重启。见 [官方 Skill 使用与安装说明](https://learn.chatgpt.com/docs/build-skills)。

## 2. 在你的研究项目里调用

```text
$codexlab 研究方向：长程 AI 智能体的可靠评测。
先检查可用数据、工具和预算，再开始文献与方法工作。
```

当前 Codex 会话担任 PI，根据需要委派文献、方法、实验、独立审查四个原生子智能体。默认将材料保存到当前项目的 `codexlab-runs/<topic-slug>/`，也可以指定输出目录。初始化材料不会注册新的自定义 agent 类型，也不修改项目或全局 `.codex` 配置。

如果只想建立材料目录、暂不研究，直接说明：

```text
$codexlab 为“科学问答中的证据可靠性”初始化材料。
输出到 codexlab-runs/evidence-reliability，只创建目录，不开始研究。
```

继续已有工作时指定原目录：

```text
$codexlab 继续 codexlab-runs/evidence-reliability。
读取已有简报、证据和决策，从尚未完成的阶段继续，不重建材料。
```

## Skill 带来了什么

安装包包含 PI 工作流、四个角色的任务指令、证据协议与研究材料模板。无需再打开源代码仓库。角色通过原生子智能体任务接收指令；并发数量、工具和权限继承当前会话。没有原生子智能体工具时，必须明确报告能力限制，不能把串行角色分析称为并行执行。

用户不需要手动运行命令。若已有 Python，Codex 可调用包内的可选初始化脚本；否则按同样契约使用文件工具创建材料。已有目标目录不能被初始化覆盖。科学实验若需要额外运行环境，仍应在 Scope 阶段说明资源需求。

可选 CLI、结构检查与只读仪表盘见 [快速开始](docs/quickstart.md)。需要独立项目级自定义 TOML 角色时，也可使用原来的 CLI 模板；这是进阶路径，不是 Skill 的安装前置条件。验证范围见 [兼容性说明](docs/codex-compatibility.md)。

## English quick start

Install from Codex chat:

```text
$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab
```

On your next message, in your research project:

```text
$codexlab Study reliable evaluation of long-horizon AI agents.
Inspect resources and budget before starting literature and method work.
```

The current session is PI. Four research roles are delegated through native subagent task instructions, with artifacts under `codexlab-runs/<topic-slug>/` by default. Installing this Skill does not register custom agent types or modify Codex configuration. Existing account limits apply. Refresh the Skill list or restart the client if a newly installed Skill is not discovered. See [official Skills documentation](https://learn.chatgpt.com/docs/build-skills).
