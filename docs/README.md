<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../LICENSE.
-->

# 文档中心

按任务查找安装说明、项目规范和版本发布信息。

## 安装与使用

- [安装总览](installation/README.md)：区分标准 Skill 导入、平台市场和远程 Agent。
- [Skills CLI](installation/skills-cli.md)：使用 Vercel Skills CLI 安装与维护。
- [手机端渠道](installation/mobile-apps.md)：手机 App、小程序和远程 Agent 的使用边界。
- [平台指南](installation/platforms/)：各 Agent、IDE 和 AI 产品的具体安装说明。
- [Agent 自主安装协议](../INSTALL.md)：供 Agent 识别宿主、选择安装方法并验证。

## 文档规范

- [GitHub 内容写作与 Markdown 排版规范](standards/github-content-writing.md)：Issue、PR、评论和技术文档结构。
- [公开开源项目文档规范](standards/open-source-docs.md)：文档体系、项目类型研究、README 语言和发布门禁。
- [本机与私有项目文档规范](standards/local-dev-docs.md)：本地环境、Agent 工作区和私有文档。
- [第三方内容与许可证审查规范](standards/third-party-license-review.md)：来源、许可证和署名检查。

## 发布

- [GitHub Releases 发布说明](releasing.md)：版本标签、Release 资产、SHA-256 校验和故障排查。

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
│   ├── local-dev-docs.md
│   ├── open-source-docs.md
│   └── third-party-license-review.md
└── releasing.md
```

平台功能、界面和目录可能随版本、地区与账号灰度变化。涉及产品能力的判断应以指南列出的官方资料及当前客户端为准。
