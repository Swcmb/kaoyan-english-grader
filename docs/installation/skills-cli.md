<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 使用 Skills CLI 安装

[Skills CLI](https://github.com/vercel-labs/skills) 可以从 Git 仓库或本地目录安装标准 Agent Skill，并按目标 Agent 配置项目级或用户级发现路径。本仓库建议使用 Gitee 镜像，GitHub 为备用来源。

## 环境准备

当前 CLI 文档要求 Node.js 22.20 或更高版本，并需要 npm/npx 与 Git。

```bash
node --version
npm --version
git --version
```

确认 Node.js 满足 CLI 当前要求，且网络能够访问所选 Git 源。

## 交互式安装

在目标项目目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

按提示选择 Agent、安装范围和文件管理方式。需要独立副本时选择复制；多个 Agent 共用源目录且宿主支持符号链接时，可选择链接。

## 指定 Agent

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex
```

多个 Agent 可按 CLI 当前参数格式传入：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent claude-code codex cursor opencode
```

Agent ID 和目录映射可能变化。执行前查看[官方 Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)，不要根据产品名称猜测 ID。

## 项目级与用户级安装

项目级安装写入当前工作区，适合随项目共享；用户级安装增加 `-g`：

```bash
# 项目级
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex

# 用户级
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex -g
```

最终目录由 Agent ID 与 CLI 版本决定，以安装输出和当前映射文档为准。

## 从本地仓库安装

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
```

GitHub 备用源：

```bash
git clone https://github.com/Swcmb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
```

## 安装结构与验证

CLI 安装标准目录版，目标目录应包含：

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

检查目录结构和文件可读性，再分别提交英语一翻译与英语二大作文测试题，确认规则路由正确。CLI 成功提示不能替代实际使用验证。

## 查看、更新和卸载

```bash
npx skills list
npx skills check
npx skills update kaoyan-english-grader
npx skills remove kaoyan-english-grader
```

更新和卸载前确认技能名称、工作区与安装范围。命令行为变化时运行 `npx skills --help`，并查看[官方命令文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。

## 官方资料

- [Skills CLI 项目与环境要求](https://github.com/vercel-labs/skills)
- [命令参考](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Agent ID 与目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [Node.js 下载](https://nodejs.org/en/download)
