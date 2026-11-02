<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Gemini CLI 安装与使用

Gemini CLI 支持标准 Agent Skills，可从用户目录、工作区目录和扩展中加载技能。

## 方式一：通过 Gitee 安装

在项目根目录打开终端：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent gemini-cli
~~~

默认安装到项目级 .agents/skills/。添加 -g 可安装到用户级目录：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent gemini-cli \
  -g
~~~

## 方式二：使用 Gemini CLI 原生命令

先将仓库克隆到本机：

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
~~~

安装到当前工作区：

~~~bash
gemini skills install ./skills/kaoyan-english-grader --scope workspace
~~~

安装到用户级目录：

~~~bash
gemini skills install ./skills/kaoyan-english-grader --scope user
~~~

检查安装：

~~~bash
gemini skills list
~~~

## 方式三：手动安装

复制完整技能目录到以下任一路径：

| 作用范围 | 路径 |
|---|---|
| 项目级通用目录 | .agents/skills/kaoyan-english-grader/ |
| 项目级 Gemini 目录 | .gemini/skills/kaoyan-english-grader/ |
| 用户级通用目录 | ~/.agents/skills/kaoyan-english-grader/ |
| 用户级 Gemini 目录 | ~/.gemini/skills/kaoyan-english-grader/ |

不要只复制 SKILL.md；六份题型规则必须保留在 references/ 子目录中。

## 验证与调用

1. 启动 Gemini CLI。
2. 输入 /skills 查看可调用技能。
3. 输入 /kaoyan-english-grader，或直接发出考研英语翻译/作文批改请求。
4. 测试英语一翻译和英语二大作文，确认对应规则文件可以读取。

如果安装后当前会话没有识别新技能，执行 /skills reload（当前版本支持时）或启动新会话。

## 更新与卸载

Skills CLI 安装：npx skills update。Gemini CLI 原生安装可执行 gemini skills uninstall kaoyan-english-grader --scope workspace，用户级安装将 scope 改为 user。手动安装：替换完整技能文件夹；卸载时删除上述目录中的 kaoyan-english-grader 子目录。

## 官方资料

- [Gemini CLI：Skills 命令与管理](https://geminicli.com/docs/cli/skills/)
- [Gemini CLI：Managing Agent Skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md)
- [Skills CLI：Gemini CLI 安装目录](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
