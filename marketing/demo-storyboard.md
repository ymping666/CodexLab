# CodexLab Skill Demo 分镜

**首屏主张：** 已经有 Codex 套餐？装一个 Skill，在当前项目搭科研 Lab，无需另配 LLM API Key。

**默认入口：** Codex 聊天用官方 skill-installer 安装，安装完成后下一条消息调用 $codexlab。无需用户下载 ZIP、切换工作区、安装 Python 或输入终端命令。

仓库：[ymping666/CodexLab](https://github.com/ymping666/CodexLab) · [安装指南](../START_HERE.md) · [Skill 指令](../skills/codexlab/SKILL.md)。

## 六个镜头 · 约 60 秒成片

| 镜头 | 画面 | 讲稿 | 素材状态 |
|---|---|---|---|
| 1 · 0—8 秒 | 概念主图，字幕“已有 Codex，无需额外 LLM API Key” | “许多 API 框架要配 Key、算额外调用。CodexLab 使用已有合适套餐，在 Codex 里安装一个 Skill。” | 概念图 / 合成示例 |
| 2 · 8—18 秒 | 当前项目的 Codex 聊天发送安装请求，等待真实安装结果 | “用官方 skill-installer 安装这个仓库的 Skill。安装成功后，再发下一条消息。” | 安装操作待录制；不伪造成功输出 |
| 3 · 18—28 秒 | 下一条消息 $codexlab + 研究方向 | “告诉它研究方向，直接在当前项目开始，不用下载 ZIP、换工作区或先安装 Python。” | Skill 发现与调用待录制 |
| 4 · 28—42 秒 | 实际 native worker 委派与子线程活动 | “当前会话是 PI，将文献、方法、实验与审查职责传入原生 worker 任务。” | 实际子线程活动待验证、待录制 |
| 5 · 42—53 秒 | 当前项目 `codexlab-runs/<topic-slug>/` 的真实文件 | “交接留在文件里。哪些来源已核实，哪些实验真跑过，都要查证。” | 材料生成待录制，状态按实际证据标记 |
| 6 · 53—60 秒 | 安装指令、仓库链接与五角色概念图 | “一个 Skill，使用已有 Codex 的原生能力。额度正常消耗，把研究方向换成你的题目。” | 仓库入口 / Alpha / 概念图 |

若实际客户端没有 spawn/委派工具，第四镜头必须改成“串行回退”，画面和讲稿明确说明这不是原生并行执行。不能用根会话写出的四段角色文字冒充四个 child threads。

## 可复制的演示步骤

在当前项目的 Codex 聊天发送：

```text
$skill-installer https://github.com/ymping666/CodexLab/tree/main/skills/codexlab
```

记录真实安装结果。安装完成后，下一条消息：

```text
$codexlab 研究方向：长程 AI 智能体的可靠评测。
先从问题范围和已有工作开始，可用时使用原生子智能体，
将证据与交接保存在当前项目。
```

客户端未识别 Skill 时，按实际界面刷新 Skill 列表或重新加载/重启，再试调用；不把重启写成所有客户端必需步骤。

拍摄应保留三个可分辨的观察：安装是否成功、是否发生实际原生委派、运行目录中交付了什么材料。研究者最后核实证据，不把工具运行当成科学验证。

安装不会自动注册四个自定义 TOML agent_types。Skill 通过任务传入角色职责，不应剪成“安装后自定义 agent_types 已注册”的演示。

## 可选进阶镜头

独立项目 TOML 配置、Python CLI 和只读仪表盘放在主 Demo 之后，作为进阶路径，不作为默认安装/调用前置条件。

CLI 需要 Python 3.11+，可创建项目配置式 Lab；status/gate/serve 也能查看 Skill 运行目录。prompt 只适用于带 kickoff 文件的项目配置式 Lab。现有只读仪表盘显示材料与 gate 结果，不执行 agent。独立本地控制 UI 属于未来方向。

assets/codexlab-dashboard-actual.jpg 可以出现在补充镜头，必须注明“进阶只读材料视图 / 合成 Demo 数据 / 非实时智能体”。

## 现有素材

- assets/codexlab-concept-demo.png：横版概念主图，保留 CONCEPT DEMO / SYNTHETIC EXAMPLE。
- assets/codexlab-launch-poster.png：竖版五角色封面，保留概念标记。
- assets/codexlab-dashboard-actual.jpg：实际只读材料仪表盘截图，使用合成数据；不代替 Skill 或原生执行截图。
- assets/image-prompts.md、assets/poster-prompt.md：生成提示与素材状态记录。

新安装、调用、原生子线程和运行材料镜头全部待录制。现有素材不证明 Skill 已安装到用户本机、原生 worker 已执行或完整科研已完成。

## 文案顺序

先讲：“已有 Codex 套餐”“无需额外 LLM API Key”“聊天安装 Skill”。

再讲：“下一条消息 $codexlab”“当前项目”“原生角色任务”“codexlab-runs/”。

最后讲：“五角色分工”“可检查的证据”“正常消耗额度”。八周可以是示例研究目标，不是论文数量或顶会录用承诺。
