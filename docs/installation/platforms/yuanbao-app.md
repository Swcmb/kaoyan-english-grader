<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# 腾讯元宝 App：技能市场安装与调用

腾讯元宝手机端提供技能入口，可浏览、安装和调用平台技能。公开用户流程以技能市场为主。

## 安装与使用

1. 更新元宝 App 并登录。
2. 打开侧边栏中的 **技能**。
3. 进入 **全部**，按分类浏览或搜索关键词。
4. 打开技能详情，核对功能说明、提供方和授权要求。
5. 按界面提示安装或使用。
6. 返回对话提交匹配任务。

## 能力边界

公开用户端流程没有明确说明普通用户可导入本地 `SKILL.md` 或 ZIP。市场安装只有在本项目实际上架后才代表安装本项目。需要完整规则时，使用支持目录或单文件导入的桌面 Agent。

## 验收

检查技能状态，并分别测试英语一翻译和英语二大作文，确认完整规则、题型路由与模拟分值可用。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [元宝官方：技能上新与安装操作](https://weibo.com/2/detail/5354654420435913)
- [元宝技能入口介绍](https://www.xmsumi.com/detail/4386)
