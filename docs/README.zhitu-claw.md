<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 智图Claw：手机端技能市场与 Gateway

智图Claw 是面向 iPhone/iPad 的移动 AI 助手。App Store 介绍了技能浏览、安装、管理和 Gateway 连接能力。

## 安装 App

1. 在 iPhone 或 iPad 打开 App Store。
2. 搜索“智图Claw”。
3. 安装并启动 App。
4. 根据应用界面完成首次登录和基本配置。

## 连接 Gateway

智图Claw 通过 Gateway 连接桌面端或托管环境中的 Agent 能力。先准备一个正在运行且允许移动端访问的 Gateway，再在 App 的 Gateway/连接设置中按界面提示完成连接。

连接前确认：
- Gateway 服务已启动；
- 手机与 Gateway 之间网络可达；
- 使用的是 Gateway 提供的有效连接地址和认证信息；
- 不要将访问令牌、密钥或管理密码粘贴到公开聊天或技能说明中。

Gateway 的配置字段和连接方式以当前 App 版本及 Gateway 服务端说明为准。本指南不假设所有用户都使用同一种部署方式。

## 浏览与安装技能

1. 打开 App 的技能区域或技能市场。
2. 浏览或搜索所需技能。
3. 打开技能详情，检查名称、说明和来源。
4. 点击安装，并在技能管理区域确认状态。
5. 返回对话，描述任务并检查 Agent 是否调用该技能。

App Store 页面确认支持浏览、安装和管理技能包，并可连接智图 Gateway。

## 导入本仓库 Skill 的边界

目前 App Store 公开说明没有明确列出手机端本地 ZIP/TAR.GZ 导入的文件格式、入口和目录规范。因此，不将“技能市场支持安装”描述为“支持从手机直接导入任意 SKILL.md 压缩包”。

如果当前版本的技能管理页确实提供本地导入入口，导入本仓库时必须保留 SKILL.md 与 references/ 六份规则文件，并在导入后逐一验证引用文件可读。若界面只有市场安装，则需要先将技能发布到智图Claw 支持的技能来源，或在兼容的 Gateway 主机上安装标准 Skill。

## 验证

- App 显示 Gateway 已连接。
- 目标技能在技能管理页面显示已安装。
- 对话能够按预期调用技能。
- 使用本仓库时，英语一翻译和英语二大作文均能读取对应规则。

## 官方资料

- [智图Claw：App Store 页面](https://apps.apple.com/cn/app/%E6%99%BA%E5%9B%BEclaw/id6760357112)
