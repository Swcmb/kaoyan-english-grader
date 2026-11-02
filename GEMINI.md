<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Repository Instructions

本文件是 Gemini CLI 及能够读取仓库指令的 Gemini 类 Agent 的入口。

## Skill 使用

@./skills/kaoyan-english-grader/SKILL.md

处理考研英语一、英语二的翻译、大作文或小作文时，先识别考试与题型，再完整读取对应评分规则。所有分数均为练习模拟评价，不得表述为官方阅卷结果或真实分数预测。

用户明确选择单文件版本时，使用 `dist/kaoyan-english-grader-single-file/SKILL.md` 作为独立完整规则来源，不要混合两个版本。

## 文档规范

- GitHub 内容、Issue、PR、评论和 README 遵循 [GitHub 内容写作规范](docs/standards/github-content-writing.md)。
- 公开文档体系、README 语言与发布内容遵循 [开源项目文档规范](docs/standards/open-source-docs.md)。
- 本机环境、私有配置和开发手册遵循 [本机与私有项目文档规范](docs/standards/local-dev-docs.md)。
- 第三方代码、Skill、Prompt、模板和文档的复制、改编与发布遵循 [第三方许可证审查规范](docs/standards/third-party-license-review.md)。

## 修改与验证

先检查现状、目标路径和影响范围，再进行完成任务所需的最小修改。区分事实、假设、计划和已验证结果；涉及平台能力时优先查看当前官方资料。

完成后检查相对链接、Markdown、命令和路径，执行对应测试并如实报告。未运行的检查标记为未执行。

除用户明确要求外，不修改 `skills/kaoyan-english-grader/` 中的标准 Skill 文件。
