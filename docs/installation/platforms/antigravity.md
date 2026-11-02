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

Skills CLI 安装标准目录；`agy plugin` 安装插件。App/IDE 与 CLI 目录可能不同，按当前文档确认发现路径。插件成功安装不自动证明标准 Skill 的内嵌评分规则可用。

## 验收

检查技能是否出现在目标产品的技能列表，并分别提交英语一翻译和英语二大作文测试。确认题型路由、分值、对应规则和输出结构正确。上传成功或保存成功不能替代实际调用验证。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`，不依赖 `（外部规则目录）` 或其他外部文件。目录安装时导入 `skills/kaoyan-english-grader/`；平台明确只接受单文件时，导入该目录中的 `SKILL.md`。

## 官方资料

- [Google Antigravity：Agent Skills](https://antigravity.google/docs/skills?app=antigravity)
- [Google Antigravity：Plugins](https://www.antigravity.google/docs/plugins)
- [Skills CLI：Agent 路径映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
