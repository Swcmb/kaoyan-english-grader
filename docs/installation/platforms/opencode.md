<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# OpenCode：安装与使用

OpenCode 原生发现 Agent Skills。每个技能使用独立目录，目录根部包含 `SKILL.md`；本项目引用规则应与主文件一并安装。

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

OpenCode 按需加载技能。主文件中的相对引用必须指向实际存在的文件；安装后测试英语一翻译和英语二图表作文，确认对应规则可读取。

## 验收

检查 Agent 能发现并加载技能，再分别测试英语一翻译和英语二大作文，确认对应规则可读取、评分分值正确、输出结构完整。

## 官方资料

- [OpenCode：Agent Skills](https://opencode.ai/docs/skills)
- [Skills CLI：命令说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
