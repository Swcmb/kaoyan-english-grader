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

指定 `skills/kaoyan-english-grader` 子目录，避免把整个仓库作为 Skill 根目录。更新或卸载时确认作用范围，保留主文件和全部引用规则。

## 验收

检查 Agent 能发现并加载技能，再分别测试英语一翻译和英语二大作文，确认对应规则可读取、评分分值正确、输出结构完整。

## 本仓库的 Skill 版本选择

优先安装标准版 `skills/kaoyan-english-grader/`，并完整保留 `SKILL.md` 与 `references/` 六份规则。完整目录安装是按项目原始结构直接复用全部评分规则的标准方式。只有当平台无法保留引用目录、但支持单个标准 `SKILL.md` 导入时，才使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准 Skill 目录的平台也可以安装完整版，但不推荐用它替代标准版。

## 官方资料

- [Gemini CLI：Skills 命令与管理](https://geminicli.com/docs/cli/skills/)
- [Gemini CLI：Agent Skills 使用说明](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md)
- [Skills CLI：Agent 映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
