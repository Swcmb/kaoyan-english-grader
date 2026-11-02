<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Google Antigravity：安装与使用

Antigravity 支持 Agent Skills，并提供 IDE、CLI 和插件工作流。标准 Skill 与插件清单是不同安装对象。

## 安装与使用

### Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent antigravity
```

### 手动安装

将完整的 `skills/kaoyan-english-grader/` 复制到以下路径之一：

| 范围 | 路径 |
| --- | --- |
| 项目级通用 | `.agents/skills/kaoyan-english-grader/` |
| 用户级 Antigravity | `~/.gemini/antigravity/skills/kaoyan-english-grader/` |
| Antigravity CLI 用户级 | `~/.gemini/antigravity-cli/skills/kaoyan-english-grader/` |

### 插件安装

```bash
agy plugin install https://github.com/Swcmb/kaoyan-english-grader
agy plugin list
agy plugin validate --strict ./kaoyan-english-grader
```

## 安装边界

Skills CLI 安装标准目录；`agy plugin` 安装插件。App/IDE 与 CLI 目录可能不同，按当前文档确认发现路径。插件成功安装不自动证明标准 Skill 的引用规则可用。

## 验收

检查技能是否出现在目标产品的技能列表，并分别提交英语一翻译和英语二大作文测试。确认题型路由、分值、对应规则和输出结构正确。上传成功或保存成功不能替代实际调用验证。

## 本仓库的 Skill 版本选择

优先安装标准版 `skills/kaoyan-english-grader/`，并完整保留 `SKILL.md` 与 `references/` 六份规则。完整目录安装是按项目原始结构直接复用全部评分规则的标准方式。只有当平台无法保留引用目录、但支持单个标准 `SKILL.md` 导入时，才使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准 Skill 目录的平台也可以安装完整版，但不推荐用它替代标准版。

## 官方资料

- [Google Antigravity：Agent Skills](https://antigravity.google/docs/skills?app=antigravity)
- [Google Antigravity：Plugins](https://www.antigravity.google/docs/plugins)
- [Skills CLI：Agent 路径映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
