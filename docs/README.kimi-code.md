<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Kimi Code 安装指南

> 国内网络环境优先使用 Gitee 镜像安装标准 Skill：
>
> ```bash
> npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent kimi-code-cli
> ```
>
> 将 `AGENT_NAME` 替换为当前平台对应的 Agent 标识。下方的平台原生插件安装方式作为补充；需要 Gitee 国内源时，优先使用此方式。

本仓库提供 Kimi 原生插件清单 kimi.plugin.json，插件包含标准 Skill 及其题型规则文件。

## 从 GitHub 安装插件

在 Kimi Code 中执行：

~~~text
/plugins install https://github.com/Swcmb/kaoyan-english-grader
/reload
~~~

也可以在安装后开启新会话。安装完成后，技能会显示在插件命名空间下。

## 作为独立 Skill 安装

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent kimi-code-cli
~~~

添加 -g 参数可通过通用技能安装工具安装到用户级目录。

## 验证

使用技能选择器，或直接要求 Kimi Code 批改一道英语一/英语二翻译或作文题。确认已加载的 Skill 能读取相邻的 references 目录。
