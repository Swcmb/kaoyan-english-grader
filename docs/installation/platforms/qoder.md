<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Qoder：安装与使用

Qoder IDE 与 Qoder CLI 支持标准 Agent Skills。可通过 Skills CLI、IDE 上传或手动放置目录安装。

## 安装与使用

### Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent qoder
```

### IDE 上传

1. 打开 Qoder IDE。
2. 进入 **Extensions → Skills**。
3. 选择 **Add Skills → Upload Skill**。
4. 上传包含完整 Skill 目录的 ZIP。
5. 在 Installed 列表检查状态。

ZIP 结构：

```text
kaoyan-english-grader/
├── SKILL.md
└── 外部规则文件
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
```

### 手动安装

| 范围 | 路径 |
| --- | --- |
| 用户级 | `~/.qoder/skills/kaoyan-english-grader/` |
| 项目级 | `.qoder/skills/kaoyan-english-grader/` |
| 用户级通用 | `~/.agents/skills/kaoyan-english-grader/` |

## 能力边界

IDE 和 CLI 的重新加载方式可能不同，按当前客户端处理。导入后检查主文件与六份引用文件均可读取；只看到 Installed 状态还不够。

## 验收

确认技能出现在目标产品的已安装列表，并分别测试英语一翻译和英语二大作文，核对对应规则、分值和输出要求。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [Qoder IDE：Skills](https://docs.qoder.com/extensions/skills)
- [Qoder CLI：Skills](https://docs.qoder.com/cli/Skills)
- [Skills CLI：Agent 映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
