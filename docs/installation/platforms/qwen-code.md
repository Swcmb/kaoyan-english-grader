<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Qwen Code：安装与使用

Qwen Code 支持 Agent Skills，可从项目和用户目录发现技能。本指南对应 Qwen Code，不涉及千问手机 App 或 QwenWork。

## 安装与使用

### Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent qwen-code
```

### 手动安装

| 范围 | Qwen 专属目录 | 通用目录 |
| --- | --- | --- |
| 项目级 | `.qwen/skills/kaoyan-english-grader/` | `.agents/skills/kaoyan-english-grader/` |
| 用户级 | `~/.qwen/skills/kaoyan-english-grader/` | `~/.agents/skills/kaoyan-english-grader/` |

复制完整目录并保持主文件和 `外部规则文件` 的相对位置。

## 能力边界

同名技能在专属目录与通用目录中的优先级以当前 Qwen Code 文档为准。技能未出现时检查目录深度，正确结构是“技能目录/`SKILL.md`”。

## 验收

确认技能出现在目标产品的已安装列表，并分别测试英语一翻译和英语二大作文，核对对应规则、分值和输出要求。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [Qwen Code：Agent Skills](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/)
- [Skills CLI：Agent 映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
