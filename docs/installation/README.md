<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 安装与版本选择

本仓库提供两个独立 Skill，覆盖相同的六类题型，评分规则一致，文件组织和适用平台不同。

## 两个 Skill 如何选择

| 版本 | 路径 | 结构 | 选择条件 |
| --- | --- | --- | --- |
| 标准版 `kaoyan-english-grader` | `skills/kaoyan-english-grader/` | `SKILL.md` + `references/` 六份规则 | 默认推荐；平台能完整保留主文件和引用目录 |
| 完整版 `kaoyan-english-grader-full` | `skills/kaoyan-english-grader-full/SKILL.md` | 单个文件内嵌全部规则 | 平台无法保留引用目录，但支持单个 `SKILL.md` 导入 |

**标准版是首选。** 完整保留主文件和 `references/` 目录，才能按本项目原始结构直接读取全部评分规则。完整版把规则合并到一个独立文件中，作为目录结构受限时的兼容替代。

支持标准 Agent Skills、原生目录安装或完整目录 ZIP 的平台，应安装标准版。此类平台也可以安装完整版，但不推荐用完整版替代标准安装。

## 先识别平台提供的能力

| 平台能力 | 安装或创建的对象 | 本项目的处理方式 |
| --- | --- | --- |
| 平台技能市场 | 平台已上架的技能条目 | 只有市场条目确实来自本项目时才可以 |
| 应用内创建 | 产品内部指令、工作流或个人 Skill | 手动迁移规则并逐项验收，不等于文件导入 |
| 标准 Skill 文件导入 | 平台支持的 Agent Skill 文件 | 能保留目录时使用标准版；只接受单文件时使用完整版 |
| 完整目录安装 | 标准版主文件与引用目录 | 保留所有文件及相对路径 |
| 单文件 Skill 导入 | 独立的 `SKILL.md` | 使用内嵌全部规则的完整版 |

市场、应用内创建和文件导入属于不同能力。市场中名称相似的技能、聊天附件、知识库文件或保存的提示词，都不能单独证明本项目已经安装。

## 推荐安装路径

### 支持标准 Agent Skills 的开发工具

优先通过 Skills CLI 或宿主原生目录安装标准版：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

指定 Agent 时增加 `--agent <verified-agent-id>`；用户级安装按当前 CLI 版本增加 `-g`。详见 [Skills CLI 指南](skills-cli.md)。

### 支持 ZIP 目录导入的应用

将 `skills/kaoyan-english-grader/` 目录整体打包，确保 ZIP 中的 `SKILL.md` 与 `references/` 同级。导入后检查六份引用文件是否保留。

### 只接受单个 Skill 文件的平台

选择 `skills/kaoyan-english-grader-full/SKILL.md`。该文件已内嵌六类完整评分规则，不依赖外部目录。

### 只有技能市场的平台

只有本项目真实上架且能核验来源时，才能从市场安装本项目；否则选择兼容的 Agent 或远程主机安装。

### 只有应用内创建的平台

把规则迁移为平台内部指令或工作流，逐项检查六类题型、评分档位、输出结构和模拟评分边界。该结果应标记为平台内创建版本，不称为标准 Skill 文件导入。

## 按平台类型查找指南

### 开发工具与 Agent CLI

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

### 桌面 AI 助手与工作流产品

| 产品 | 已记录入口 | 指南 |
| --- | --- | --- |
| Claude 网页版 / Desktop | ZIP 上传 | [Claude](platforms/claude.md) |
| 豆包桌面端 | 应用内创建 / 本地导入（视版本）/ 开发者上架 | [豆包](platforms/doubao.md) |
| 腾讯元宝 | 技能市场 / 专属智能体 | [元宝](platforms/yuanbao.md) |
| WorkBuddy | 技能市场 / 自定义技能 / ZIP 上传 | [WorkBuddy](platforms/workbuddy.md) |
| QwenWork | 技能广场 / 本地文件上传 | [QwenWork](platforms/qwenwork.md) |

### 手机 App 与小程序

| 产品 | 已确认能力 | 指南 |
| --- | --- | --- |
| 豆包 App | 调用账号可用技能 | [豆包手机端](platforms/doubao-mobile.md) |
| 腾讯元宝 App | 技能市场 | [元宝 App](platforms/yuanbao-app.md) |
| 千问 App | 技能广场 | [千问 App](platforms/qwen-app.md) |
| WorkBuddy 小程序 | SkillHub 指令安装、对话添加 | [WorkBuddy 手机版](platforms/workbuddy-mobile.md) |
| 脑花 | 应用内沉淀个人 Skill | [脑花](platforms/brainhua.md) |
| 智图Claw | 技能市场、Gateway | [智图Claw](platforms/zhitu-claw.md) |
| 灵犀·晓伴 | 第三方技能中心 | [灵犀·晓伴](platforms/lingxi-xiaoban.md) |
| AgentOS | 技能商店 | [AgentOS](platforms/agentos.md) |
| AionClaw | 手机端技能市场 | [AionClaw](platforms/aionclaw.md) |

## 手机远程使用

OpenClaw 等自托管 Agent 在 Gateway 主机加载 Skill。手机连接后提供对话入口，实际执行发生在远程主机。手机端市场或对话添加入口不会自动把 Skill 安装到手机本地。

## 安装验收

1. 记录实际使用的能力类型：市场安装、应用内创建、标准文件导入或远程 Agent。
2. 记录选择的 Skill：标准版或完整版，并说明选择原因。
3. 标准版检查主文件、六份引用文件和相对路径；完整版检查六个题型章节均内嵌。
4. 检查宿主发现、启用和调用状态。
5. 分别测试英语一翻译与英语二大作文，核对题型路由、分值和评分依据。

## 相关文档

- [Skills CLI 指南](skills-cli.md)
- [手机端渠道](mobile-apps.md)
- [Agent 安装协议](../../INSTALL.md)
