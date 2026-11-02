<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 手机端 Skill 使用渠道

手机端产品提供的技能市场、应用内创建、文件导入和远程 Agent 连接属于不同能力。先确认技能在哪里运行，再选择本项目的使用方式。

## 技能市场

| 产品 | 市场入口 | 已知能力边界 | 指南 |
| --- | --- | --- | --- |
| 腾讯元宝 | 侧边栏 → 技能 → 全部 | 安装平台已上架的技能条目 | [元宝 App](platforms/yuanbao-app.md) |
| 千问 App | 工作助理 → 技能 → 更多技能 | 技能广场；手机本地 Skill 文件导入尚未确认 | [千问 App](platforms/qwen-app.md) |
| 智图Claw | 技能 / 技能市场 | 市场技能与 Gateway；本地归档导入尚未确认 | [智图Claw](platforms/zhitu-claw.md) |
| 灵犀·晓伴 | AI 工具与技能中心 | 第三方技能扩展；标准文件导入尚未确认 | [灵犀·晓伴](platforms/lingxi-xiaoban.md) |
| AionClaw | Skill 技能市场 | 市场安装；标准文件导入尚未确认 | [AionClaw](platforms/aionclaw.md) |

市场入口只安装市场实际提供的条目。只有本项目真实上架且发布者和来源可核验时，才能称为从市场安装了本项目。名称相似或功能相近的技能不构成证明。

## 应用内创建个人 Skill

| 产品 | 创建方式 | 指南 |
| --- | --- | --- |
| 脑花 | 将已验证的协作流程沉淀为个人 Skill | [脑花](platforms/brainhua.md) |
| 豆包 | 使用电脑版工作任务模式创建技能，手机端调用账号可用技能 | [豆包手机端](platforms/doubao-mobile.md) |

应用内创建生成的是产品内部格式。迁移本项目规则时，应逐项核对六类题型的评分档位、输入要求、输出结构和模拟评分边界。保存个人 Skill 不等于导入标准 Agent Skill 文件。

## 手机端文件导入

手机文件选择器、聊天附件、知识库上传和 Skill 导入是不同功能。只有平台明确提供 Skill 导入入口并说明支持格式时，才可据此导入本项目。

本项目只有一个自包含的 `SKILL.md`。平台支持完整目录或 ZIP 时，上传 `skills/kaoyan-english-grader/`；平台明确只接受单文件时，上传 `skills/kaoyan-english-grader/SKILL.md`。

## 通过手机连接远程 Agent

| 产品 | 手机端作用 | Skill 运行位置 | 指南 |
| --- | --- | --- | --- |
| OpenClaw | 消息渠道或配套客户端远程对话 | OpenClaw Gateway 所在主机 | [OpenClaw](platforms/openclaw.md) |
| 智图Claw | 连接 Gateway | Gateway 对应的 Agent 主机 | [智图Claw](platforms/zhitu-claw.md) |
| AionClaw | 使用产品提供的远程工作流 | 以账号与服务端配置为准 | [AionClaw](platforms/aionclaw.md) |

远程连接时，在实际运行 Agent 的主机安装 Skill。手机只提供交互入口，技能是否可用取决于远程 Agent 的安装和发现状态。

## 相关入口

- [安装与平台选择总览](README.md)
- [Skills CLI 安装指南](skills-cli.md)
- [Agent 安装与验收协议](../../INSTALL.md)
