# CodexLab App 入门 Demo 分镜

**首屏主张：** 已经有 Codex 套餐，就用原生多智能体搭科研 Lab，无需另配 LLM API Key。

**默认入口：** Codex App。下载 ZIP，聊天创建工作区，再独立打开 Lab。无需用户先安装 Python 或输入终端命令。

仓库：[ymping666/CodexLab](https://github.com/ymping666/CodexLab) · 入口说明：[START_HERE.md](../START_HERE.md)。

## 六个镜头 · 约 60 秒

| 镜头 | 画面 | 讲稿 | 素材状态 |
|---|---|---|---|
| 1 · 0—8 秒 | 概念主图，字幕“已有 Codex，无需额外 LLM API Key” | “常见 API 框架要配 Key、算额外调用。CodexLab 从你已登录的 Codex App 开始，正常消耗已有合适套餐的额度。” | 概念图 / 合成示例 |
| 2 · 8—18 秒 | GitHub Code → Download ZIP，解压后在 App 打开仓库 | “下载解压，把仓库作为项目打开。默认流程不用先安装 Python，也不用你输入终端命令。” | App 和浏览器操作，待录制 |
| 3 · 18—31 秒 | 仓库新聊天粘贴创建提示，检查 my-lab 目录 | “告诉 Codex 研究主题，它按模板创建 my-lab，生成角色配置和科研材料。这一步只创建，不开始研究。” | App 操作与生成文件，待录制 |
| 4 · 31—44 秒 | 将 my-lab 独立打开，审阅/信任配置，新聊天读取 kickoff | “再把 my-lab 单独打开并信任，在新聊天读取 kickoff。打开仓库不会自动加载子目录角色。” | 第二次打开与新聊天，待录制 |
| 5 · 44—53 秒 | 概念图的五角色区与 Lab 科研材料 | “PI 带队，文献、方法、实验和 Reviewer 分工，交接留在文件里。真实结论仍要查证。” | 概念图；实际材料需录制后使用 |
| 6 · 53—60 秒 | GitHub 仓库和 START_HERE | “用已有 Codex 的原生能力，开始一个精简科研 Lab。下载项目，把创建提示里的主题换成你的方向。” | 仓库入口 / Alpha |

这条 Demo 必须呈现两次打开。不能把在仓库中创建文件的画面剪成“原生角色已在仓库会话生效”。角色调用只有在真实观察到执行后才能作为执行画面发布。

## 可复制的 App 演示步骤

1. 从 GitHub 下载 ZIP，解压。
2. 在 Codex App 打开解压后的仓库目录，新建聊天。
3. 粘贴中文或英文创建提示，将主题替换为演示方向。
4. 检查新生成的 my-lab：模板结构、隐藏 .codex、四份角色配置、research/kickoff.md 和工作区元数据应齐全；已有目录不得覆盖。
5. 记录 Codex 返回的 my-lab 绝对路径，再将此文件夹作为独立项目打开。
6. 审阅 AGENTS.md 和 .codex 配置，完成原生信任提示。
7. 在 Lab 的新聊天读取 research/kickoff.md，由 PI 从 Scope 开始。实际角色不可用时如实呈现配置问题。

创建和启动提示直接使用中英文 README 的可复制文本，避免另写一份不一致的操作路径。

## 可选工具的补充镜头

CLI 与只读本地仪表盘放在主 Demo 之后，面向需要材料检查的用户。它们需要 Python 3.11+，不作为 App 入门前置条件。

```bash
# 已安装可选 CLI 时，从仓库目录运行
python -m codexlab status ./my-lab
python -m codexlab gate ./my-lab literature

# 新的合成 Demo 目标必须不存在
python -m codexlab demo ./recording-demo
python -m codexlab serve ./recording-demo --port 8765
```

本地仪表盘只显示材料状态和 gate 结果，不执行 agent，也不显示实时 agent 遥测。独立本地控制 UI 是未来路线，不能用现有截图冒充已经交付。

合成 Demo 的科研 gate 返回失败是预期行为；文件结构检查不证明科学结论成立。

## 静态素材

- assets/codexlab-concept-demo.png：横版概念主图，保留 CONCEPT DEMO / SYNTHETIC EXAMPLE。
- assets/codexlab-launch-poster.png：竖版双语封面，保留概念标记。
- assets/codexlab-dashboard-actual.jpg：实际只读本地仪表盘截图，使用合成数据；仅用于可选工具补充镜头，不代替 App 执行截图。
- assets/image-prompts.md、assets/poster-prompt.md：生成提示与素材状态记录。

现有概念图和材料仪表盘截图不证明 App 端到端流程或真实科研已运行。App 操作需重新录制和核实。

## 文案顺序

先讲：“已有 Codex 套餐”“原生多智能体”“无需额外 LLM API Key”“正常消耗额度”。

再讲：“下载 ZIP”“App 聊天创建”“将 Lab 独立打开并信任”“新聊天读 kickoff”。

最后讲：“五个科研角色”“共享材料”“可选结构检查”。八周可以是示例研究目标，不是论文数量或顶会录用承诺。
