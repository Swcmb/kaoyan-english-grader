<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 使用 Skills CLI 安装考研英语批改 Skill

[Vercel Skills CLI](https://github.com/vercel-labs/skills) 可从 Git 仓库、URL 或本地目录获取标准 Agent Skill，并安装到所选 Agent 的项目级或用户级目录。**本仓库默认安装标准版**，完整保留主文件和六份引用规则。

## 两个 Skill

| Skill | CLI 名称 | 安装对象 | 推荐用途 |
| --- | --- | --- | --- |
| 标准版 | `kaoyan-english-grader` | `skills/kaoyan-english-grader/` 完整目录 | 默认推荐，适用于支持标准 Skill 目录的平台 |
| 完整版 | `kaoyan-english-grader-full` | `skills/kaoyan-english-grader-full/SKILL.md` | 平台无法保留引用目录、只支持单文件导入时使用 |

完整版内嵌全部六类评分规则。支持标准 Skill 目录的平台也可安装完整版，但不推荐用它替代标准版。

## 环境要求

Skills CLI 当前文档要求 Node.js 22.20 或更高版本。还需要 Git 能访问所选仓库源，并且目标 Agent 在当前 CLI 支持清单中。

```bash
node --version
npm --version
git --version
```

## 安装标准版（推荐）

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

指定 Codex：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex
```

Agent ID 以当前官方清单为准：[Skills CLI Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

## 安装完整版

仅在平台不能完整保留标准版主文件与 `references/` 目录、但支持标准单文件 Skill 时使用：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader-full
```

该版本是独立 Skill，六类规则全部位于单个 `SKILL.md` 中。支持完整目录安装的平台应优先安装标准版。

## 项目级与用户级安装

项目级安装写入当前工作区，适合随项目共享。用户级安装适用于多个工作区，增加 `-g`：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent codex
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent codex -g
```

具体目录由 Agent ID 决定，以 CLI 当前目录映射为准。

## 从本地仓库安装

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
```

需要安装完整版时，将名称改为 `kaoyan-english-grader-full`。

## 安装结构与验证

标准版必须保留主文件和六份 `references/` 规则。完整版只有一个 `SKILL.md`，并在文件内部包含六个完整题型章节。安装后检查目标目录、文件完整性和 Agent 发现状态。分别提交英语一翻译和英语二大作文测试，确认对应规则读取正常。不要只凭 CLI 退出码判断安装成功。

## 查看、更新与卸载

```bash
npx skills list
npx skills check
npx skills update kaoyan-english-grader
npx skills remove kaoyan-english-grader
```

管理完整版时，将名称替换为 `kaoyan-english-grader-full`。执行卸载前确认工作区、安装范围与技能名称。CLI 命令和参数可能变化，遇到行为差异时以当前 `npx skills --help` 和[官方命令文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)为准。
