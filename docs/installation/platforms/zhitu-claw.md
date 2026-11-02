<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 智图Claw：技能市场与 Gateway 连接

智图Claw 面向 iPhone/iPad 提供移动 AI 助手。App Store 介绍包含技能浏览、安装、管理和 Gateway 连接能力。

## 安装 App

1. 在 iPhone 或 iPad 打开 App Store。
2. 搜索“智图Claw”。
3. 安装并启动 App。
4. 按界面提示登录并完成基础配置。

## 连接 Gateway

智图Claw 可连接桌面端或托管环境中的 Agent。先准备正在运行且允许手机访问的 Gateway。

连接前核对：

- Gateway 服务已启动。
- 手机与 Gateway 网络互通。
- 使用 Gateway 提供的有效地址和认证信息。
- 不要将访问令牌、密钥或管理密码粘贴到公开聊天或技能说明中。

连接字段和认证方式以当前 App 与 Gateway 版本为准。

## 浏览和安装技能

1. 打开技能区域或技能市场。
2. 浏览分类或搜索目标技能。
3. 打开详情，核对名称、用途和来源。
4. 按界面提示安装。
5. 在技能管理页确认状态。
6. 返回对话提交任务，检查 Agent 是否调用。

## 本仓库的导入边界

App Store 公开说明尚未明确列出手机端本地 ZIP/TAR.GZ 导入格式、入口和目录要求。因此，市场安装不等同于导入任意 `SKILL.md` 压缩包。

若当前版本提供本地导入入口，先验证支持格式，再导入包含主文件和 `references/` 六份规则的完整包。若只有市场入口，可使用已发布技能来源，或在兼容 Gateway 主机上安装标准 Skill。

## 验证与官方资料

- App 显示 Gateway 已连接。
- 技能管理页显示目标技能已安装。
- 对话能够实际调用技能。
- 使用本仓库时，英语一翻译和英语二大作文均可读取对应规则。

[智图Claw：App Store 页面](https://apps.apple.com/cn/app/%E6%99%BA%E5%9B%BEclaw/id6760357112)
