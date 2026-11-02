<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# OpenCode：安装与使用

OpenCode 原生发现 Agent Skills。每个技能使用独立目录，并在目录根部提供 `SKILL.md`。

## 通过 Skills CLI 安装

在目标项目目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent opencode
```

用户级安装增加 `-g`。

## 手动安装

将完整技能目录放在以下发现路径之一：

| 范围 | 路径 |
| --- | --- |
| 项目级 OpenCode | `.opencode/skills/kaoyan-english-grader/` |
| 项目级通用 | `.agents/skills/kaoyan-english-grader/` |
| 用户级 OpenCode | `~/.config/opencode/skills/kaoyan-english-grader/` |
| 用户级通用 | `~/.agents/skills/kaoyan-english-grader/` |

OpenCode 也兼容 Claude Code 的 `.claude/skills/` 路径。本仓库优先使用 `.opencode/skills/` 或 `.agents/skills/`。

## 调用与验证

开启新会话后输入 `/kaoyan-english-grader`，或直接提交考研英语批改任务。检查 Agent 是否读取所需 `references/` 文件，并分别测试英语一翻译和英语二图表作文。

OpenCode 按需加载技能：先读取名称和描述，任务匹配时再读取完整指令与引用文件。

## 更新与卸载

Skills CLI 安装使用 `npx skills update`。手动安装时替换完整技能目录；卸载时只删除目标范围下的 `kaoyan-english-grader/`。

## 官方文档与参考资料

- [OpenCode：Agent Skills](https://opencode.ai/docs/skills)
- [Skills CLI：安装与更新命令](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
