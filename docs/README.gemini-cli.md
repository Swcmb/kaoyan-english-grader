<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Gemini CLI 与 Qwen Code 安装指南

> 国内网络环境优先使用 Gitee 镜像安装标准 Skill：
>
> ```bash
> npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent gemini-cli
> ```
>
> 将 `AGENT_NAME` 替换为当前平台对应的 Agent 标识。下方的平台原生插件安装方式作为补充；需要 Gitee 国内源时，优先使用此方式。

仓库包含 Gemini CLI 扩展清单，以及用于加载标准 Skill 的 GEMINI.md 入口文件。

## Gemini CLI

从 GitHub 安装：

~~~bash
gemini extensions install https://github.com/Swcmb/kaoyan-english-grader
~~~

安装后重新启动 Gemini CLI。更新扩展：

~~~bash
gemini extensions update
~~~

查看已安装扩展：

~~~text
/extensions list
~~~

## Qwen Code

通过扩展命令安装：

~~~bash
qwen extensions install Swcmb/kaoyan-english-grader
~~~

安装后重新启动 Qwen Code。可使用其扩展管理命令查看已安装扩展。

## 作为独立 Skill 安装

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader --agent gemini-cli
~~~

## 验证

要求 Agent 批改一道具体题目，检查它是否读取对应的中文题型规则。
