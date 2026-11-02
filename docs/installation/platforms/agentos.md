<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# AgentOS（艾嘿）：技能商店

AgentOS 的公开应用商店介绍和版本记录包含技能商店。本页记录市场安装，不把市场入口等同于标准 Agent Skill 文件导入。

## 安装与使用

1. 从 [Apple App Store 加拿大区](https://apps.apple.com/ca/app/agentos/id6759725374) 或[智利区](https://apps.apple.com/cl/app/agentos/id6759725374)查看当前应用信息，核对开发者后安装。
2. 登录并完成首次启动。
3. 打开技能商店，浏览分类或搜索技能。
4. 查看介绍、来源和权限，再按页面提示安装。
5. 在已安装列表检查状态并测试调用。

## 安装边界

公开资料提及自定义安装能力，但标准 `SKILL.md`、文件夹 ZIP 和引用目录协议尚未确认。只有当前版本明确支持完整目录导入且保留全部引用规则时，才能认定为标准 Skill 导入。

## 验收

检查技能是否出现在目标产品的技能列表，并分别提交英语一翻译和英语二大作文测试。确认题型路由、分值、对应规则和输出结构正确。上传成功或保存成功不能替代实际调用验证。

## 本仓库的 Skill 版本选择

技能市场只安装平台实际上架的条目；只有能够核验本项目的发布者和来源时，才能称为安装了本项目。应用内创建生成平台内部 Skill，需要将六类评分规则迁移并逐项核对，不能视为标准文件导入。若当前版本明确支持标准 Skill 目录或完整 ZIP，优先安装标准版；若只能导入单个标准 `SKILL.md`，使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准目录的平台也可安装完整版，但不推荐替代标准版。

## 官方资料

- [AgentOS：加拿大区 App Store](https://apps.apple.com/ca/app/agentos/id6759725374)
- [AgentOS：智利区 App Store](https://apps.apple.com/cl/app/agentos/id6759725374)
