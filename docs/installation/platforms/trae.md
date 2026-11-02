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
5. 上传包含主文件和六份引用规则的完整包。
6. 保存后检查技能列表。

### 手动安装

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.trae/skills/kaoyan-english-grader/` |
| 用户级 macOS / Linux | `~/.trae-cn/skills/kaoyan-english-grader/` |
| 用户级 Windows | `%USERPROFILE%/.trae-cn/skills/kaoyan-english-grader/` |

## 能力边界

Trae、Trae CN、TraeCode 和 TraeWork 等产品线的菜单可能不同。导入后检查 `references/` 是否完整保留；只接受单文件时使用完整单文件版本。

## 验收

确认技能出现在目标产品的已安装列表，并分别测试英语一翻译和英语二大作文，核对对应规则、分值和输出要求。

## 官方资料

- [Trae：技能（Skill）](https://docs.trae.cn/ide_skills)
- [Skills CLI：Trae 路径映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
