<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# WorkBuddy 微信小程序：安装与调用 Skill

WorkBuddy 小程序提供 SkillHub 指令安装和对话内添加技能。手机文件附件属于任务资料输入，不代表标准 Skill 导入。

## 安装与使用

### 从 SkillHub 获取技能

1. 在微信中打开 WorkBuddy 小程序并登录。
2. 在 SkillHub 查找目标技能。
3. 查看技能详情、发布者和来源，复制安装指令。
4. 返回目标对话并发送指令。
5. 等待安装完成，在技能列表确认可用。

### 为当前对话添加技能

1. 打开目标对话。
2. 点击输入栏左侧的 **+**。
3. 在工具面板选择 **添加技能（Skills）**。
4. 选择技能后返回对话继续输入任务。

## 能力边界

小程序附件面板支持添加文件和文档，但附件上传不等于技能安装。公开流程确认 SkillHub 指令安装和对话添加，尚未确认手机端支持导入任意标准 `SKILL.md` 文件夹或 ZIP。没有市场条目时，可在支持本地导入的桌面端安装完整版本。

## 验收

检查技能状态，并分别测试英语一翻译和英语二大作文，确认完整规则、题型路由与模拟分值可用。

## 本仓库的 Skill 版本选择

技能市场只安装平台实际上架的条目；只有能够核验本项目的发布者和来源时，才能称为安装了本项目。应用内创建生成平台内部 Skill，需要将六类评分规则迁移并逐项核对，不能视为标准文件导入。若当前版本明确支持标准 Skill 目录或完整 ZIP，优先安装标准版；若只能导入单个标准 `SKILL.md`，使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准目录的平台也可安装完整版，但不推荐替代标准版。

## 官方资料

- [WorkBuddy 小程序：添加附件与技能](https://www.codebuddy.cn/docs/workbuddymini/features/Attachments-and-Skills)
- [WorkBuddy 小程序：快速开始](https://www.codebuddy.cn/docs/workbuddymini/quick-start/Overview)
- [WorkBuddy Enterprise：技能管理](https://cloud.tencent.com/document/product/1831/134432)
