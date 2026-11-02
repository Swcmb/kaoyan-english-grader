<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Claude Code：安装与使用

Claude Code 支持标准 Agent Skills。项目级 Skill 随仓库共享，用户级 Skill 可在多个工作区复用。本指南介绍本机 Claude Code，不适用于 Claude 网页版或 Desktop 的 ZIP 上传流程。

## 安装方式

### 使用 Skills CLI

在目标项目根目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent claude-code
```

用户级安装增加 `-g`。选择复制或符号链接时，根据是否需要独立副本决定。

### 手动安装

将完整的 `skills/kaoyan-english-grader/` 复制到：

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.claude/skills/kaoyan-english-grader/` |
| 用户级 | `~/.claude/skills/kaoyan-english-grader/` |
| Windows 用户级 | `%USERPROFILE%/.claude/skills/kaoyan-english-grader/` |

安装目录必须同时包含 `SKILL.md` 和完整的 `references/`。

## 调用与验证

重新加载 Claude Code 或开启新会话，使用 `/skills` 查看技能，或输入 `/kaoyan-english-grader` 调用。分别提交英语一翻译和英语二图表作文，确认 Agent 读取对应规则并按题型评分。

技能未出现时，先检查目录深度、文件名和安装范围，再按当前版本要求重新加载。

## 更新与卸载

Skills CLI 安装可使用 `npx skills update kaoyan-english-grader`。手动安装时完整替换技能目录。卸载时只删除目标范围下的 `kaoyan-english-grader/`，保留其他技能。

## 参考资料

- [Claude Code：Agent Skills 概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills CLI：命令说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
