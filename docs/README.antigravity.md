<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Google Antigravity 安装指南

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
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent antigravity
~~~

添加 -g 参数可安装到用户级目录。

## 验证

要求 Antigravity 批改一道具体题目，检查它是否读取中文题型规则。
