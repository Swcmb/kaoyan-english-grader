<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Claude Code：安装与使用

Claude Code 支持标准 Agent Skills。项目级 Skill 随仓库共享；用户级 Skill 可在多个工作区复用。国内网络优先使用 Gitee。

## 通过 Skills CLI 安装

要求 Node.js 22.20 或更高版本。在目标项目根目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent claude-code
```

用户级安装增加 `-g`。按提示选择复制或符号链接：复制适合独立管理，符号链接适合多个 Agent 共用一份源文件。

## 手动安装

将完整的 `skills/kaoyan-english-grader/` 复制到：

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.claude/skills/kaoyan-english-grader/` |
| 用户级 | `~/.claude/skills/kaoyan-english-grader/` |
| Windows 用户级 | `%USERPROFILE%/.claude/skills/kaoyan-english-grader/` |

目录必须包含 `SKILL.md` 和完整 `references/`。

## 调用与验证

1. 打开或重新加载 Claude Code。
2. 使用 `/skills` 查看技能。
3. 调用 `/kaoyan-english-grader`，或直接提出批改任务。
4. 分别测试英语一翻译和英语二图表作文，核对分值与规则引用。

技能未出现时，检查目录深度和文件名，再开启新会话。

## 更新与卸载

Skills CLI 安装使用 `npx skills update`。手动安装时完整替换技能目录。卸载只删除 `kaoyan-english-grader/`。

## 官方资料

- [Claude Code：Agent Skills 概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills CLI：命令说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
