# 从 Codex App 开始

默认使用 Codex App 和已有账号权限。无需用户安装 Python、pip、CLI，或另配模型 API key。额度与工作区权限仍然适用。完整提示见 [START_HERE.md](../START_HERE.md)。

1. 下载 ZIP、解压，在 App 中打开仓库目录。
2. 在聊天中明确要求阅读根 `AGENTS.md`，从 `codexlab/templates/research` 为你的课题创建新的 `my-lab`。这一步只创建材料；目标已存在时停止，包括空文件夹。
3. Codex 完整复制模板，包含 `.codex`、四个角色、空证据和运行记录；替换项目名、课题占位符，创建 `.codexlab.json`，返回生成目录的绝对路径。
4. 把 **生成的 my-lab 作为独立 App 项目打开**，审阅配置并处理 App 信任提示。项目配置需要信任才加载；原聊天不能保证热加载新目录。见 [官方配置说明](https://learn.chatgpt.com/docs/config-file/config-advanced)。
5. 在 my-lab 开启新聊天，请 Codex 阅读 `AGENTS.md`、`research/brief.md` 和 `research/kickoff.md`，由 PI 明确请求四个原生角色开始科研。

PI 是主会话，literature、method、experiment、reviewer 是四个专门角色。官方文档支持 App 显示子智能体线程；角色发现和调用以实际客户端行为为准。见 [官方子智能体说明](https://learn.chatgpt.com/docs/agent-configuration/subagents)。登录使用 App 的账号流程；[官方认证说明](https://learn.chatgpt.com/docs/auth) 描述可用身份方式。

## 在 App 中检查材料

PI 先补全 `research/brief.md` 的问题、数据/模型/计算资源、预算、指标、证伪条件与边界，再按 `scope -> literature -> method -> experiment -> review` 推进，把决定写入 `research/decisions.md`。

没有 Python 时，在 App 中人工检查每阶段文件、未完成占位符、证据记录和原始产物，并明确记录“人工检查”、问题与依据。人工检查不能标注自动 gate PASS。自动结构检查同样不能证明科学正确、创新性或论文录用。

| 阶段 | 核心材料 |
| --- | --- |
| scope | `research/brief.md` |
| literature | `literature/prior-art.md`、`evidence/ledger.jsonl` |
| method | `method/proposal.md` |
| experiment | `experiments/plan.md`、`experiments/results.md`、`experiments/runs.jsonl` 与原始输出 |
| review | `review/report.md` |

文献记录要求 `title`、`url`、`checked_at`、`claim`，只能收录实际打开的来源。实验记录要求 `run_id`、实际执行的 `command`、`seed`、数值 `metrics`、指向已有原始文件的相对 `artifact_path`，并保留代码/数据身份、环境和偏离计划情况。负结果、零效果与失败日志都要保留；崩溃的运行不能靠编造指标通过检查。

独立 reviewer 检查原论文、代码与原始运行记录，在已有资源和预算内尝试复现。结论可以是修改、停止或交人类审阅。

## 资源管理器复制备选

App 文件权限阻止创建时，用资源管理器复制整个 `codexlab/templates/research` 到新目录并命名为 my-lab，确认 `.codex/config.toml` 和四个 `.codex/agents/*.toml` 存在。将副本作为独立 App 项目打开，用文件编辑或聊天替换全部 `{{PROJECT_NAME}}` 为目录名、`{{TOPIC}}` 为课题，保留 `TODO` 决策，然后阅读 kickoff。已有副本不能再次覆盖初始化。手动复制没有 `.codexlab.json`；如需可选 CLI，请 Codex 按根 AGENTS.md 的 schema 补齐，不能假定未补齐的副本兼容 CLI。

## 可选 Python CLI

已有 Python 3.11+ 的用户或开发者可从仓库根目录使用 CLI；这不是 App 路径的前置条件。以下初始化面向另一个**尚不存在**的目标：

```console
python -m codexlab doctor
python -m codexlab init cli-lab --topic "Efficient retrieval for scientific question answering"
python -m codexlab prompt cli-lab
python -m codexlab status cli-lab
python -m codexlab gate cli-lab scope
python -m codexlab serve cli-lab --port 8765
```

CLI 复制、检查和只读展示材料，不启动模型或取代原生子智能体。`gate WORKSPACE STAGE` 支持五个阶段；各阶段独立检查，PI 负责依赖顺序，没有 `advance` 命令。`doctor`、`status`、`gate` 支持 `--json`。`serve` 打印本地回环 URL，用 Ctrl+C 停止。需要从其他目录使用时，可自行将本地包安装到已有 Python 环境。

可选 `demo` 工作区包含标明虚构的材料，研究 gates 不允许其通过。[toy regression 示例](../examples/README.md) 实际计算离线合成数据指标，但也不验证原生模型执行或论文贡献。
