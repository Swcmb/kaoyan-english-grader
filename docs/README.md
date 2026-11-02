<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../LICENSE.
-->

# 文档中心

按任务查找安装、平台兼容、文档规范和版本发布信息。

## 安装与使用

- [安装总览](installation/README.md)：目录版、单文件版、平台技能市场、应用内创建和远程 Agent 的区别。
- [Skills CLI](installation/skills-cli.md)：从 Git 仓库安装标准 Agent Skill。
- [手机端渠道](installation/mobile-apps.md)：移动市场、个人 Skill 创建和远程连接。
- [平台指南](installation/platforms/)：各产品安装入口与能力边界。
- [Agent 安装协议](../INSTALL.md)：自动识别宿主、安装和验收。

## 文档规范

- [GitHub 内容写作与 Markdown 排版规范](standards/github-content-writing.md)：Issue、PR、评论和技术文档的结构、Markdown 与证据呈现。
- [公开开源项目文档规范](standards/open-source-docs.md)：项目类型研究、文档架构、README 语言、i18n 和发布门禁。
- [本机与私有项目文档规范](standards/local-dev-docs.md)：本机环境、私有配置、开发与运维记录。
- [第三方内容与许可证审查规范](standards/third-party-license-review.md)：来源、许可证、署名和再分发条件。

## 发布

- [GitHub Releases 发布说明](releasing.md)：版本标签、源码归档、SHA-256 和故障排查。

## 目录结构

```text
docs/
├── installation/
│   ├── README.md
│   ├── mobile-apps.md
│   ├── skills-cli.md
│   └── platforms/
├── standards/
│   ├── github-content-writing.md
│   ├── open-source-docs.md
│   ├── local-dev-docs.md
│   └── third-party-license-review.md
└── releasing.md
```

平台菜单、文件导入和账号权限会随版本、地区与灰度调整。未经确认的产品能力应标记为待核实，并以当前官方资料和客户端为准。
