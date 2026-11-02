<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Claude Code：安装与使用

Claude Code 通过文件系统发现标准 Agent Skills。项目级目录可随仓库共享，用户级目录适合多个工作区。本指南不适用于 Claude 网页版或 Desktop 上传流程。

## 安装与使用

### Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent claude-code
```

### 手动安装

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.claude/skills/kaoyan-english-grader/` |
| 用户级 | `~/.claude/skills/kaoyan-english-grader/` |
| Windows 用户级 | `%USERPROFILE%/.claude/skills/kaoyan-english-grader/` |

将 `skills/kaoyan-english-grader/` 目录完整放入目标路径。该目录只包含完整的 `SKILL.md` 文件。

## 安装边界

Claude Code 本地目录和 Claude 网页版自定义 Skill 上传由不同界面与目录管理，不会自动同步。不要将网页 ZIP 上传流程作为 Claude Code 本地安装方式。

## 验收

检查技能是否出现在目标产品的技能列表，并分别提交英语一翻译和英语二大作文测试。确认题型路由、分值、对应规则和输出结构正确。上传成功或保存成功不能替代实际调用验证。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`，不依赖额外的规则文件或运行时服务。目录安装时导入 `skills/kaoyan-english-grader/`；平台明确只接受单文件时，导入该目录中的 `SKILL.md`。

## 官方资料

- [Claude Code：Agent Skills 概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills CLI：命令说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
