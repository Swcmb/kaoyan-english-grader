<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 国内 AI 平台与 Agent 安装索引

本页汇总仓库已记录的国内 AI 产品、开发工具和自托管渠道。各独立指南提供入口、安装步骤、验证方式和能力边界。

## 让 Agent 自行安装

将 [README 中的自然语言安装指令](../README.md#自然语言安装) 发给当前 Agent，或要求它读取 [INSTALL.md](../INSTALL.md)。Agent 应识别宿主、工作区和权限，选择原生安装器、Skills CLI、手动部署或 UI 导入，再检查 Skill 是否可发现。

## 三类能力

| 类型 | 含义 | 对本仓库的意义 |
| --- | --- | --- |
| 标准 Skill 导入 | 导入完整文件夹或 ZIP，保留主文件和引用目录 | 可运行六类题型规则 |
| 平台技能市场 | 安装平台已发布的技能条目 | 只有项目真实上架时才等于安装本仓库 |
| 应用内沉淀 / 远程调用 | 保存产品内工作流，或连接远程 Agent | 需确认规则迁移完整，或远程主机已安装本 Skill |

本仓库的主文件是 `skills/kaoyan-english-grader/SKILL.md`，六份评分规则位于同级 `references/`。只复制主文件不构成完整安装。

## 桌面 AI 助手

| 产品 | 记录的方式 | 指南 |
| --- | --- | --- |
| 豆包工作任务模式 | 创建个人技能；部分版本提供本地导入；开放平台支持服务方提交审核 | [豆包](README.doubao.md) |
| 腾讯元宝 | 技能市场；普通用户本地导入未确认 | [元宝](README.yuanbao.md) |
| WorkBuddy | 本地 ZIP 上传 | [WorkBuddy](README.workbuddy.md) |
| 千问办公（QwenWork） | 本地 SKILL.md/ZIP 上传、对话搜索 | [QwenWork](README.qwenwork.md) |

## 开发工具与 Agent CLI

| 产品 | Skills CLI Agent ID | 指南 |
| --- | --- | --- |
| Claude Code | `claude-code` | [Claude Code](README.claude-code.md) |
| Codex | `codex` | [Codex](README.codex.md) |
| Cursor | `cursor` | [Cursor](README.cursor.md) |
| OpenCode | `opencode` | [OpenCode](README.opencode.md) |
| Gemini CLI | `gemini-cli` | [Gemini CLI](README.gemini-cli.md) |
| Qwen Code | `qwen-code` | [Qwen Code](README.qwen-code.md) |
| Antigravity | `antigravity` | [Antigravity](README.antigravity.md) |
| Kimi Code CLI | `kimi-code-cli` | [Kimi Code](README.kimi-code.md) |
| Trae CN | `trae-cn` | [Trae](README.trae.md) |
| Qoder | `qoder` | [Qoder](README.qoder.md) |
| OpenClaw | `openclaw` | [OpenClaw](README.openclaw.md) |

Agent ID 和目录映射可能随 Skills CLI 版本变化。安装前查看[官方 Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

## 手机 App 与小程序

| 产品 | 入口 | 标准 Skill 文件导入状态 | 指南 |
| --- | --- | --- | --- |
| 豆包 App | 使用账号已有技能 | 手机端本地导入未确认 | [豆包手机端](README.doubao-mobile.md) |
| 腾讯元宝 App | 技能市场 | 本地 SKILL.md/ZIP 未确认 | [元宝 App](README.yuanbao-app.md) |
| 千问 App | 工作助理技能广场 | 手机端本地导入未确认 | [千问 App](README.qwen-app.md) |
| WorkBuddy 小程序 | SkillHub 指令安装、对话添加 | 本地 ZIP 未确认 | [WorkBuddy 手机版](README.workbuddy-mobile.md) |
| 脑花 | 沉淀个人 Skill | 标准文件导入未确认 | [脑花](README.brainhua.md) |
| 智图Claw | 技能市场、Gateway | 本地 ZIP/TAR.GZ 未确认 | [智图Claw](README.zhitu-claw.md) |
| 灵犀·晓伴 | 工具与技能中心 | 标准文件导入未确认 | [灵犀·晓伴](README.lingxi-xiaoban.md) |
| AgentOS | 技能商店与历史自定义安装能力 | 文件格式和地区状态需确认 | [AgentOS](README.agentos.md) |
| AionClaw | iOS/Android 技能市场 | 标准文件导入未确认 | [AionClaw](README.aionclaw.md) |

## 自托管与远程使用

OpenClaw 将 Skill 安装在运行 Gateway/Agent 的主机或服务器上，手机端主要作为远程对话入口。详见 [OpenClaw 指南](README.openclaw.md)。

## 完整安装验收

1. 使用目标产品明确支持的安装方式。
2. 获取完整的 `skills/kaoyan-english-grader/`。
3. 确认 `SKILL.md` 和 `references/` 六份规则存在。
4. 检查 Agent 能发现 Skill 并读取对应规则。
5. 分别测试英语一翻译和英语二大作文。

仅支持技能市场的平台，可以使用市场中真实存在的技能，或通过产品自定义流程迁移规则。此类流程应标明为平台内创建，不能称为安装了本仓库的标准 Skill。

## 相关文档

- [手机端渠道索引](README.mobile-apps.md)
- [Skills CLI 指南](README.skills-cli.md)
- [Claude ZIP 导入](README.claude.md)
- [Agent 自主安装说明](../INSTALL.md)
