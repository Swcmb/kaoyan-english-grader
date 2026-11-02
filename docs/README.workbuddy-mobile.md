<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# WorkBuddy 微信小程序：安装与调用 Skill

WorkBuddy 手机端通过微信小程序使用。公开文档说明，用户可以从 SkillHub 获取技能安装指令，再在对话中添加技能。

## 从 SkillHub 获取技能

1. 在微信中打开 WorkBuddy 小程序并登录。
2. 在 SkillHub 页面查找目标技能。
3. 打开详情，复制页面提供的安装指令。
4. 回到 WorkBuddy 小程序。
5. 将指令粘贴到对话框并发送。
6. 等待安装完成，再从添加技能列表确认技能可用。

执行前检查发布者、来源和命令内容，不要运行来源不明的安装指令。

## 为当前对话添加技能

1. 打开目标对话。
2. 点击输入栏左侧的 **+**。
3. 在工具面板选择 **添加技能（Skills）**。
4. 选择所需技能。
5. 返回对话继续输入任务。

所选技能作用于当前对话。切换任务时可再次打开添加技能面板。

## 手机附件与 Skill 导入的区别

小程序附件面板支持添加手机文件、相册、微信文件和已连接文档中的资料。附件能力不等于技能安装。

公开流程确认的是 SkillHub 指令安装，尚未确认手机端支持从文件管理器直接导入任意 `SKILL.md` 或 ZIP。

## 使用本仓库

若 SkillHub 已发布兼容的本项目技能包，可复制其安装指令到小程序。没有对应条目时，使用 [WorkBuddy 桌面端 ZIP 导入](README.workbuddy.md)，或选择支持标准 Skill 文件导入的平台。

## 官方资料

- [WorkBuddy 小程序：添加附件与技能](https://www.codebuddy.cn/docs/workbuddymini/features/Attachments-and-Skills)
- [WorkBuddy 小程序：快速开始](https://www.codebuddy.cn/docs/workbuddymini/quick-start/Overview)
- [WorkBuddy Enterprise：技能安装与管理](https://cloud.tencent.com/document/product/1831/134432)
