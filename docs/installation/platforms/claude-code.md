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

将完整目录放入目标路径，保留 `SKILL.md` 和 `references/`。

## 安装边界

Claude Code 本地目录和 Claude 网页版自定义 Skill 上传由不同界面与目录管理，不会自动同步。不要将网页 ZIP 上传流程作为 Claude Code 本地安装方式。

## 验收

检查技能是否出现在目标产品的技能列表，并分别提交英语一翻译和英语二大作文测试。确认题型路由、分值、对应规则和输出结构正确。上传成功或保存成功不能替代实际调用验证。

## 本仓库的 Skill 版本选择

优先安装标准版 `skills/kaoyan-english-grader/`，并完整保留 `SKILL.md` 与 `references/` 六份规则。完整目录安装是按项目原始结构直接复用全部评分规则的标准方式。只有当平台无法保留引用目录、但支持单个标准 `SKILL.md` 导入时，才使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准 Skill 目录的平台也可以安装完整版，但不推荐用它替代标准版。

## 官方资料

- [Claude Code：Agent Skills 概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills CLI：命令说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
