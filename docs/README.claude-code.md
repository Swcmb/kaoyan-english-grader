<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Claude Code 安装与使用

**推荐方式：从 Gitee 安装标准 Agent Skill。** 该方式保留主指令文件与六份题型规则的目录关系。

## 方式一：通过 Skills CLI 安装

要求 Node.js 22.20 或更高版本。在项目根目录打开终端，执行：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent claude-code
~~~

默认安装到当前项目的 Claude Code 技能目录。希望所有项目都能使用时，添加 -g：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent claude-code \
  -g
~~~

CLI 会提示选择复制或符号链接方式。多个 Agent 共用一份文件时，选择符号链接；需要独立管理时，选择复制。

## 方式二：手动安装

克隆仓库：

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
~~~

将整个技能目录复制到以下任一路径：

- 项目级：项目根目录/.claude/skills/kaoyan-english-grader/
- 用户级：~/.claude/skills/kaoyan-english-grader/

Windows 用户的用户级目录为 %USERPROFILE%/.claude/skills/kaoyan-english-grader/。

最终结构必须完整：

~~~text
kaoyan-english-grader/
├── SKILL.md
└── references/
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
~~~

## 验证

1. 打开或重新启动 Claude Code。
2. 输入 /skills，检查列表中是否出现 kaoyan-english-grader。
3. 输入 /kaoyan-english-grader，或直接要求批改英语一翻译。
4. 再测试英语二图表作文，确认 Agent 能读取相应的 references 规则。

若技能未出现，先检查 SKILL.md 是否位于技能目录根部，再开启新会话。

## 更新与卸载

Skills CLI 安装的技能可执行 npx skills update。手动安装时，用新版本完整替换目标目录。卸载时只删除 kaoyan-english-grader 文件夹，不要删除同级其他技能。

## 官方资料

- [Claude Code：Agent Skills 概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills CLI：命令说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
