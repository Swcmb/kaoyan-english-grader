<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 考研英语 AI 批改

**一套面向考研英语一、英语二的 Agent Skill，覆盖翻译、大作文和小作文六类主观题。** 根据题型专属规则完成审题、模拟评分、逐句修改、完整修订稿和针对性复盘。

支持 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Qwen Code、Antigravity、Kimi Code CLI、Trae、Qoder、OpenClaw，以及具备完整 Skill 导入能力的 AI 助手。

> **评分说明：** 本项目用于备考训练和写作反馈。所有分数均为模拟评价，不代表官方阅卷结果、官方评分细则或真实考试分数预测。

## 功能

- **六类题型独立评分：** 英语一、英语二分别使用对应翻译、大作文和小作文规则，不混用分值与评分口径。
- **先审题再评分：** 作文先核查任务要求、交际目的、图画寓意或图表信息，再评价内容、语言和结构。
- **翻译模拟采分：** 按句子或意群分析准确、遗漏、误译和表达问题，说明每项判断依据。
- **逐句纠错：** 区分【必须修改】与【可选优化】，保留正确、自然且有效的表达。
- **完整修订稿：** 提供修改后的全文，并解释关键调整。
- **针对性复盘：** 归纳可复用表达、主要薄弱点和下一步练习方向。
- **图片作答支持：** 可处理清晰的题目、图画、图表和手写作答图片；无法辨认的文字会标记并请求确认。

## 支持题型

| 考试 | 题型 | 满分 | 评分规则 |
| --- | --- | ---: | --- |
| 英语一 | 大作文（B 节） | 20 分 | [英语一大作文](skills/kaoyan-english-grader/references/english1_essay_major.md) |
| 英语一 | 小作文（A 节应用文） | 10 分 | [英语一小作文](skills/kaoyan-english-grader/references/english1_essay_minor.md) |
| 英语一 | 翻译（5 个划线句） | 10 分 | [英语一翻译](skills/kaoyan-english-grader/references/english1_translation.md) |
| 英语二 | 大作文（通常为图表作文） | 15 分 | [英语二大作文](skills/kaoyan-english-grader/references/english2_essay_major.md) |
| 英语二 | 小作文（应用文） | 10 分 | [英语二小作文](skills/kaoyan-english-grader/references/english2_essay_minor.md) |
| 英语二 | 翻译 | 15 分 | [英语二翻译](skills/kaoyan-english-grader/references/english2_translation.md) |

## 安装

### 自然语言安装（推荐）

将下面的指令直接发送给你正在使用的 AI Agent。Agent 会识别当前宿主、工作区和权限，自行选择受支持的安装方法，执行安装并验证结果。

```text
请帮我安装这个仓库中的「考研英语 AI 批改」Skill（kaoyan-english-grader）。

仓库地址：https://github.com/Swcmb/kaoyan-english-grader
国内网络备用地址：https://gitee.com/ianwusb/kaoyan-english-grader
Agent 安装说明：https://raw.githubusercontent.com/Swcmb/kaoyan-english-grader/main/INSTALL.md

请先读取 INSTALL.md，自行识别当前 Agent、操作系统和工作区，选择当前环境真正支持的原生 Skill/插件安装器、Skills CLI 或手动部署方式。只安装 kaoyan-english-grader，保留 SKILL.md 和 references/ 下六份题型规则；根据当前工作区和宿主约定选择项目级或用户级范围。

请直接执行安装并验证 Agent 是否能够发现该 Skill。不要只给我教程或命令。若当前环境无法自动完成 UI 操作或受到权限限制，请说明具体阻塞和我需要完成的最后一步。不要覆盖来源不明的同名 Skill，也不要修改无关文件。
```

Agent 应以仓库根目录的 [INSTALL.md](INSTALL.md) 为执行规范。安装完成后，检查目标目录是否包含主文件和六份规则，并确认宿主能够发现该 Skill。

### 使用 Skills CLI 安装

国内网络优先使用 Gitee：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

指定 Agent，例如 Codex：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex
```

安装到用户级目录时增加 `-g`。Skills CLI 的 Agent ID 和目录映射会随版本更新，使用前请核对[官方支持列表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

备用 GitHub 源：

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

### 其他安装方式

- **Claude 网页版 / Desktop：** [上传完整 Skill ZIP](docs/README.claude.md)。
- **WorkBuddy：** [桌面端上传技能 ZIP](docs/README.workbuddy.md)。
- **QwenWork：** [上传本地 SKILL.md / ZIP](docs/README.qwenwork.md)。
- **Trae / Qoder：** [Trae 导入](docs/README.trae.md) · [Qoder 导入](docs/README.qoder.md)。
- **开发工具与 Agent CLI：** 查看[国内平台安装索引](docs/README.domestic-platforms.md)和[Skills CLI 指南](docs/README.skills-cli.md)。
- **手机 App / 小程序：** 查看[手机端渠道索引](docs/README.mobile-apps.md)。

平台技能市场、应用内沉淀和标准 Agent Skill 文件导入是不同能力。平台指南会明确标注本地文件导入是否已确认；只有保留完整目录的安装方式才能复用本仓库六类题型规则。

## 使用方式

安装后，直接向 Agent 提供考试类型、题型、题目和作答。也可以明确指定本 Skill。

### 翻译批改示例

```text
请使用考研英语 AI 批改 Skill。

考试：英语一
题型：翻译

英文原文：
（粘贴原文，包含上下文）

我的译文：
（粘贴译文）

请按英语一翻译规则进行模拟评分，逐句分析失分点，提供修改稿和复盘。
```

### 作文批改示例

```text
请使用考研英语 AI 批改 Skill。

考试：英语二
题型：大作文

题目与图表：
（粘贴题目或上传清晰图片）

我的作文：
（粘贴作文）

请先提取题目任务和图表信息，再按英语二大作文规则模拟评分、逐句修改并给出完整修订稿。
```

## 评分原则

1. 英语一、英语二的题型、分值和评分档位分别执行。
2. 作文先核查任务完成度与切题性，再评价语言、结构和格式。
3. 翻译采分点是训练用的模拟划分，不代表官方采分表。
4. 每项重要评价和扣分都对应具体原文、译文或题目要求。
5. 区分真实错误与可选优化；正确、自然且符合语境的表达可以保留。
6. 不猜测模糊手写文字，不编造图表数据、事实或因果关系。
7. 资料不完整时明确评价边界；能够可靠判断的部分仍可继续批改。

## 项目结构

```text
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
├── INSTALL.md
├── GEMINI.md
├── LICENSE
├── COPYING
└── docs/
    ├── README.*.md
    ├── github-content-writing.md
    └── third-party-license-review.md
```

只分发 Skill 时，复制 `skills/kaoyan-english-grader/` 完整目录。不要只复制 `SKILL.md`，六份 `references/` 文件是题型批改所需的规则。

## 文档与贡献

- [国内平台安装索引](docs/README.domestic-platforms.md)
- [手机端渠道索引](docs/README.mobile-apps.md)
- [Skills CLI 安装指南](docs/README.skills-cli.md)
- [Agent 自主安装规范](INSTALL.md)
- [GitHub 内容写作与 Markdown 排版规范](docs/github-content-writing.md)
- [第三方内容与许可证审查规范](docs/third-party-license-review.md)

Issue、PR 和技术说明应结论先行，区分事实、假设、方案与验证。测试结果必须来自实际执行记录。文档发布前检查链接、代码块、表格和 GitHub 渲染效果。

## 许可证

本仓库原创内容采用 [GNU GPL-3.0-or-later](LICENSE)，完整文本同时保存在 [COPYING](COPYING)。第三方文件继续保留各自的许可证、版权声明和必要通知。
