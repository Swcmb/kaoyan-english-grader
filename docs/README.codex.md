<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# OpenAI Codex 安装与使用

Codex 原生发现 Agent Skills。项目级技能适合与仓库一起提交；用户级技能适合在所有项目中复用。

## 方式一：通过 Gitee 安装

在项目根目录打开 Codex 终端，执行：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex
~~~

默认安装到当前项目的 .agents/skills/。添加 -g 可安装到用户级 ~/.agents/skills/：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex \
  -g
~~~

## 方式二：手动安装

克隆仓库：

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
~~~

将完整技能目录复制到目标路径：

- 项目级：项目根目录/.agents/skills/kaoyan-english-grader/
- 用户级：~/.agents/skills/kaoyan-english-grader/

Windows 用户的用户级目录对应 %USERPROFILE%/.agents/skills/kaoyan-english-grader/。

目录中必须同时有 SKILL.md 和 references/。不要只复制主文件。

## 方式三：让 Codex 下载并安装

在 Codex 对话中请求：

~~~text
请从以下 Git 仓库安装考研英语批改 Skill：
https://gitee.com/ianwusb/kaoyan-english-grader.git

只安装 kaoyan-english-grader，并保留其 references 子目录。
~~~

Codex 的下载能力受当前网络和运行环境权限影响。执行后检查实际写入目录，不要仅凭回复判断安装成功。

## 验证

1. 在 Codex 中开启新会话。
2. 输入 /skills 或询问当前可用的 Skills。
3. 调用 $kaoyan-english-grader，或描述一项考研英语批改任务。
4. 分别测试英语一翻译与英语二大作文，确认两类任务使用对应分值和规则。

## 更新与卸载

CLI 安装的技能可使用 npx skills update 更新。手动安装时，用新版本完整覆盖目标目录。删除项目级目录会影响使用该仓库的团队成员；删除用户级目录只影响当前用户。

## 官方资料

- [Codex：构建 Skills](https://learn.chatgpt.com/docs/build-skills)
- [Skills CLI：支持 Agent 与安装目录](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
