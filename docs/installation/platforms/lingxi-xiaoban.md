<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# 灵犀·晓伴：工具与技能中心

灵犀·晓伴的应用商店介绍包含 AI 工具与技能中心、第三方技能扩展、专属智能体和自动化任务能力。

## 安装与使用

1. 从官方渠道或应用商店安装并登录。
2. 打开主页或工具入口中的 **AI 工具与技能中心**。
3. 浏览分类并搜索所需技能。
4. 查看用途、提供方、授权和使用条件。
5. 按页面提示添加或启用，再到对话或智能体场景测试。

需要自定义流程时，可查看 AI 创作或智能体专区，按产品提供的选项配置角色、目标和能力。

## 能力边界

公开应用商店信息确认第三方技能扩展，但没有提供标准 Agent Skill 的 `SKILL.md`、ZIP 或 TAR.GZ 导入步骤。本指南记录应用内技能中心，不将其描述为标准文件导入。

## 验收

检查 Agent 能发现并加载技能，再分别测试英语一翻译和英语二大作文，确认对应规则可读取、评分分值正确、输出结构完整。

## 本仓库的 Skill 版本选择

技能市场只安装平台实际上架的条目；只有能够核验本项目的发布者和来源时，才能称为安装了本项目。应用内创建生成平台内部 Skill，需要将六类评分规则迁移并逐项核对，不能视为标准文件导入。若当前版本明确支持标准 Skill 目录或完整 ZIP，优先安装标准版；若只能导入单个标准 `SKILL.md`，使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准目录的平台也可安装完整版，但不推荐替代标准版。

## 官方资料

- [灵犀·晓伴：小米应用商店](https://app.mi.com/details?id=com.lxxb)
- [灵犀·晓伴：App Store](https://apps.apple.com/cn/app/%E7%81%B5%E7%8A%80-%E6%99%93%E4%BC%B4/id6766031151)
