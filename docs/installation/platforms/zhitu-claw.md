<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# 智图Claw：技能市场与 Gateway 连接

智图Claw 的应用商店介绍包含技能浏览、安装、管理和 Gateway 连接。市场技能与远程 Gateway 上的标准 Skill 应分别检查。

## 安装与使用

### 安装 App

在 iPhone 或 iPad 打开 App Store，搜索“智图Claw”，安装后登录并完成基础配置。

### 连接 Gateway

1. 准备正在运行且允许手机访问的 Gateway。
2. 确认手机与 Gateway 网络互通。
3. 使用 Gateway 提供的地址和认证信息连接。
4. 检查连接状态，不要将访问令牌或管理密码粘贴到公开聊天。

### 浏览技能市场

打开技能区域或市场，搜索目标技能，查看来源和使用条件，再按界面提示安装。

## 能力边界

公开 App Store 资料未明确列出手机端本地 ZIP/TAR.GZ 导入格式和目录要求。若只有市场入口，可使用真实上架条目；若连接 Gateway，则应在 Gateway 主机安装标准 Skill。只有确认本地导入保留主文件和六份内嵌评分规则时，才可认定为完整目录导入。

## 验收

检查技能状态，并分别测试英语一翻译和英语二大作文，确认完整规则、题型路由与模拟分值可用。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [智图Claw：App Store 页面](https://apps.apple.com/cn/app/%E6%99%BA%E5%9B%BEclaw/id6760357112)
