<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Repository Instructions

本文件是 Gemini CLI 及能够读取仓库指令的 Gemini 类 Agent 的入口。

## Skill 使用规则

考研英语批改任务统一使用唯一的自包含 Skill：

- `@./skills/kaoyan-english-grader/SKILL.md`

处理英语一、英语二的翻译、大作文或小作文时，先识别考试与题型，再完整读取对应题型的评分规则。六类题型的全部评分规则均位于该文件中，不依赖额外引用目录。

讲解语言使用中文；英文原句、修改句、例句和修改后的英文作文保留英文。所有分数均为练习模拟评价，不得表述为官方阅卷结果、官方评分细则或真实考试分数预测。

## 文档规范

- GitHub 内容、Issue、PR、评论和 README 遵循 [GitHub 内容写作规范](docs/standards/github-content-writing.md)。
- 公开文档体系、README 语言与发布内容遵循 [开源项目文档规范](docs/standards/open-source-docs.md)。
- 本机环境、私有配置和开发手册遵循 [本机与私有项目文档规范](docs/standards/local-dev-docs.md)。
- 第三方代码、Skill、Prompt、模板和文档的复制、改编与发布遵循 [第三方许可证审查规范](docs/standards/third-party-license-review.md)。

## 修改与验证

先检查现状、目标路径和影响范围，再进行完成任务所需的最小修改。区分事实、假设、计划和已验证结果；涉及平台能力时优先查看当前官方资料。

完成后检查相对链接、Markdown、命令和路径，执行对应测试并如实报告。未运行的检查标记为未执行。

除用户明确要求外，不修改 Skill 的评分规则内容。
