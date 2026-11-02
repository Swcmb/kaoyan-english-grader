<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 安装与使用渠道

本仓库交付一个标准 Agent Skill：`skills/kaoyan-english-grader/`。完整安装必须保留 `SKILL.md` 和 `references/` 下六份评分规则。

## 首选安装路径

将 [README 中的自然语言安装指令](../../README.md#安装) 发送给当前 Agent，或直接要求 Agent 读取 [INSTALL.md](../../INSTALL.md)。Agent 应识别宿主、工作区、可用安装器和权限，执行安装并验证结果。

开发工具与 CLI 用户也可以直接使用 [Skills CLI 指南](skills-cli.md)。

## 先区分安装对象

| 方式 | 实际安装对象 | 能否直接复用本仓库完整 Skill |
| --- | --- | --- |
| 标准 Skill 导入 | 完整文件夹或 ZIP | 是，前提是保留引用目录 |
| 平台技能市场 | 平台已发布的技能条目 | 仅当本项目真实上架该市场 |
| 应用内创建个人 Skill | 产品内部工作流或提示词 | 需人工迁移并核对六类规则 |
| 手机远程连接 Agent | 远程主机已安装的 Skill | 是，Skill 在远程主机运行 |

将 `SKILL.md` 当作普通聊天附件发送，或安装名称相似的市场技能，都不等于安装了本仓库。

## 开发工具与 Agent CLI

| 产品 | 安装入口 | 独立指南 |
| --- | --- | --- |
| Claude Code | Skills CLI / 原生目录 | [Claude Code](platforms/claude-code.md) |
| Codex | Skills CLI / 原生目录 | [Codex](platforms/codex.md) |
| Cursor | Skills CLI / IDE | [Cursor](platforms/cursor.md) |
| OpenCode | Skills CLI / 原生目录 | [OpenCode](platforms/opencode.md) |
| Gemini CLI | 原生 Skills 命令 / Skills CLI | [Gemini CLI](platforms/gemini-cli.md) |
| Qwen Code | Skills CLI / 原生目录 | [Qwen Code](platforms/qwen-code.md) |
| Antigravity | Skills CLI / 插件 | [Antigravity](platforms/antigravity.md) |
| Kimi Code CLI | Skills CLI / 插件 | [Kimi Code CLI](platforms/kimi-code.md) |
| Trae | IDE 导入 / Skills CLI | [Trae](platforms/trae.md) |
| Qoder | IDE 上传 / Skills CLI | [Qoder](platforms/qoder.md) |
| OpenClaw | 原生命令 / Skills CLI | [OpenClaw](platforms/openclaw.md) |

Agent ID、路径映射和命令参数可能随 Skills CLI 更新。安装前检查[官方 Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

## 桌面 AI 助手与工作流产品

| 产品 | 已记录的方式 | 独立指南 |
| --- | --- | --- |
| Claude 网页版 / Desktop | 自定义 Skill ZIP 上传 | [Claude](platforms/claude.md) |
| 豆包桌面端 | 个人技能创建；部分版本本地导入；开发者可提交上架审核 | [豆包](platforms/doubao.md) |
| 腾讯元宝 | 技能市场 / 专属智能体配置 | [元宝](platforms/yuanbao.md) |
| WorkBuddy | 本地 ZIP 上传 | [WorkBuddy](platforms/workbuddy.md) |
| 千问办公（QwenWork） | 本地 `SKILL.md` / ZIP 上传 | [QwenWork](platforms/qwenwork.md) |

## 手机 App 与小程序

| 产品 | 主要入口 | 标准文件导入状态 | 独立指南 |
| --- | --- | --- | --- |
| 豆包 App | 账号已有技能 | 手机端导入未确认 | [豆包手机端](platforms/doubao-mobile.md) |
| 腾讯元宝 App | 技能市场 | 本地导入未确认 | [元宝 App](platforms/yuanbao-app.md) |
| 千问 App | 工作助理技能广场 | 手机端导入未确认 | [千问 App](platforms/qwen-app.md) |
| WorkBuddy 小程序 | SkillHub 安装指令、对话添加 | 本地 ZIP 未确认 | [WorkBuddy 手机版](platforms/workbuddy-mobile.md) |
| 脑花 | 沉淀个人 Skill | 标准文件导入未确认 | [脑花](platforms/brainhua.md) |
| 智图Claw | 技能市场、Gateway | 本地归档导入未确认 | [智图Claw](platforms/zhitu-claw.md) |
| 灵犀·晓伴 | 工具与技能中心 | 标准文件导入未确认 | [灵犀·晓伴](platforms/lingxi-xiaoban.md) |
| AgentOS | 技能商店与历史自定义安装 | 文件格式和地区状态待确认 | [AgentOS](platforms/agentos.md) |
| AionClaw | iOS / Android 技能市场 | 标准文件导入未确认 | [AionClaw](platforms/aionclaw.md) |

## 自托管与远程使用

OpenClaw 等自托管 Agent 在运行 Gateway/Agent 的主机上加载 Skill，手机端通常提供远程对话入口。参阅 [OpenClaw 指南](platforms/openclaw.md)。

## 完整安装验收

1. 使用目标产品真实支持的安装方式。
2. 获取完整的 `skills/kaoyan-english-grader/`。
3. 确认 `SKILL.md` 和 `references/` 六份规则存在且可读取。
4. 检查 Agent 能发现 Skill，并能按题型读取对应规则。
5. 分别测试英语一翻译和英语二大作文。

只支持市场的平台，可使用市场中真实存在的技能，或通过产品自定义流程迁移规则。此类流程应标明为平台内创建，不应称为安装了本仓库的标准 Skill。

## 相关文档

- [Skills CLI 安装指南](skills-cli.md)
- [手机端渠道索引](mobile-apps.md)
- [Agent 自主安装协议](../../INSTALL.md)
