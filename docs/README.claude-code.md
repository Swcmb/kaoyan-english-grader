<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Claude Code 安装指南

> 国内网络环境优先使用 Gitee 镜像安装标准 Skill：
>
> ```bash
> npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent claude-code
> ```
>
> 将 `AGENT_NAME` 替换为当前平台对应的 Agent 标识。下方的平台原生插件安装方式作为补充；需要 Gitee 国内源时，优先使用此方式。

本仓库提供 Claude Code 插件入口，也提供可独立安装的标准 Agent Skill。

## 作为插件安装

在 Claude Code 中执行：

~~~text
/plugin marketplace add Swcmb/kaoyan-english-grader
/plugin install kaoyan-english-grader@kaoyan-english-grader
~~~

安装后重新启动 Claude Code 会话。

## 作为独立 Skill 安装

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent claude-code
~~~

默认安装到当前项目的技能目录。添加 -g 参数可安装到用户级目录。

## 验证

要求 Claude Code 批改一道英语一或英语二翻译/作文题，检查它是否读取对应题型规则并按中文要求输出。
