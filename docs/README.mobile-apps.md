<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 手机端 Skill 使用渠道索引

本页汇总手机 App、小程序和手机远程控制方案。各产品的技能能力分为三类：市场技能安装、应用内沉淀自定义流程、从手机连接远程 Agent。它们不自动代表支持导入任意标准 SKILL.md 文件夹。

## 可直接在手机端安装/使用平台技能

| 产品 | 手机端操作入口 | 能力边界 | 操作文档 |
|---|---|---|---|
| 腾讯元宝 | 侧边栏 → 技能 → 全部 → 选择技能 → 安装/使用 | 普通用户以技能市场为主 | [腾讯元宝 App](README.yuanbao-app.md) |
| 千问 App | 工作助理 → 技能 → 更多技能 | 技能广场安装和调用；桌面 QwenWork 有独立本地导入能力 | [千问 App](README.qwen-app.md) |
| WorkBuddy 微信小程序 | 对话输入栏左侧 + → 添加技能；通过 SkillHub 获取技能 | 当前对话添加；官方公开流程没有确认手机本地 ZIP 导入 | [WorkBuddy 手机版](README.workbuddy-mobile.md) |
| 智图Claw | 技能/技能市场 → 浏览 → 安装；可配置 Gateway | 技能市场和 Gateway；本地归档导入格式未确认 | [智图Claw](README.zhitu-claw.md) |
| 灵犀·晓伴 | AI 工具与技能中心 | 第三方技能扩展；标准 SKILL.md 文件导入未确认 | [灵犀·晓伴](README.lingxi-xiaoban.md) |
| AionClaw | Skill 技能市场 → 选择并安装 | 市场技能；标准本地文件导入未确认 | [AionClaw](README.aionclaw.md) |

## 应用内沉淀个人 Skill

| 产品 | 适合的用途 | 操作文档 |
|---|---|---|
| 脑花 | 把多轮协作中验证有效的步骤、标准和方法沉淀成个人 Skill | [脑花 App](README.brainhua.md) |
| 豆包 | 在电脑版工作任务模式创建自定义 Skill，手机端使用账号可用技能 | [豆包手机端](README.doubao-mobile.md) |

应用内创建/沉淀的 Skill 是产品自身的数据和能力格式。不能假定它与标准 Agent Skills 的目录、引用文件和 frontmatter 完全兼容。

## 通过手机连接桌面或云端 Agent

| 产品 | 手机端作用 | 技能实际运行位置 | 操作文档 |
|---|---|---|---|
| OpenClaw | 通过受支持消息渠道或配套客户端远程聊天 | 运行 OpenClaw Gateway 的本机或服务器 | [OpenClaw](README.openclaw.md) |
| 智图Claw | 连接智图 Gateway | Gateway 所连接的 Agent 主机 | [智图Claw](README.zhitu-claw.md) |
| AionClaw | 按产品提供的远程工作流使用 | 具体部署以账号和服务端产品配置为准 | [AionClaw](README.aionclaw.md) |

## 本仓库 Skill 的移动端适配

本仓库包含：

- 主指令：skills/kaoyan-english-grader/SKILL.md
- 六份题型规则：skills/kaoyan-english-grader/references/*.md

手机端只有在支持完整 Skill 包导入、或连接到已安装本技能的远程 Agent 时，才能完整复用所有评分规则。技能市场中名称相似的“英语批改”或“作文润色”能力，不能视为本仓库 Skill 已安装。

## 相关文档

- [国内平台完整索引](README.domestic-platforms.md)
- [桌面端千问办公（QwenWork）](README.qwenwork.md)
- [桌面端 WorkBuddy](README.workbuddy.md)
- [Claude 网页版与 Desktop](README.claude.md)
