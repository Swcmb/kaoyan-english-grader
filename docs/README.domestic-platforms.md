<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 国内 AI 平台支持渠道索引

本页是国内产品适配总入口。每个渠道有独立操作文档，包含入口定位、安装步骤、使用验证和能力边界。

## 先区分三种支持方式

| 类型 | 含义 | 本仓库适配情况 |
|---|---|---|
| **本地导入标准 Skill** | 上传完整技能文件夹/ZIP，或将 Skill 放入产品发现目录 | 可用于本仓库完整批改规则 |
| **平台技能市场** | 只能安装平台当前上架的技能 | 需要平台上架本项目，不能直接等同于本地导入 |
| **应用内沉淀/远程调用** | 把对话流程保存成应用内技能，或通过手机连接远程 Agent | 需将本仓库规则转成该产品支持的格式，或在远程主机安装 |

本仓库技能由 SKILL.md 和 references/ 下六份题型规则组成。只有在目标产品能保留整套目录结构时，才能视为完整导入。

## 桌面 AI 助手

| 产品 | 支持等级 | 适合的安装方式 | 操作文档 |
|---|---|---|---|
| 豆包工作任务模式 | 自定义创建；本地文件导入取决于客户端入口 | 工作任务中创建技能；开发者可通过开放平台上传 ZIP 并审核上架 | [豆包详细指南](README.doubao.md) |
| 腾讯元宝 | 技能市场安装 | 从侧边栏技能入口安装现成平台技能；本地标准 Skill 导入尚未确认 | [腾讯元宝详细指南](README.yuanbao.md) |
| WorkBuddy | 本地 ZIP 导入 | 专家·技能·连接器 → 添加技能 → 上传技能 | [WorkBuddy 桌面端详细指南](README.workbuddy.md) |
| 千问办公（QwenWork） | 本地 SKILL.md/ZIP 导入 | 扩展 → 技能 → 添加 → 上传技能 | [千问办公详细指南](README.qwenwork.md) |
| Trae / Trae CN | 本地 SKILL.md/ZIP 导入；全局/项目级 | 设置 → 技能与命令 → 创建/导入；或 Skills CLI | [Trae 详细指南](README.trae.md) |
| Qoder | 本地 SKILL.md/ZIP 导入；IDE/CLI | Extensions → Skills → Add Skills → Upload Skill；或 Skills CLI | [Qoder 详细指南](README.qoder.md) |

## 开发工具与 Agent CLI

这些产品原生支持标准 Agent Skills 或可通过 Skills CLI 安装：

| 产品 | Skills CLI 参数 | 详细操作 |
|---|---|---|
| Claude Code | claude-code | [Claude Code](README.claude-code.md) |
| Codex | codex | [Codex](README.codex.md) |
| Cursor | cursor | [Cursor](README.cursor.md) |
| OpenCode | opencode | [OpenCode](README.opencode.md) |
| Gemini CLI | gemini-cli | [Gemini CLI](README.gemini-cli.md) |
| Qwen Code | qwen-code | [Qwen Code](README.qwen-code.md) |
| Antigravity | antigravity | [Antigravity](README.antigravity.md) |
| Kimi Code CLI | kimi-code-cli | [Kimi Code](README.kimi-code.md) |
| Trae CN | trae-cn | [Trae](README.trae.md) |
| Qoder | qoder | [Qoder](README.qoder.md) |
| OpenClaw | openclaw | [OpenClaw](README.openclaw.md) |

统一安装命令模板：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent AGENT_ID
~~~

将 AGENT_ID 替换为表格中的参数。需要全局安装时增加 -g。每个工具的实际目录映射和发现范围以其独立文档为准。

## 手机 App 与小程序

手机端渠道的能力差异较大。下表所说的“能安装技能”，可能指市场技能、应用内工作流或远程 Agent 能力，并非全部都能导入本地 SKILL.md。

| 手机端产品 | 已确认能力 | 本仓库完整 Skill 导入情况 | 操作文档 |
|---|---|---|---|
| 豆包 App | 使用账号已有技能 | 手机端创建/本地导入流程不明确，创建请使用电脑版 | [豆包手机端](README.doubao-mobile.md) |
| 腾讯元宝 App | 技能市场浏览、安装、调用 | 未确认支持本地 SKILL.md/ZIP | [元宝 App](README.yuanbao-app.md) |
| 千问 App | 工作助理技能广场 | 手机端本地导入未确认；桌面 QwenWork 可上传 | [千问 App](README.qwen-app.md) |
| WorkBuddy 微信小程序 | SkillHub 安装；当前对话添加技能 | 手机端按 SkillHub 流程使用；本地 ZIP 导入未确认 | [WorkBuddy 手机版](README.workbuddy-mobile.md) |
| 脑花 | 将协作流程沉淀成个人 Skill | 属于应用内流程沉淀；标准 Skill 文件导入未确认 | [脑花](README.brainhua.md) |
| 智图Claw | 技能市场、技能管理、Gateway 连接 | 本地 ZIP/TAR.GZ 导入格式未确认 | [智图Claw](README.zhitu-claw.md) |
| 灵犀·晓伴 | AI 工具与技能中心、第三方技能扩展 | 标准 SKILL.md/ZIP 导入未确认 | [灵犀·晓伴](README.lingxi-xiaoban.md) |
| AgentOS（艾嘿） | 产品历史版本提供技能商店和自定义安装能力 | 文件格式和当前上架状态需按地区确认 | [AgentOS](README.agentos.md) |
| AionClaw | iOS/Android App 和 Skill 技能市场 | 标准本地文件导入未确认 | [AionClaw](README.aionclaw.md) |

## 极客向与自托管渠道

| 产品 | 方式 | 详细操作 |
|---|---|---|
| OpenClaw | 在 Gateway/Agent 主机上安装标准 Skill，手机通过消息渠道远程使用 | [OpenClaw 安装指南](README.openclaw.md) |

OpenClaw 适合愿意管理服务器、Gateway、权限和消息渠道的用户。手机主要是远程对话入口，技能运行在 Agent 主机上。Termux 等 Android 自托管方式属于自行部署，需要另行处理运行时和设备兼容性。

暂未将 Air-Ko 列为本仓库正式适配渠道：目前没有找到足够明确且可复现的官方 Skill 安装/发现文档。找到可核验的操作入口后再加入，避免仅凭产品描述宣称支持。

## 导入前检查

1. 下载或克隆仓库后，只取 skills/kaoyan-english-grader/ 作为技能包来源。
2. 确认 ZIP 根目录能看到 SKILL.md 和 references/。
3. 导入后检查六份题型规则是否保留。
4. 至少测试英语一翻译和英语二大作文，核对分值、题型路由和引用文件。
5. 不支持文件夹或 ZIP 导入的平台，按该产品自身支持方式使用市场技能或建立应用内流程；不要把普通聊天附件当作 Skill 安装。

## 相关入口

- [通用 Skills CLI 安装](README.skills-cli.md)
- [Claude 网页版 / Desktop 自定义 Skill 上传](README.claude.md)
- [平台安装方式与 CLI 参数总表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
