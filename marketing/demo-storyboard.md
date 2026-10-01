# CodexLab Demo 分镜与讲稿

**展示目标：** 前 15 秒讲清“已有 Codex 套餐 + 原生多智能体 + 无需另配模型 API Key”，然后展示五角色科研分工与共享材料。

**首屏主张：** 已经有 Codex 套餐，就用它搭科研 Lab。框架无需额外 LLM API Key，正常消耗已有合适套餐的 Codex 额度。

**仓库：** [ymping666/CodexLab](https://github.com/ymping666/CodexLab)。

**素材状态：** 概念图不是运行截图；`demo` 产生合成材料。真实 CLI 截图须从实际运行捕获，保留终端输出，不虚构结果。

## 六个镜头 · 约 60 秒

| 镜头 | 画面 | 讲稿 | 状态标记 |
|---|---|---|---|
| 1 · 0—8 秒 | 首图 + 字幕“已有 Codex，无需额外模型 API Key” | “想搭科研多智能体，却卡在 API Key 和额外调用计费？如果你已有 Codex 套餐，可以从 CodexLab 开始。” | 概念 Demo / 合成示例 |
| 2 · 8—16 秒 | 实际终端的配置与 `prompt` 输出 | “直接使用已登录的 Codex 和原生子智能体，框架无需再配 LLM API Key，额度按套餐正常消耗。” | 实际文件与 CLI，拍摄后确认 |
| 3 · 16—27 秒 | 实际 `init` 输出 + 概念图五角色区 | “创建工作区，PI 带队，文献、方法、实验和 Reviewer 各自负责。” | 实际 CLI + 概念图 |
| 4 · 27—38 秒 | `assets/codexlab-dashboard-actual.jpg` 与 `status` 输出 | “角色交接留在同一个工作区，本地仪表盘查看材料状态。这里展示的是合成 Demo 数据。” | 实际界面 / 合成数据 / 非实时智能体 |
| 5 · 38—49 秒 | 实际 `gate ./recording-demo literature` 输出 | “阶段检查帮助找到缺失材料，真实结论由研究者查证。合成例子不能通过科研 gate。” | 实际 CLI + 合成示例 |
| 6 · 49—60 秒 | 仓库 README 和 GitHub 链接 | “用已有 Codex 的原生能力，开始一个五角色科研 Lab。到 GitHub 克隆 CodexLab，把你的研究方向放进去。” | Alpha / 仓库入口 |

## 可复制的 CLI 拍摄脚本

需要 Python 3.11+ 与已登录的 Codex。先克隆仓库；拍摄目标目录必须不存在。

```bash
git clone https://github.com/ymping666/CodexLab.git
cd CodexLab
python -m pip install -e .
python -m codexlab doctor
python -m codexlab init ./recording-lab --topic "Reliable evaluation of long-horizon AI agents"
python -m codexlab prompt ./recording-lab
python -m codexlab status ./recording-lab
python -m codexlab demo ./recording-demo
python -m codexlab status ./recording-demo
python -m codexlab gate ./recording-demo literature
```

最后一个 gate 对合成 Demo 返回失败是预期行为。要展示原生执行，请另在 `recording-lab` 中启动 Codex，审阅 `AGENTS.md` 与 `.codex` 配置、完成原生信任提示，再粘贴 `prompt` 输出。拍摄脚本本身只验证工作区工具，不证明真实智能体已执行。

## 静态素材交付

- `assets/codexlab-concept-demo.png`：主视觉，README 与发布封面使用。
- `assets/codexlab-launch-poster.png`：竖版中英双语封面，小红书优先使用。
- `assets/codexlab-dashboard-actual.jpg`：实际本地材料仪表盘截图，展示合成 Demo 数据；不是概念图，也不表示智能体实时运行状态。可用于第四镜头展示材料与阶段状态。
- `assets/image-prompts.md`：完整生成提示和素材状态，便于追踪与复现创作意图。
- `assets/poster-prompt.md`：竖版海报生成提示、尺寸与验收记录。
- 本分镜：后续实际终端截图与短视频录制依据。

## 展示中的措辞

首先使用：“已有 Codex 套餐”“原生多智能体”“无需另配 LLM API Key”“正常消耗套餐额度”。然后展开：“五角色科研 Lab”“共享材料”“结构检查”“合成示例”。

没有实证前不写：“自动顶会”“已发表 N 篇”“免费无限使用”“一键保证投稿成功”“真实性已验证”“完整在线仪表盘”。
