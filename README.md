<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 考研英语 AI 批改

**一套覆盖考研英语一、英语二六类主观题的 Agent Skill。** 让 AI 按题型规则审题、模拟评分、逐句修改，并交付完整修订稿和针对性复盘。

本项目采用标准 Agent Skills 目录结构，可用于 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Qwen Code、Trae、Qoder、Antigravity、Kimi Code CLI、OpenClaw 等工具；也提供 Claude 网页版、WorkBuddy、千问办公等产品的本地导入说明。

> **评分边界：** 本项目提供备考训练用的模拟评价，不代表官方阅卷结果、官方评分细则、官方采分点或真实考试分数预测。

## 能做什么

- **六类题型独立批改：** 英语一、英语二的翻译、大作文和小作文分别使用对应规则，不混用满分和评分口径。
- **审题与切题核查：** 作文先核查写作任务、交际目的、图画寓意或图表信息，再评价内容、语言和结构。
- **翻译模拟采分：** 按句子或意群划分模拟采分点，解释准确、遗漏、误译和表达问题。
- **逐句纠错：** 区分【必须修改】与【可选优化】，保留正确、自然、有效的表达。
- **完整修订稿：** 提供修改后的全文，并说明修改依据。
- **学习复盘：** 归纳可复用表达、薄弱环节和后续练习重点。
- **图片作答支持：** 可处理清晰的题目、图画、图表和手写作答图片；无法辨认的文字会要求确认，不把识别错误当成考生错误。

## 支持题型

| 考试 | 题型 | 满分 | 详细规则 |
|---|---|---:|---|
| 英语一 | 大作文（B 节） | 20 分 | [英语一大作文规则](skills/kaoyan-english-grader/references/english1_essay_major.md) |
| 英语一 | 小作文（A 节应用文） | 10 分 | [英语一小作文规则](skills/kaoyan-english-grader/references/english1_essay_minor.md) |
| 英语一 | 翻译（5 个划线句） | 10 分 | [英语一翻译规则](skills/kaoyan-english-grader/references/english1_translation.md) |
| 英语二 | 大作文（通常为图表作文） | 15 分 | [英语二大作文规则](skills/kaoyan-english-grader/references/english2_essay_major.md) |
| 英语二 | 小作文（应用文） | 10 分 | [英语二小作文规则](skills/kaoyan-english-grader/references/english2_essay_minor.md) |
| 英语二 | 翻译 | 15 分 | [英语二翻译规则](skills/kaoyan-english-grader/references/english2_translation.md) |

## 快速安装

### 自然语言安装（推荐）

将下面这段话直接发送给你正在使用的 AI Agent。Agent 会识别当前宿主工具和运行环境，自行选择兼容的安装方式，执行安装并验证结果。

```text
请直接帮我安装这个仓库中的「考研英语 AI 批改」Skill（kaoyan-english-grader）。

仓库地址：https://github.com/Swcmb/kaoyan-english-grader
Agent 安装说明：https://raw.githubusercontent.com/Swcmb/kaoyan-english-grader/main/INSTALL.md
国内网络备用说明：https://gitee.com/ianwusb/kaoyan-english-grader/raw/main/INSTALL.md

请先读取并遵循仓库的 Agent 安装说明，自行识别当前 Agent、操作系统和工作区，选择当前环境真正支持的原生 Skill/插件安装方式、Skills CLI 或手动部署方式。请安装完整的 kaoyan-english-grader 目录，保留 SKILL.md 和 references/ 下的六份规则文件；根据当前工作区和宿主约定判断项目级或用户级安装范围。

请直接执行安装并验证 Agent 是否能够发现该 Skill。不要只给我安装教程或命令；遇到当前环境无法自动完成的 UI 操作、权限限制或其他阻塞时，明确说明具体原因和我需要完成的最后一步。不要覆盖同名的其他 Skill，也不要修改无关项目文件。
```

自然语言安装会根据 Agent 的实际能力选择路径；支持情况以当前 Agent 的官方机制为准。Agent 无法直接操作宿主 UI 时，会给出需要用户完成的最后一步。

<details>
<summary><strong>国内网络：从 Gitee 安装（推荐）</strong></summary>

要求 Node.js 22.20 或更高版本。

**交互式选择 Agent：**

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader
~~~

**指定一个 Agent：**

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex
~~~

将 codex 替换为目标 Agent 的标识。需要安装到用户级目录时增加 -g；不加 -g 时按当前项目安装。

**一次安装到多个 Agent：**

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  -a claude-code \
  -a codex \
  -a cursor \
  -a opencode \
  -a gemini-cli \
  -a antigravity \
  -a kimi-code-cli \
  -a qwen-code \
  -a qoder \
  -a trae-cn \
  -a openclaw
~~~

</details>

<details>
<summary><strong>备用：从 GitHub 安装</strong></summary>

~~~bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git --skill kaoyan-english-grader
~~~

</details>

<details>
<summary><strong>网络受限：先克隆，再从本地安装</strong></summary>

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
~~~

如 Gitee 地址不可访问，可将 clone 地址替换为 GitHub。若需要全局安装，添加 -g。

</details>

完整安装参数、目标 Agent 标识和故障排查见[通用 Skills CLI 安装指南](docs/README.skills-cli.md)。

## 支持渠道与详细操作

本项目将“安装本仓库的标准 Skill”和“使用产品技能市场中的现成技能”分开说明。只有能够完整保留主文件与引用目录的渠道，才能完整运行本项目六类题型规则。

### 标准 Agent Skills / 开发工具

| 渠道 | 安装方式 | 详细操作 |
|---|---|---|
| Claude Code | Skills CLI 或本地目录 | [Claude Code 安装指南](docs/README.claude-code.md) |
| Codex | Skills CLI 或本地目录 | [Codex 安装指南](docs/README.codex.md) |
| Cursor | Skills CLI 或本地目录 | [Cursor 安装指南](docs/README.cursor.md) |
| OpenCode | Skills CLI 或本地目录 | [OpenCode 安装指南](docs/README.opencode.md) |
| Gemini CLI | Skills CLI 或本地目录 | [Gemini CLI 安装指南](docs/README.gemini-cli.md) |
| Qwen Code | Skills CLI 或本地目录 | [Qwen Code 安装指南](docs/README.qwen-code.md) |
| Antigravity | Skills CLI、插件或本地目录 | [Antigravity 安装指南](docs/README.antigravity.md) |
| Kimi Code CLI | Skills CLI、插件或本地目录 | [Kimi Code 安装指南](docs/README.kimi-code.md) |
| Trae / Trae CN | Skills CLI、IDE 导入 SKILL.md/ZIP | [Trae 安装指南](docs/README.trae.md) |
| Qoder | Skills CLI、IDE 上传 Skill ZIP/SKILL.md | [Qoder 安装指南](docs/README.qoder.md) |
| OpenClaw | OpenClaw CLI 安装本地 Skill | [OpenClaw 安装指南](docs/README.openclaw.md) |

### AI 助手与本地技能导入

| 产品 | 支持方式 | 详细操作 |
|---|---|---|
| Claude 网页版 / Desktop | Customize → Skills 上传 ZIP | [Claude 自定义 Skill 安装指南](docs/README.claude.md) |
| 豆包工作任务模式 | 创建个人自定义技能；开发者开放平台可提交 ZIP 上架 | [豆包桌面端指南](docs/README.doubao.md) |
| WorkBuddy 桌面端 | 上传本地技能 ZIP | [WorkBuddy 桌面端指南](docs/README.workbuddy.md) |
| 千问办公（QwenWork） | 扩展 → 技能 → 上传 SKILL.md/ZIP | [千问办公指南](docs/README.qwenwork.md) |
| 腾讯元宝 | 技能市场安装；普通用户本地标准 Skill 导入未确认 | [腾讯元宝指南](docs/README.yuanbao.md) |

### 手机 App 与小程序

手机端入口、技能市场和自定义导入边界见[手机端 Skill 使用渠道索引](docs/README.mobile-apps.md)。

| 产品 | 手机端能力 | 详细操作 |
|---|---|---|
| 豆包 App | 使用账号当前可用的技能；创建管理以电脑版为主 | [豆包手机端](docs/README.doubao-mobile.md) |
| 腾讯元宝 App | 浏览、安装、调用技能市场内容 | [元宝 App](docs/README.yuanbao-app.md) |
| 千问 App | 工作助理中的技能广场 | [千问 App](docs/README.qwen-app.md) |
| WorkBuddy 微信小程序 | SkillHub 安装、对话中添加技能 | [WorkBuddy 手机版](docs/README.workbuddy-mobile.md) |
| 脑花 | 将验证过的协作流程沉淀为个人 Skill | [脑花 App](docs/README.brainhua.md) |
| 智图Claw | 技能市场、技能管理和 Gateway 连接 | [智图Claw](docs/README.zhitu-claw.md) |
| 灵犀·晓伴 | AI 工具与技能中心、第三方技能扩展 | [灵犀·晓伴](docs/README.lingxi-xiaoban.md) |
| AgentOS（艾嘿） | 技能商店和历史版本中的自定义安装能力 | [AgentOS](docs/README.agentos.md) |
| AionClaw | iOS/Android 技能市场 | [AionClaw](docs/README.aionclaw.md) |

**重要区别：** 技能市场中安装一个现成技能，不代表该 App 可以导入本仓库的标准 Skill。腾讯元宝、部分手机 App 当前按市场/应用内能力使用；脑花强调应用内流程沉淀；OpenClaw 和智图Claw 可通过 Gateway 在远程主机执行技能。具体边界以各平台详细指南为准。

## 使用方式

安装后，直接告诉 Agent 考试类型和题型，附上题目和自己的作答。可以使用以下模板：

~~~text
请使用考研英语 AI 批改 Skill。

考试：英语一
题型：翻译
题目与英文原文：
（粘贴原文或上传清晰图片）

我的译文：
（粘贴译文）

请按对应规则完成模拟评分、逐句讲解、修改稿和复盘。
~~~

作文任务可使用：

~~~text
请使用考研英语 AI 批改 Skill。

考试：英语二
题型：大作文
题目与图表：
（粘贴题目、上传图表）

我的作文：
（粘贴作文）

请先核查题目任务与图表信息，再按英语二大作文规则模拟评分。
~~~

## 项目结构

~~~text
kaoyan-english-grader/
├── skills/
│   └── kaoyan-english-grader/
│       ├── SKILL.md
│       └── references/
│           ├── english1_essay_major.md
│           ├── english1_essay_minor.md
│           ├── english1_translation.md
│           ├── english2_essay_major.md
│           ├── english2_essay_minor.md
│           └── english2_translation.md
├── .claude-plugin/
├── .codex-plugin/
├── .cursor-plugin/
├── .antigravity-plugin/
├── .agents/plugins/marketplace.json
├── plugin.json
├── gemini-extension.json
├── kimi.plugin.json
├── GEMINI.md
├── LICENSE
├── COPYING
└── docs/
    ├── README.*.md
    ├── github-content-writing.md
    └── third-party-license-review.md
~~~

只分发技能时，复制 skills/kaoyan-english-grader/ 完整目录即可。不要只复制 SKILL.md，references/ 是批改流程所需的规则文件。

## 评分原则与边界

1. 英语一和英语二的分值、评分档位、题型要求分别执行，不混用规则。
2. 作文先判断任务完成度与切题性，再评估语言、结构和格式。
3. 翻译采分点是用于训练反馈的模拟划分，不代表官方采分表。
4. 评分必须引用作答中的具体内容作为依据，不为了鼓励而抬分，也不为了显得严格而压分。
5. 区分真实错误和可选优化；正确、自然、符合语境的表达可以保留。
6. 不猜测模糊手写文字，不编造图表数据、题目要求、事实或因果关系。
7. 资料不完整时明确评价边界；可可靠判断的部分仍可继续批改。

## 文档与贡献

本仓库把使用手册、工程规范和许可审查规范分开维护：

- [全部平台安装文档索引](docs/README.domestic-platforms.md)
- [手机端 Skill 使用渠道索引](docs/README.mobile-apps.md)
- [Skills CLI 通用安装指南](docs/README.skills-cli.md)
- [GitHub 内容写作与 Markdown 排版规范](docs/github-content-writing.md)
- [第三方内容与许可证审查规范](docs/third-party-license-review.md)

文档以 GitHub 最终渲染效果为准。Issue、PR 和技术说明应结论先行，区分事实、假设、方案和验证结果，避免把计划执行的测试写成已通过。

## 许可证

本仓库原创内容采用 [GNU GPL-3.0-or-later](LICENSE)，完整文本同时保存在 [COPYING](COPYING)。引入的第三方文件继续保留各自的文件级许可、版权声明和必要通知。
