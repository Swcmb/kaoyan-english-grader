<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../LICENSE.
-->

# 文档中心

按任务查找 Skill 版本、安装渠道、平台兼容、文档规范和版本发布信息。

## Skill 与安装

- [安装与版本选择](installation/README.md)：两个 Skill 的区别、推荐顺序及各类平台能力边界。
- [Skills CLI](installation/skills-cli.md)：从 Git 仓库安装标准 Agent Skill。
- [手机端渠道](installation/mobile-apps.md)：技能市场、应用内创建和远程 Agent 的区别。
- [平台指南](installation/platforms/)：各产品安装入口、文件格式和能力边界。
- [Agent 安装协议](../INSTALL.md)：识别平台、选择 Skill、安装和验收。

## 两个 Skill

- 标准版：[`skills/kaoyan-english-grader/`](../skills/kaoyan-english-grader/SKILL.md)，需完整保留 `SKILL.md` 与 `references/` 六份规则。
- 完整版：[`skills/kaoyan-english-grader-full/SKILL.md`](../skills/kaoyan-english-grader-full/SKILL.md)，六类规则全部内嵌，供单文件导入场景使用。

## 文档规范

- [GitHub 内容写作与 Markdown 排版规范](standards/github-content-writing.md)：Issue、PR、评论和技术文档的结构、Markdown 与证据呈现。
- [公开开源项目文档规范](standards/open-source-docs.md)：项目类型研究、文档架构、README 语言、i18n 和发布门禁。
- [本机与私有项目文档规范](standards/local-dev-docs.md)：本机环境、私有配置、开发与运维记录。
- [第三方内容与许可证审查规范](standards/third-party-license-review.md)：来源、许可证、署名和再分发条件。

## 发布

- [GitHub Releases 发布说明](releasing.md)：版本标签、源码归档、SHA-256 和故障排查。
