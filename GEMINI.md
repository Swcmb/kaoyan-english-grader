<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Repository Instructions

本文件是 Gemini CLI 及能够读取仓库指令的 Gemini 类 Agent 的入口。

## Skill 选择

仓库提供两个独立 Skill：

- 默认使用标准版：@./skills/kaoyan-english-grader/SKILL.md
- 只有用户明确选择完整版，或目标平台无法保留标准 Skill 的 `references/` 目录且只支持单文件导入时，使用：@./skills/kaoyan-english-grader-full/SKILL.md

标准版依赖同目录下的六份 `references/` 规则文件。完整目录安装时必须保留主文件与引用目录。完整版已将六类规则内嵌到单个文件中，不依赖外部引用；支持标准 Skill 目录的平台优先使用标准版。

处理考研英语一、英语二的翻译、大作文或小作文时，先识别考试与题型，再完整读取所选版本中的对应评分规则。所有分数均为练习模拟评价，不得表述为官方阅卷结果或真实分数预测。

## 文档规范

- GitHub 内容、Issue、PR、评论和 README 遵循 [GitHub 内容写作规范](docs/standards/github-content-writing.md)。
- 公开文档体系、README 语言与发布内容遵循 [开源项目文档规范](docs/standards/open-source-docs.md)。
- 本机环境、私有配置和开发手册遵循 [本机与私有项目文档规范](docs/standards/local-dev-docs.md)。
- 第三方代码、Skill、Prompt、模板和文档的复制、改编与发布遵循 [第三方许可证审查规范](docs/standards/third-party-license-review.md)。

## 修改与验证

先检查现状、目标路径和影响范围，再进行完成任务所需的最小修改。区分事实、假设、计划和已验证结果；涉及平台能力时优先查看当前官方资料。

完成后检查相对链接、Markdown、命令和路径，执行对应测试并如实报告。未运行的检查标记为未执行。

除用户明确要求外，不修改两个 Skill 的评分规则内容。
