<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 安装与使用渠道

本仓库提供标准目录版和完整单文件版两种 Skill 交付形式。目录版包含 `SKILL.md` 与六份 `references/` 规则；单文件版已将六类规则内嵌，适合只接受单个 `SKILL.md` 的导入入口。

## 先区分安装对象

| 能力 | 实际对象 | 是否直接包含全部规则 |
| --- | --- | --- |
| 标准 Skill 目录导入 | 主文件 + 引用目录 | 是，前提是目录完整 |
| 单文件 Skill 导入 | 独立完整的 `SKILL.md` | 是，六类规则已内嵌 |
| 平台技能市场 | 平台已发布的技能条目 | 取决于市场条目 |
| 应用内创建个人 Skill | 产品内部指令或工作流 | 需人工迁移并核对 |
| 手机远程连接 Agent | 远程主机上的 Agent | 取决于远程安装 |

技能市场、应用内创建和标准文件导入是不同能力。市场中名称相似的技能、聊天附件和已保存提示词都不能证明安装了本项目。要直接复用全部规则，应导入完整目录版或完整单文件版。

## 推荐安装

支持标准 Agent Skills 的工具优先使用 Skills CLI：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

也可以交由 [Agent 安装协议](../../INSTALL.md) 自动执行。单文件版本见[完整 SKILL.md](../../dist/kaoyan-english-grader-single-file/SKILL.md)。

## 开发工具与 Agent CLI

| 产品 | 入口 | 指南 |
| --- | --- | --- |
| Claude Code | Skills CLI / 原生目录 | [Claude Code](platforms/claude-code.md) |
| Codex | Skills CLI / `.agents/skills/` | [Codex](platforms/codex.md) |
| Cursor | Skills CLI / IDE / 原生目录 | [Cursor](platforms/cursor.md) |
| OpenCode | Skills CLI / 原生目录 | [OpenCode](platforms/opencode.md) |
| Gemini CLI | 原生命令 / Skills CLI | [Gemini CLI](platforms/gemini-cli.md) |
| Qwen Code | Skills CLI / 原生目录 | [Qwen Code](platforms/qwen-code.md) |
| Antigravity | Skills CLI / 插件 | [Antigravity](platforms/antigravity.md) |
| Kimi Code CLI | Skills CLI / 插件 | [Kimi Code CLI](platforms/kimi-code.md) |
| Trae | IDE 导入 / Skills CLI | [Trae](platforms/trae.md) |
| Qoder | IDE 上传 / Skills CLI | [Qoder](platforms/qoder.md) |
| OpenClaw | 原生命令 / Skills CLI | [OpenClaw](platforms/openclaw.md) |

Skills CLI 的 Agent ID 和目录映射会更新，安装前检查[官方支持清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

## 桌面 AI 助手与工作流产品

| 产品 | 已记录入口 | 指南 |
| --- | --- | --- |
| Claude 网页版 / Desktop | ZIP 上传 | [Claude](platforms/claude.md) |
| 豆包桌面端 | 个人技能创建、本地导入（视版本）及开发者上架 | [豆包](platforms/doubao.md) |
| 腾讯元宝 | 技能市场 / 专属智能体 | [元宝](platforms/yuanbao.md) |
| WorkBuddy | 本地技能包上传 | [WorkBuddy](platforms/workbuddy.md) |
| QwenWork | 技能广场、仓库获取、本地文件上传 | [QwenWork](platforms/qwenwork.md) |

## 手机 App 与小程序

| 产品 | 主要能力 | 标准文件导入状态 | 指南 |
| --- | --- | --- | --- |
| 豆包 App | 调用账号可用技能 | 手机本地导入未确认 | [豆包手机端](platforms/doubao-mobile.md) |
| 腾讯元宝 App | 技能市场 | 本地导入未确认 | [元宝 App](platforms/yuanbao-app.md) |
| 千问 App | 技能广场 | 本地导入未确认 | [千问 App](platforms/qwen-app.md) |
| WorkBuddy 小程序 | SkillHub 指令安装、对话添加 | 本地 ZIP 未确认 | [WorkBuddy 手机版](platforms/workbuddy-mobile.md) |
| 脑花 | 沉淀个人 Skill | 标准导入未确认 | [脑花](platforms/brainhua.md) |
| 智图Claw | 技能市场、Gateway | 本地归档导入未确认 | [智图Claw](platforms/zhitu-claw.md) |
| 灵犀·晓伴 | 工具与技能中心 | 标准导入未确认 | [灵犀·晓伴](platforms/lingxi-xiaoban.md) |
| AgentOS | 技能商店 | 文件协议待核实 | [AgentOS](platforms/agentos.md) |
| AionClaw | 手机端技能市场 | 标准导入未确认 | [AionClaw](platforms/aionclaw.md) |

## 手机远程使用

OpenClaw 等自托管 Agent 在 Gateway 主机加载 Skill。手机连接后提供对话入口，实际执行仍发生在远程主机。参阅 [OpenClaw 指南](platforms/openclaw.md)。

## 安装验收

1. 确认使用目录版或单文件版。
2. 目录版检查主文件和六份引用文件；单文件版确认全部规则已内嵌。
3. 检查宿主发现和启用状态。
4. 分别测试英语一翻译与英语二大作文。
5. 核对题型路由、分值、评分依据和输出结构。

应用内创建的版本应标明为平台内实现，并逐项检查六类规则，不能称为原样安装的标准 Skill。

## 相关文档

- [Skills CLI 指南](skills-cli.md)
- [手机端渠道](mobile-apps.md)
- [Agent 安装协议](../../INSTALL.md)
