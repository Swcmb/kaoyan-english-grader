<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 手机端 Skill 使用渠道

本页区分手机端技能市场、应用内自定义流程，以及连接桌面或云端 Agent 的远程入口。三者的安装对象和运行位置不同。

## 手机端可直接使用的平台技能

| 产品 | 入口 | 能力边界 | 指南 |
| --- | --- | --- | --- |
| 腾讯元宝 | 侧边栏 → 技能 → 全部 | 以平台市场为主 | [元宝 App](README.yuanbao-app.md) |
| 千问 App | 工作助理 → 技能 → 更多技能 | 技能广场；手机本地导入未确认 | [千问 App](README.qwen-app.md) |
| WorkBuddy 小程序 | SkillHub 安装指令；输入栏 `+` → 添加技能 | 当前对话添加；本地 ZIP 未确认 | [WorkBuddy 手机版](README.workbuddy-mobile.md) |
| 智图Claw | 技能/技能市场 | 市场技能与 Gateway；本地归档导入未确认 | [智图Claw](README.zhitu-claw.md) |
| 灵犀·晓伴 | AI 工具与技能中心 | 第三方扩展；标准文件导入未确认 | [灵犀·晓伴](README.lingxi-xiaoban.md) |
| AionClaw | Skill 技能市场 | 市场安装；标准文件导入未确认 | [AionClaw](README.aionclaw.md) |

## 应用内创建或沉淀个人 Skill

| 产品 | 用途 | 指南 |
| --- | --- | --- |
| 脑花 | 将协作中验证有效的流程、标准和方法沉淀为个人 Skill | [脑花](README.brainhua.md) |
| 豆包 | 在电脑版工作任务模式创建技能，手机端调用账号可用技能 | [豆包手机端](README.doubao-mobile.md) |

应用内 Skill 属于产品内部格式。除非官方明确支持标准 Agent Skills 目录与引用文件，否则不能假定它兼容本仓库的 `SKILL.md`、`references/` 和 frontmatter。

## 通过手机连接远程 Agent

| 产品 | 手机端作用 | 技能运行位置 | 指南 |
| --- | --- | --- | --- |
| OpenClaw | 消息渠道或配套客户端远程对话 | OpenClaw Gateway 所在主机 | [OpenClaw](README.openclaw.md) |
| 智图Claw | 连接 Gateway | Gateway 对应的 Agent 主机 | [智图Claw](README.zhitu-claw.md) |
| AionClaw | 使用产品提供的远程工作流 | 以账号与服务端配置为准 | [AionClaw](README.aionclaw.md) |

## 本仓库的手机端使用条件

本 Skill 包含 `skills/kaoyan-english-grader/SKILL.md` 和其 `references/` 下六份评分规则。手机端必须支持完整导入该目录，或连接已安装本 Skill 的远程 Agent，才能复用全部规则。

市场中名称相似的英语批改或作文润色技能，不代表已经安装本仓库。

## 相关入口

- [国内平台总索引](README.domestic-platforms.md)
- [Skills CLI 安装指南](README.skills-cli.md)
- [Agent 自主安装说明](../INSTALL.md)
