<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# OpenCode 安装与使用

OpenCode 原生发现 Agent Skills。每个 Skill 应放在独立目录中，主文件名为 SKILL.md。

## 方式一：通过 Gitee 安装

进入项目目录，执行：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent opencode
~~~

默认安装到项目级目录。添加 -g 可安装到用户级目录：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent opencode \
  -g
~~~

## 方式二：手动安装

复制完整目录到以下任一位置：

| 作用范围 | 路径 |
|---|---|
| 项目级 OpenCode 目录 | .opencode/skills/kaoyan-english-grader/ |
| 项目级通用目录 | .agents/skills/kaoyan-english-grader/ |
| 用户级 OpenCode 目录 | ~/.config/opencode/skills/kaoyan-english-grader/ |
| 用户级通用目录 | ~/.agents/skills/kaoyan-english-grader/ |

OpenCode 也兼容 Claude Code 的 .claude/skills/ 路径。对本仓库建议优先使用 .opencode/skills/ 或 .agents/skills/。

## 验证与调用

1. 重新打开 OpenCode 会话。
2. 在提示词中输入 /kaoyan-english-grader，或直接请求考研英语作文/翻译批改。
3. 检查 Agent 是否读取 references/english1_essay_major.md 等题型规则。
4. 分别测试英语一翻译与英语二图表作文，确认使用对应评分规则。

OpenCode 按需加载技能：Agent 先读取技能名称和描述，任务匹配时再读取完整指令与引用文件。

## 更新与卸载

CLI 更新：npx skills update。手动安装时替换整个 Skill 目录。卸载时删除对应作用范围下的 kaoyan-english-grader 文件夹。

## 官方资料

- [OpenCode：Agent Skills](https://opencode.ai/docs/skills)
- [Skills CLI：安装与更新命令](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
