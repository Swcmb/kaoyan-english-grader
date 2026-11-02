<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Google Antigravity 安装指南

> 国内网络环境优先使用 Gitee 镜像安装标准 Skill：
>
> ```bash
> npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent antigravity
> ```
>
> 将 `AGENT_NAME` 替换为当前平台对应的 Agent 标识。下方的平台原生插件安装方式作为补充；需要 Gitee 国内源时，优先使用此方式。

本仓库包含 Antigravity 插件清单 .antigravity-plugin/plugin.json，以及标准 Agent Skill。

## 作为插件安装

~~~bash
agy plugin install https://github.com/Swcmb/kaoyan-english-grader
~~~

验证安装：

~~~bash
agy plugin list
~~~

安装前验证本地仓库：

~~~bash
agy plugin validate --strict ./kaoyan-english-grader
agy plugin install ./kaoyan-english-grader
~~~

## 作为独立 Skill 安装

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent antigravity
~~~

添加 -g 参数可安装到用户级目录。

## 验证

要求 Antigravity 批改一道具体题目，检查它是否读取中文题型规则。
