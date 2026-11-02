<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 手机端 Skill 使用渠道

手机端技能能力主要分为平台技能市场、应用内创建个人 Skill，以及连接远程 Agent。三类能力的安装对象、文件兼容性和运行位置不同。

## 平台技能市场

| 产品 | 公开入口 | 已确认能力 | 文件导入边界 |
| --- | --- | --- | --- |
| 腾讯元宝 | 侧边栏 → 技能 → 全部 | 浏览、安装和调用平台技能 | 本地标准文件导入未确认 |
| 千问 App | 工作助理 → 技能 → 更多技能 | 技能广场浏览和调用 | 与桌面 QwenWork 分开管理 |
| WorkBuddy 小程序 | SkillHub；输入栏 `+` → 添加技能 | 指令安装、对话添加 | 手机文件附件不是 Skill 导入 |
| 智图Claw | 技能 / 技能市场 | 浏览、安装和 Gateway 连接 | 本地 ZIP 导入格式未确认 |
| 灵犀·晓伴 | AI 工具与技能中心 | 第三方技能扩展 | 标准 Agent Skills 导入未确认 |
| AionClaw | Skill 技能市场 | 市场技能安装 | 标准文件导入未确认 |
| AgentOS | 技能商店 | 市场技能浏览和安装 | 自定义文件协议待核实 |

市场安装的是平台发布条目。只有本项目真实出现在对应市场中，才能通过该市场直接安装本项目；名称相似不能作为安装证据。

## 应用内创建个人 Skill

| 产品 | 已记录的创建方式 | 与标准 Skill 的关系 |
| --- | --- | --- |
| 脑花 | 将协作中验证有效的流程沉淀为个人 Skill | 产品内部 Skill；标准导入未确认 |
| 豆包 | 电脑版工作任务模式创建，手机端调用账号技能 | 创建、导入和开发者上架是不同流程 |

通过应用内创建迁移本项目规则时，应逐项检查英语一翻译、大作文、小作文，以及英语二对应三类题型共六份规则，确保评分档位、输出要求和边界均已迁移。

## 通过手机连接远程 Agent

| 产品 | 手机端作用 | Skill 运行位置 |
| --- | --- | --- |
| OpenClaw 消息渠道或客户端 | 远程对话 | OpenClaw Gateway 所在主机 |
| 智图Claw Gateway 连接 | 接入远程 Agent | 配置的 Gateway 主机 |
| 其他远程工作流产品 | 按账号和服务端配置操作 | 以实际部署为准 |

远程连接不会自动把 Skill 安装到手机。应先在远程 Agent 主机安装完整 Skill，再确认手机渠道连接的是同一 Agent 或工作区。

## 需要复用本项目全部规则时

优先选择支持标准 Agent Skills 文件夹或完整 ZIP 的客户端，安装 `skills/kaoyan-english-grader/`。只接受单个文件的入口，可使用[内嵌六类规则的单文件版本](../../dist/kaoyan-english-grader-single-file/SKILL.md)。

将 `SKILL.md` 作为普通聊天附件发送、从市场安装名称相似的技能，或保存一段个人提示词，都不能单独证明六类评分规则已完整安装。

## 相关文档

- [安装渠道总览](README.md)
- [Skills CLI 安装指南](skills-cli.md)
- [Agent 自主安装协议](../../INSTALL.md)
