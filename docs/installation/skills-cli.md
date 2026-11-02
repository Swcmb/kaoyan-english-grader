<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 使用 Skills CLI 安装

[Vercel Skills CLI](https://github.com/vercel-labs/skills) 可以从 Git 仓库、URL 或本地目录发现标准 Agent Skill，并安装到受支持 Agent 的项目级或用户级目录。

本仓库只有一个 Skill：`kaoyan-english-grader`。全部六类评分规则内嵌于 `skills/kaoyan-english-grader/SKILL.md`，该文件可独立完成全部批改任务。

## 环境准备

检查 Node.js、npm 和 Git 是否可用：

~~~bash
node --version
npm --version
git --version
~~~

Skills CLI 的运行时要求、Agent ID 和参数可能随版本变化。安装前查看当前 CLI 帮助和[官方 Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

## 从 Gitee 安装

默认安装到当前项目：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
~~~

指定 Codex：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex
~~~

使用 GitHub 源：

~~~bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
~~~

Agent ID 以 CLI 当前版本的官方清单为准。

## 项目级与用户级安装

项目级安装写入当前工作区，适合随项目共享。用户级安装适用于多个工作区，按 CLI 当前版本增加 `-g`：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex -g
~~~

具体安装目录由 Agent ID 和 CLI 的路径映射决定。

## 从本地仓库安装

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
~~~

如果仓库已经存在，可在仓库根目录直接执行最后一条命令。

## 安装结构与验证

Skill 目录只包含一个主文件：

~~~text
kaoyan-english-grader/
└── SKILL.md
~~~

安装后检查目标目录、文件内容和 Agent 发现状态。分别提交英语一翻译和英语二大作文测试，确认题型路由、满分、评分依据和输出结构正常。不要只凭 CLI 退出码判断安装成功。

## 查看、更新与卸载

~~~bash
npx skills list
npx skills check
npx skills update kaoyan-english-grader
npx skills remove kaoyan-english-grader
~~~

执行更新或卸载前确认工作区、安装范围与技能名称。CLI 命令和参数可能变化，遇到行为差异时以当前 `npx skills --help` 和[官方命令文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)为准。
