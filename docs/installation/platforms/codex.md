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

不要只复制 `SKILL.md`；`references/` 六份规则属于目录版的完整内容。Codex 插件与本项目独立 Skill 是不同安装对象。

## 验收

检查技能是否出现在目标产品中，并分别测试英语一翻译和英语二大作文。核对题型路由、评分档位、引用规则和输出要求。上传或保存成功不能替代真实任务验证。

## 本仓库的 Skill 版本选择

优先安装标准版 `skills/kaoyan-english-grader/`，并完整保留 `SKILL.md` 与 `references/` 六份规则。完整目录安装是按项目原始结构直接复用全部评分规则的标准方式。只有当平台无法保留引用目录、但支持单个标准 `SKILL.md` 导入时，才使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准 Skill 目录的平台也可以安装完整版，但不推荐用它替代标准版。

## 官方资料

- [Codex：构建 Skills](https://learn.chatgpt.com/docs/build-skills)
- [Skills CLI：Agent 路径映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
