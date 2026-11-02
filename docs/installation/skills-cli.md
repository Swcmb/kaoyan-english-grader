<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 使用 Skills CLI 安装考研英语批改 Skill

[Vercel Skills CLI](https://github.com/vercel-labs/skills) 可从 Git 仓库、URL 或本地目录获取标准 Agent Skill，并安装到所选 Agent 的项目级或用户级目录。国内网络可优先尝试 Gitee 镜像。

## 环境要求

Skills CLI 当前文档要求 Node.js 22.20 或更高版本。还需要 Git 能访问所选仓库源，并且目标 Agent 在当前 CLI 支持清单中。

```bash
node --version
npm --version
git --version
```

## 交互式安装

在目标项目目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader
```

按提示选择 Agent、安装范围和文件管理方式。若 CLI 支持符号链接，可使用单一源目录；需要独立文件副本时选择复制方式。

## 指定 Agent

例如安装到 Codex：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex
```

支持多个 Agent 时可以重复传入 Agent ID：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent claude-code codex cursor opencode
```

Agent ID 与目录映射可能随 CLI 版本调整。执行前查看[官方 Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)，不要使用未经确认的标识。

## 项目级与用户级安装

项目级安装写入当前工作区，适合随项目共享。用户级安装适用于多个工作区，增加 `-g`：

```bash
# 项目级
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent codex

# 用户级
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent codex -g
```

具体目录由 Agent ID 决定。以 CLI 当前目录映射为准，不把某个版本的目录约定视为永久路径。

## 从本地仓库安装

网络不稳定时先克隆，再安装：

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
```

备用 GitHub 源：

```bash
git clone https://github.com/Swcmb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
```

## 安装结构与验证

必须保留以下结构：

```text
kaoyan-english-grader/
├── SKILL.md
└── references/
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
```

安装后检查目标目录、六份引用文件和 Agent 发现状态。分别提交英语一翻译和英语二大作文测试，确认对应规则读取正常。不要只凭 CLI 退出码判断完整安装成功。

## 查看、更新与卸载

```bash
npx skills list
npx skills check
npx skills update kaoyan-english-grader
npx skills remove kaoyan-english-grader
```

执行卸载前确认工作区、安装范围与技能名称。CLI 命令和参数可能变化，遇到行为差异时以当前 `npx skills --help` 和[官方命令文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)为准。

## 官方资料

- [Skills CLI：命令文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Skills CLI：Agent 与目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [Skills CLI：项目主页与环境要求](https://github.com/vercel-labs/skills)
- [Node.js 下载](https://nodejs.org/en/download)
