<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# OpenCode：安装与使用

OpenCode 原生发现 Agent Skills。每个技能使用独立目录，目录根部包含 `SKILL.md`。本项目的六类题型评分规则全部内嵌在该文件中。

## 安装与使用

### 使用 Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent opencode
```

### 手动安装

| 范围 | 路径 |
| --- | --- |
| 项目级 OpenCode | `.opencode/skills/kaoyan-english-grader/` |
| 项目级通用 | `.agents/skills/kaoyan-english-grader/` |
| 用户级 OpenCode | `~/.config/opencode/skills/kaoyan-english-grader/` |
| 用户级通用 | `~/.agents/skills/kaoyan-english-grader/` |

## 能力边界

OpenCode 按需加载技能。本项目的 `SKILL.md` 自包含，不需要加载其他规则文件；安装后测试英语一翻译和英语二图表作文，确认对应规则可读取。

## 验收

检查 Agent 能发现并加载技能，再分别测试英语一翻译和英语二大作文，确认对应规则可读取、评分分值正确、输出结构完整。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [OpenCode：Agent Skills](https://opencode.ai/docs/skills)
- [Skills CLI：命令说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
