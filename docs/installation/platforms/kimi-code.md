<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Kimi Code CLI：安装与使用

Kimi Code CLI 支持标准 Agent Skills，也提供插件系统。标准目录版和 Kimi 插件是两个独立安装对象。

## 安装与使用

### 安装标准 Skill

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent kimi-code-cli
```

### 手动安装路径

| 范围 | Kimi 专属目录 | 通用目录 |
| --- | --- | --- |
| 用户级 | `~/.kimi-code/skills/kaoyan-english-grader/` | `~/.agents/skills/kaoyan-english-grader/` |
| 项目级 | `.kimi-code/skills/kaoyan-english-grader/` | `.agents/skills/kaoyan-english-grader/` |

默认 `KIMI_CODE_HOME` 为 `~/.kimi-code`，修改该变量会影响 Kimi 专属目录。

### 插件安装

```text
/plugins install https://github.com/Swcmb/kaoyan-english-grader
/plugins list
/reload
```

## 能力边界

插件和标准 Skill 的安装范围、更新方式不同。使用 Gitee 源安装标准 Skill 时使用 Skills CLI；安装插件时另行检查插件是否包含完整批改规则。

## 验收

检查 Agent 能发现并加载技能，再分别测试英语一翻译和英语二大作文，确认对应规则可读取、评分分值正确、输出结构完整。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [Kimi Code：Using Skills](https://www.kimi.ai/help/plugins-and-skills/use-skills-in-code)
- [Kimi Code：Plugins 命令](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/plugins.html)
- [Skills CLI：Agent 映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
