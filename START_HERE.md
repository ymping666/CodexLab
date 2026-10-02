# 在 Codex App 里启动 CodexLab

下载 ZIP、解压，在 Codex App 中打开解压后的仓库文件夹，用已有的、具备 Codex 权限的账号登录。默认入口是 App 对话，无需先安装 Python、pip、CLI，也无需另配模型 API key。账号额度与工作区权限照常生效。

在仓库项目的新聊天中发送下面这段话，把课题替换成你的方向：

```text
阅读 START_HERE.md 和仓库根 AGENTS.md。
请从 codexlab/templates/research 完整创建新的 my-lab 研究工作区。
我的课题是：提高科学问答中检索证据的使用效率。
包含隐藏的 .codex、所有角色文件和 .codexlab.json 工作区记录，
替换项目名与课题占位符。如果 my-lab 已存在，请停止，不覆盖。
这一步只创建工作区，不在仓库根目录开始科研。
完成后给我生成目录的绝对路径，并说明如何在 App 中打开它。
```

创建工作区是复制文件，不等于已经启动科研团队。接着把返回的 **my-lab 目录作为独立 App 项目打开**。审阅生成的 `.codex/config.toml` 与角色文件，按 App 的项目信任提示处理。项目配置需要信任才能加载；不能假定原聊天即时加载另一个目录的配置。见 [OpenAI 项目配置说明](https://learn.chatgpt.com/docs/config-file/config-advanced)。

在 my-lab 中开启新聊天，发送：

```text
阅读 AGENTS.md、research/brief.md 和 research/kickoff.md。
按 kickoff 启动 CodexLab：你担任 PI，明确调用 literature、method、
experiment、reviewer 四个原生角色，先完善范围、资源和预算。
没有 Python 时人工检查材料并记录，不要声称自动 gate 通过。
```

PI 再组织文献、方法、实验与独立审查。官方文档支持 App 请求子智能体并查看子线程，具体客户端与账号仍需实际验证。见 [OpenAI 子智能体说明](https://learn.chatgpt.com/docs/agent-configuration/subagents)。

如果文件权限阻止自动创建，用资源管理器复制 **codexlab/templates/research 整个文件夹**，将副本命名为 my-lab，确保 `.codex` 也被复制。把副本作为独立 App 项目打开，用 App 文件编辑或请 Codex 替换全部 `{{PROJECT_NAME}}` 为 my-lab、`{{TOPIC}}` 为你的课题，保留 `TODO`。手动复制不会自动生成 `.codexlab.json`；如需可选 CLI，请 Codex 按根 AGENTS.md 的 schema 补齐记录，不能声称未经补齐就兼容 CLI。不要重新覆盖初始化这个已有副本。

详细材料与可选工具见 [快速开始](docs/quickstart.md)，验证范围见 [兼容性说明](docs/codex-compatibility.md)。

## English quick start

1. Download and extract the ZIP, then open the repository folder in the Codex App with your eligible existing sign-in. Python, pip, CLI and a separate model API key are not prerequisites.
2. Send the creation prompt below, replacing the topic. Wait for the absolute path of the new workspace; an existing target is refused, even if empty.
3. Open that generated directory as a **separate App project**, inspect its `.codex` files and project trust controls, and start a **new chat** with the launch prompt. Do not assume the original chat reloads another folder's roles.

Creation prompt:

```text
Read START_HERE.md and repository AGENTS.md. Create a new my-lab research
workspace from codexlab/templates/research for this topic: efficient scientific
question answering. Copy all files including .codex, replace project/topic tokens,
and create .codexlab.json. Refuse an existing destination. Only create the files;
do not begin research in the repository. Return the absolute generated path.
```

Launch prompt in the generated project's new chat:

```text
Read AGENTS.md, research/brief.md, and research/kickoff.md. Act as PI and
explicitly use literature, method, experiment, and reviewer. Start with scope
and resource budgets. If Python is unavailable, inspect and record materials
manually; do not claim an automated gate pass. Report unsupported role behavior.
```

If file permissions block copying, use File Explorer to copy the whole template folder, including `.codex`, to a new my-lab. In the copied project, use App editing/chat to replace all project/topic tokens and preserve unresolved `TODO` decisions. Ask Codex to add the manifest described in repository AGENTS.md before using optional CLI tools; raw manual copies have no manifest. Account-specific live agent execution remains to be confirmed; see [compatibility and verification](docs/codex-compatibility.md).
