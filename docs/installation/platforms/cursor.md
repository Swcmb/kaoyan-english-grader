<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Cursor：安装与使用

Cursor 支持标准 Agent Skills，并提供项目级、用户级发现路径。Cloud Agents 的可见性还取决于 Skill 同步设置。

## 安装与使用

### Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent cursor
```

### 手动安装

| 范围 | 路径 |
| --- | --- |
| 项目级通用 | `.agents/skills/kaoyan-english-grader/` |
| 项目级 Cursor | `.cursor/skills/kaoyan-english-grader/` |
| 用户级通用 | `~/.agents/skills/kaoyan-english-grader/` |
| 用户级 Cursor | `~/.cursor/skills/kaoyan-english-grader/` |

将完整目录复制到目标路径，保持完整 Skill 文件的相对位置。

## 能力边界

本机用户级 Skill 是否同步到 Cloud Agents，取决于 Cursor 当前同步设置和账号能力。未同步的本机目录不会自动出现在远程 Agent 或自托管 Worker 中。

## 验收

检查技能是否出现在目标产品中，并分别测试英语一翻译和英语二大作文。核对题型路由、评分档位、内嵌评分规则和输出要求。上传或保存成功不能替代真实任务验证。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [Cursor：Agent Skills](https://cursor.com/docs/skills)
- [Cursor：个人 Skills 与 Cloud Agents](https://cursor.com/help/customization/skills)
- [Skills CLI：目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
