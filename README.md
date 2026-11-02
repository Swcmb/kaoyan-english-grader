<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 考研英语 AI 批改

**面向考研英语（一）（二）的 Agent Skill，覆盖翻译、大作文和小作文六类主观题。** 按题型专属规则完成审题、模拟评分、逐句修改、完整修订稿和针对性复盘。

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPL--3.0--or--later-blue.svg)](LICENSE)
[![GitHub Releases](https://img.shields.io/github/v/release/Swcmb/kaoyan-english-grader?display_name=tag)](https://github.com/Swcmb/kaoyan-english-grader/releases)
[![GitHub Actions](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml/badge.svg)](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml)

> 本项目用于备考训练和写作反馈。所有分数均为模拟评价，不代表官方阅卷结果、官方评分细则或真实考试分数预测。

## 核心能力

| 题型 | 英语一 | 英语二 |
| --- | --- | --- |
| 翻译 | 5 个划线句，10 分 | 全文翻译，15 分 |
| 大作文 | 图画作文，20 分 | 图表作文，15 分 |
| 小作文 | 应用文，10 分 | 应用文，10 分 |

针对每类题型分别应用评分规则，避免混用考试分值和评分口径。

**批改输出包括：** 任务与审题分析、模拟评分及依据、逐句问题定位、修改建议、完整修订稿和针对性复盘。翻译按句子或意群分析准确、遗漏、误译和表达问题；作文先检查任务完成度与切题性，再评价内容、语言和结构。

## 安装

### 自然语言安装（推荐）

将下面的指令发送给当前 AI Agent。Agent 应读取安装协议，识别宿主和权限，选择实际支持的安装方式，执行后验证。

```text
请帮我安装这个仓库中的「考研英语 AI 批改」Skill（kaoyan-english-grader）。

GitHub：https://github.com/Swcmb/kaoyan-english-grader
Gitee：https://gitee.com/ianwusb/kaoyan-english-grader
安装协议：https://raw.githubusercontent.com/Swcmb/kaoyan-english-grader/main/INSTALL.md

请读取 INSTALL.md，自行识别当前 Agent、操作系统和工作区，选择受支持的原生 Skill 安装器、Skills CLI 或手动部署方式。只安装 kaoyan-english-grader，保留 SKILL.md 和 references/ 下六份规则。请直接执行安装并验证 Agent 能发现该 Skill；不要只给教程或命令。不要覆盖来源不明的同名 Skill，也不要修改无关文件。
```

### Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

指定 Codex：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex
```

用户级安装增加 `-g`。完整说明见 [Skills CLI 安装指南](docs/installation/skills-cli.md)。

### 其他平台

- [开发工具与 Agent CLI 安装总览](docs/installation/README.md)
- [Claude 网页版 / Desktop](docs/installation/platforms/claude.md)
- [Trae](docs/installation/platforms/trae.md)
- [Qoder](docs/installation/platforms/qoder.md)
- [WorkBuddy](docs/installation/platforms/workbuddy.md)
- [QwenWork](docs/installation/platforms/qwenwork.md)
- [手机端渠道](docs/installation/mobile-apps.md)

平台技能市场、应用内创建和标准 Skill 文件导入是不同能力。只有完整保留 Skill 主文件与引用目录的安装方式，才能直接复用本项目的全部评分规则。

## 使用

安装后，提供考试类型、题型、题目和作答即可。也可以显式调用 `kaoyan-english-grader`。

翻译任务示例：

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

作文任务示例：

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

## 评分边界

- 英语一、英语二的题型、分值和评分档位分别执行。
- 翻译采分点属于训练用模拟划分，不代表官方采分表。
- 每项重要评价和扣分对应具体原文、译文或题目要求。
- 区分真实错误与可选优化；正确、自然且符合语境的表达可以保留。
- 不猜测模糊手写文字，不编造图表数据、事实或原文没有的信息。

## 项目结构

```text
kaoyan-english-grader/
├── .agents/                  # Agent 插件市场元数据
├── .antigravity-plugin/      # Antigravity 插件元数据
├── .claude-plugin/           # Claude 插件元数据
├── .codex-plugin/            # Codex 插件元数据
├── .cursor-plugin/           # Cursor 插件元数据
├── .github/workflows/        # GitHub Release 工作流
├── docs/
│   ├── installation/         # 安装索引与平台指南
│   ├── standards/            # 文档与许可证规范
│   └── releasing.md          # GitHub Releases 发布说明
├── skills/
│   └── kaoyan-english-grader/
│       ├── SKILL.md
│       └── references/       # 六份题型评分规则
├── GEMINI.md                 # Gemini 类 Agent 仓库指令
├── INSTALL.md                # Agent 自主安装协议
├── LICENSE
└── README.md
```

## GitHub Releases

推送符合格式的版本标签（例如 `v1.0.0`）后，GitHub Actions 自动创建 Release，并附加完整源码 ZIP、TAR.GZ 和 SHA-256 校验文件。

- [查看 Releases](https://github.com/Swcmb/kaoyan-english-grader/releases)
- [版本发布说明](docs/releasing.md)

## 文档

- [文档中心](docs/README.md)
- [安装与使用渠道](docs/installation/README.md)
- [公开开源项目文档规范](docs/standards/open-source-docs.md)
- [GitHub 内容写作规范](docs/standards/github-content-writing.md)
- [本机与私有项目文档规范](docs/standards/local-dev-docs.md)
- [第三方许可证审查规范](docs/standards/third-party-license-review.md)

## License

本仓库原创内容采用 [GNU GPL-3.0-or-later](LICENSE)。第三方材料继续保留各自的版权声明、许可证和必要通知。
