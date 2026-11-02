<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# WorkBuddy 手机版：微信小程序安装 Skill

WorkBuddy 手机端通过微信小程序使用。公开文档说明，用户可以从 SkillHub 获取技能包，再在对话中添加技能。

## 从 SkillHub 获取技能

1. 在微信中打开 WorkBuddy 小程序，并登录账号。
2. 在浏览器或 SkillHub 页面找到需要的 Skill。
3. 打开技能详情，复制页面提供的安装指令。
4. 回到 WorkBuddy 小程序。
5. 将安装指令粘贴到 WorkBuddy 对话框并发送。
6. 等待 WorkBuddy 完成安装；安装成功后，技能可在添加技能列表中使用。

SkillHub 页面提供的指令可能包含具体技能来源和安装参数。使用前检查技能发布者和来源，不要将来源不明的命令直接粘贴执行。

## 为当前对话启用技能

1. 打开 WorkBuddy 小程序中的目标对话。
2. 点击输入栏左侧的 **+**。
3. 在工具面板中选择 **添加技能（Skills）**。
4. 在技能选择面板中选中所需技能。
5. 返回对话，继续输入任务。

所选技能在当前对话中生效。需要切换任务时，可再次打开添加技能面板调整。

## 通过手机文件上传的边界

小程序的附件面板支持从手机文件、相册、微信文件和已连接文档中添加常见资料。该附件能力不等同于导入 Skill 包。官方公开流程中的技能安装方式是 SkillHub 指令安装，目前没有确认手机端能直接从文件管理器选择任意 SKILL.md 或 ZIP 作为技能安装。

## 本仓库的使用方式

本仓库的 Skill 包含主文件和六份 references 规则。若 SkillHub 已发布本项目兼容的技能包，可复制其安装指令到 WorkBuddy 小程序；若没有对应条目，使用 WorkBuddy 桌面端上传本地 ZIP，或使用其他支持本地 Skill 导入的平台。

## 官方资料

- [WorkBuddy 小程序：添加附件与技能](https://www.codebuddy.cn/docs/workbuddymini/features/Attachments-and-Skills)
- [WorkBuddy 小程序：快速开始](https://www.codebuddy.cn/docs/workbuddymini/quick-start/Overview)
- [WorkBuddy Enterprise：技能安装与管理](https://cloud.tencent.com/document/product/1831/134432)
