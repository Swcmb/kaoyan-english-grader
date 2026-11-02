<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# AgentOS（艾嘿）：技能商店与自定义安装

AgentOS 的应用商店版本历史包含技能商店改版、“默认/已装”分类及自定义安装能力。当前功能可能因 App 版本和地区而异。

## 安装与登录

1. 在设备应用商店搜索 AgentOS 或 AIHEY（艾嘿）。
2. 核对开发者与应用信息后安装。
3. 登录并完成首次启动流程。

当地应用商店没有该应用时，按地区可用性处理。不要从来源不明的网站下载安装包。

## 安装市场技能

1. 打开 **技能商店**。
2. 进入 **默认** 或相应分类。
3. 浏览或搜索技能。
4. 打开详情，检查用途和提供方。
5. 按页面提示安装。
6. 在 **已装** 分类确认状态，再返回对话测试。

历史版本说明记录了默认和已装分类；实际入口以当前版本为准。

## 自定义 Skill 的导入边界

公开版本说明提到自定义安装能力，但没有明确文件格式、目录结构或导入协议。因此，暂不能确认 AgentOS 可直接导入标准 `SKILL.md` 文件夹或 ZIP。

若当前版本提供自定义安装入口，先检查支持的格式和目录要求。只有明确支持完整目录或 ZIP 时，才导入本仓库技能包，并检查 `references/` 六份规则是否保留。

## 安全与验证

安装前检查提供方、授权范围和外部服务连接。对读写文件、访问账号或执行自动化的技能，先使用低风险任务验证。

使用本仓库时，检查技能是否可见，并分别测试英语一翻译和英语二大作文。

## 官方资料

- [AgentOS：加拿大区 App Store 页面](https://apps.apple.com/ca/app/agentos/id6759725374)
- [AgentOS：智利区 App Store 页面](https://apps.apple.com/cl/app/agentos/id6759725374)
