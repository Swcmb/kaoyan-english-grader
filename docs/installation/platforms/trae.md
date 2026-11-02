<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Trae / Trae CN：安装与使用

Trae 支持以 `SKILL.md` 定义技能，并提供 IDE 导入、技能市场以及全局/项目级管理。

## 安装与使用

### Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent trae-cn
```

### IDE 导入

1. 打开 Trae。
2. 进入 **设置 → 技能与命令**。
3. 在技能区域选择创建或导入本地技能。
4. 选择全局或项目范围。
5. 上传包含主文件和六份内嵌评分规则的完整包。
6. 保存后检查技能列表。

### 手动安装

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.trae/skills/kaoyan-english-grader/` |
| 用户级 macOS / Linux | `~/.trae-cn/skills/kaoyan-english-grader/` |
| 用户级 Windows | `%USERPROFILE%/.trae-cn/skills/kaoyan-english-grader/` |

## 能力边界

Trae、Trae CN、TraeCode 和 TraeWork 等产品线的菜单可能不同。导入后确认 `SKILL.md` 内容完整且 Agent 能正常调用；平台明确只接受单文件时，直接导入该文件。

## 验收

确认技能出现在目标产品的已安装列表，并分别测试英语一翻译和英语二大作文，核对对应规则、分值和输出要求。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [Trae：技能（Skill）](https://docs.trae.cn/ide_skills)
- [Skills CLI：Trae 路径映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
