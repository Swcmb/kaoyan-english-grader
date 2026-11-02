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

复制完整目录并保持主文件和 `references/` 的相对位置。

## 能力边界

同名技能在专属目录与通用目录中的优先级以当前 Qwen Code 文档为准。技能未出现时检查目录深度，正确结构是“技能目录/`SKILL.md`”。

## 验收

确认技能出现在目标产品的已安装列表，并分别测试英语一翻译和英语二大作文，核对对应规则、分值和输出要求。

## 本仓库的 Skill 版本选择

优先安装标准版 `skills/kaoyan-english-grader/`，并完整保留 `SKILL.md` 与 `references/` 六份规则。完整目录安装是按项目原始结构直接复用全部评分规则的标准方式。只有当平台无法保留引用目录、但支持单个标准 `SKILL.md` 导入时，才使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准 Skill 目录的平台也可以安装完整版，但不推荐用它替代标准版。

## 官方资料

- [Qwen Code：Agent Skills](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/)
- [Skills CLI：Agent 映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
