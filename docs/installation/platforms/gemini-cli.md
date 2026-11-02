<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Gemini CLI：安装与使用

Gemini CLI 支持标准 Agent Skills，可从仓库或本地目录安装，并区分 user 与 workspace 作用范围。本指南只适用于 Gemini CLI。

## 安装与使用

### 使用 Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent gemini-cli
```

### 使用原生命令

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader

# 项目级安装
gemini skills install ./skills/kaoyan-english-grader --scope workspace

# 用户级安装
gemini skills install ./skills/kaoyan-english-grader --scope user

# 查看技能
gemini skills list
```

按需使用 `/skills reload` 重新扫描当前技能。

## 能力边界

指定 `skills/kaoyan-english-grader` 子目录，避免把整个仓库作为 Skill 根目录。更新或卸载时确认作用范围，确保 `SKILL.md` 文件内容完整。

## 验收

检查 Agent 能发现并加载技能，再分别测试英语一翻译和英语二大作文，确认对应规则可读取、评分分值正确、输出结构完整。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [Gemini CLI：Skills 命令与管理](https://geminicli.com/docs/cli/skills/)
- [Gemini CLI：Agent Skills 使用说明](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md)
- [Skills CLI：Agent 映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
