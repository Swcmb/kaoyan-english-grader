<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# OpenCode 安装指南

> 国内网络环境优先使用 Gitee 镜像安装标准 Skill：
>
> ```bash
> npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent opencode
> ```
>
> 将 `AGENT_NAME` 替换为当前平台对应的 Agent 标识。下方的平台原生插件安装方式作为补充；需要 Gitee 国内源时，优先使用此方式。

OpenCode 原生支持 Agent Skills 格式。它可以从项目级 .agents/skills/、.opencode/skills/，以及用户级 ~/.agents/skills/、~/.config/opencode/skills/ 目录发现技能。

## 推荐安装方式

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent opencode
~~~

添加 -g 参数可安装到用户级目录。

## 手动安装

将完整技能目录（包括 references 文件夹）复制到以下任一位置：

- 项目级：.agents/skills/kaoyan-english-grader/
- 项目原生目录：.opencode/skills/kaoyan-english-grader/
- 用户级：~/.config/opencode/skills/kaoyan-english-grader/
- 通用用户级：~/.agents/skills/kaoyan-english-grader/

请确保 SKILL.md 与 references/ 位于同一技能目录结构中。

## 验证

在 OpenCode 中请求批改英语一或英语二题目，确认技能已加载且能读取对应规则。
