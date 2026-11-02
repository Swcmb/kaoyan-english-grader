<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Repository Instructions

本文件是 Gemini 类 Agent 的仓库级入口。

## 考研英语批改

@./skills/kaoyan-english-grader/SKILL.md

用户要求批改考研英语一、英语二的翻译、大作文或小作文时，遵循该 Skill。先识别考试类型和题型，再读取对应评分规则。所有分数均为练习模拟评价，不得表述为官方阅卷结果。

## 文档与许可证

- 编辑 README、平台安装指南、Issue、Pull Request 或评论时，遵循 [GitHub 内容写作规范](docs/standards/github-content-writing.md)。
- 修改公开项目文档体系、README 语言或发布内容前，遵循 [公开开源项目文档规范](docs/standards/open-source-docs.md)。
- 处理本机环境、私有配置和开发操作手册时，遵循 [本机与私有项目文档规范](docs/standards/local-dev-docs.md)。
- 复制、改编、翻译、重命名、vendor 或发布第三方代码、Skill、Prompt、配置和模板前，遵循 [第三方许可证审查规范](docs/standards/third-party-license-review.md)，记录文件级来源和许可证据。

## 变更与验证

先检查现有状态和适用范围，采用满足目标的最小修改。不要修改 `skills/kaoyan-english-grader/` 中的 Skill 文件，除非用户明确要求。

区分事实、假设、计划和已验证结果。完成变更后执行对应检查，并报告真实结果；未运行的检查标记为未执行。
