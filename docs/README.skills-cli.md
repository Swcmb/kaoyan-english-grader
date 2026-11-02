<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 使用 Skills CLI 安装考研英语批改 Skill

Vercel Skills CLI 可从 Git 仓库获取标准 Agent Skill，并安装到所选 Agent 的项目级或用户级目录。本仓库提供 Gitee 镜像，国内网络优先使用 Gitee。

不想手动选择命令时，将 [README 中的自然语言安装指令](../README.md#自然语言安装) 发给当前 Agent。Agent 会读取 [INSTALL.md](../INSTALL.md)，识别当前宿主并验证安装结果。

## 环境要求

- Node.js 22.20 或更高版本。
- Git 可访问所选仓库源。
- 目标 Agent 在当前 Skills CLI 版本的支持清单中。

检查环境：

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

按交互提示选择 Agent、安装范围和文件管理方式。安装后检查 Agent 是否发现技能，不要只凭 CLI 退出码判断成功。

## 指定 Agent

例如安装到 Codex：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex
```

如需同时安装到多个 Agent，可重复提供受支持的 `--agent` 参数：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  -a claude-code -a codex -a cursor -a opencode \
  -a gemini-cli -a antigravity -a kimi-code-cli \
  -a qwen-code -a qoder -a trae-cn -a openclaw
```

Agent ID 与目录映射可能随 CLI 版本调整。执行前查看[官方 Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)，不要使用未经确认的标识。

## 项目级与用户级安装

项目级安装写入当前工作区，适合随仓库共享。用户级安装适用于当前用户的多个工作区，增加 `-g`：

```bash
# 项目级
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent codex

# 用户级
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent codex -g
```

具体目录由 Agent ID 决定。Codex 常用 `.agents/skills/`，Claude Code 常用 `.claude/skills/`；以当前 CLI 目录映射为准。

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

必须保留如下结构：

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

安装后检查目标目录、六份引用文件和 Agent 发现状态。分别提交英语一翻译、英语二大作文测试，确认对应规则读取正常。

## 查看、更新与卸载

```bash
npx skills list
npx skills update
npx skills remove kaoyan-english-grader
```

使用卸载命令前确认工作区、安装范围与技能名称。全局安装和指定 Agent 的参数以当前 CLI 文档为准。

## 常见问题

| 现象 | 检查方向 |
| --- | --- |
| Node.js 版本不满足 | 检查 `node --version`，升级至 22.20 或更高版本 |
| Git 克隆失败 | 检查网络；切换 Gitee/GitHub 源或先克隆再安装 |
| Agent 未识别 | 更新 CLI 并核对官方 Agent ID 清单 |
| Agent 未发现 Skill | 检查目标目录是否含 `kaoyan-english-grader/SKILL.md` |
| 批改时缺少规则 | 检查 `references/` 六份文件是否完整 |
| 仍使用旧版本 | 更新后开启新会话或按宿主要求重新加载 |

## 平台原生导入

- [Claude 网页版/Desktop](README.claude.md)：Customize → Skills 上传 ZIP。
- [Qoder](README.qoder.md)：Extensions → Skills 上传技能包。
- [Trae](README.trae.md)：设置 → 技能与命令 → 导入。
- [WorkBuddy](README.workbuddy.md)：技能管理页上传 ZIP。
- [QwenWork](README.qwenwork.md)：扩展 → 技能 → 上传 ZIP。

## 官方资料

- [Skills CLI：命令文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Skills CLI：Agent 与目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [Node.js 下载](https://nodejs.org/en/download)
