# Role menu presentation

Use [roster.md](roster.md) and [catalog.json](catalog.json) for category/profile mapping, recommendations and scope. The optional [role-picker.html](../assets/ui/role-picker.html) is a self-contained HTML fragment with an embedded copy of the catalog, styles and JavaScript. It has no server, package, API key or repository dependency. Its first screen asks for one of four concrete uses; team review comes next, with per-responsibility adjustment. Five categories, fifteen profiles and five scenario presets remain available without showing all of them on the first screen.

## Select the presentation

1. If the user asks for text, use text. Otherwise use visual cards only when the current host exposes an inline HTML presentation capability and its documented rendering contract. Read the applicable available presentation skill/tool instructions before rendering. Do not infer support from the word “Codex”, a desktop client, or a browser tool alone.
2. On a capable host, copy the bundled fragment to a new, task-owned file in an explicitly writable durable preview directory, then present it using that host's documented content reference. Resolve the source relative to this installed Skill. Do not publish, start a server, modify Codex configuration or initialize a scientific run just to show the menu. Preview servers are only for explicitly requested local development/debugging.
3. Without that capability, or if rendering fails, show the text menu below immediately. Do not print unsupported rendering directives, install a visualization dependency, or require a browser/CLI to choose a team.

With no confirmed or saved choice, begin at “你现在想做什么？” with no use preselected. Choosing a catalog entry_points use updates only a candidate; “下一步：查看团队” opens a summary with Chinese responsibilities, names/styles and an adjustment action beside each row. The exploration entry configures Orion + Atlas + Nova without experiment or review; the idea entry configures Quinn + Flint + Mira + Rook without experiment. The other two entries cover experiment preparation and reproduction. These are configuration heuristics, not stage authorization or proven best teams. Avoid asking the user to memorize names.

The native responsibility select and profile buttons appear only after an adjustment action, with a clear return to the team. PI remains the current chat even when its profile is Orion or Quinn. A profile replaces only its category; five scenario presets under an optional section replace all slots. Turning off a specialist clears its selected-profile detail. Returning between views preserves choices. Confirmed configurations and compatible saved drafts enter the team review directly; clearly distinguish confirmed inputs from unconfirmed saved drafts. Never replace an existing team just because a novice opens the menu.

For confirmed choices, prepare a new task-owned copy and replace the `codexlab-picker-options` JSON script with `{"selection":{"pi":"Quinn","literature":"Atlas","method":"Mira","experiment":null,"reviewer":"Trace"},"ignoreSavedState":true}` using the actual confirmed slots. JSON-escape data; do not modify installed assets. Keep `codexlab-style-catalog` consistent with catalog.json. Saved drafts must not override later explicit choices.

File tools suffice for copying and editing the two data elements. If Python already exists, the optional stdlib [prepare_role_picker.py](../scripts/prepare_role_picker.py) embeds the current catalog, validates complete slot choices and writes a new preview file. Never install Python for this menu. Its output parent must already exist; it refuses existing targets, traversal and symlink/reparse paths. Example arguments:

```text
prepare_role_picker.py --output <new-absolute-preview.html> --selection <five-slot-JSON> --ignore-saved-state
```

When no confirmed team exists, copying the ready bundled asset requires no helper or Python. A maintenance catalog change should refresh the embedded catalog before packaging; runtime copies must remain self-contained.

## Confirmation and handoff

Use/profile/preset clicks affect only local selection. On hosts exposing `window.openai.sendFollowUpMessage`, the team review's primary **确认团队并回到聊天** requests a follow-up containing all five slots and the configuration-only scope. The host may ask the user to confirm sending. Without the bridge, the same primary action becomes **复制配置指令** when the native clipboard is available, or **选中指令，手动复制** otherwise. Clipboard denial switches to that manual label and reveals/selects the complete instruction. Always make the manual instruction available in an optional section. Tell the user to paste/send in chat to confirm; successful copying is not confirmation. Failed handoffs reveal the instruction for manual retry; no automatic retries or dispatch occur. After a successful handoff, say that the chat reply determines the configuration and that the user can describe their topic and authorized task there. Do not say research has started.

`widgetState` is optional, untrusted, best-effort presentation state. Schema version 2 stores canonical names by category; the original five-name array can restore a compatible legacy draft. Save only choices and configuration-only scope, with presentation category in privateContent. Never treat state as user authorization, evidence, a lab manifest or successful dispatch. Accept configuration only as an explicit user message and follow roster.md. Report the confirmed team or append an explicitly requested managed-run decision, without starting research.

Saved state can hydrate an untouched page. Once the user changes, copies or submits its draft, later host state events must not replace that local choice. Presentation view, use and category may be restored from privateContent only when valid; legacy saved arrays still restore a team review. Use native select/button keyboard behavior for adjustment rather than a custom tab system. Presentation navigation is not team confirmation.

## Text fallback

For a newcomer who asks for help choosing, start with concrete uses from entry_points or infer a small relevant team from their stated resources; do not require learning fifteen names or answering a questionnaire. Explain the Chinese responsibilities and the next chat action. Show all five categories and three names/styles when the user asks for the full catalog or custom selection. Preserve 均衡推进 / 前沿探索 / 有限预算 / 严谨验证 / 复现诊断 with their scenarios/tradeoffs and legacy preset aliases. State a known confirmed team rather than replacing it with a suggestion. End with a complete, usable message such as:

```text
$codexlab 团队配置：PI=Aster；文献=Atlas；方法=Nova；实验=不启用；审查=不启用。先只配置团队，不开始研究。
```

For an empty specialist list:

```text
$codexlab 只保留 Aster，先只配置团队。
```

Menu choice does not authorize a scientific stage. A prompt that already names a team and a scientific task goes directly to the requested task; do not insert an extra UI confirmation step.
