<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# OpenAI Codex：安装与使用

Codex 支持标准 Agent Skills。项目级目录可随仓库共享，用户级目录可跨工作区使用。

## 安装与使用

### Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex
```

### 手动安装

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.agents/skills/kaoyan-english-grader/` |
| 用户级 | `~/.agents/skills/kaoyan-english-grader/` |
| Windows 用户级 | `%USERPROFILE%/.agents/skills/kaoyan-english-grader/` |

也可以在 Codex 对话中要求它从仓库获取 Skill，并检查文件实际路径。

## 能力边界

不要只复制 `SKILL.md`；内嵌的六类评分规则属于目录版的完整内容。Codex 插件与本项目独立 Skill 是不同安装对象。

## 验收

检查技能是否出现在目标产品中，并分别测试英语一翻译和英语二大作文。核对题型路由、评分档位、内嵌评分规则和输出要求。上传或保存成功不能替代真实任务验证。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`，不依赖 `（外部规则目录）` 或其他外部文件。目录安装时导入 `skills/kaoyan-english-grader/`；平台明确只接受单文件时，导入该目录中的 `SKILL.md`。

## 官方资料

- [Codex：构建 Skills](https://learn.chatgpt.com/docs/build-skills)
- [Skills CLI：Agent 路径映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
