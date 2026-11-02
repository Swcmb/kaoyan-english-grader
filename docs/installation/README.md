<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 安装与平台选择

本仓库提供一个自包含的标准 Agent Skill：`kaoyan-english-grader`。英语一、英语二翻译、大作文和小作文六类题型的全部评分规则都位于同一个 `SKILL.md` 中，不需要其他辅助文件。

## Skill 文件

~~~text
skills/
└── kaoyan-english-grader/
    └── SKILL.md
~~~

安装时根据平台能力选择导入方式：

| 平台能力 | 导入对象 | 本项目的做法 |
| --- | --- | --- |
| 原生 Agent Skills 目录 | 标准 Skill 文件夹 | 安装 `skills/kaoyan-english-grader/` |
| 完整目录 ZIP 上传 | Skill 文件夹压缩包 | ZIP 中保留 `kaoyan-english-grader/SKILL.md` |
| 单文件 Skill 导入 | 独立 `SKILL.md` | 导入 `skills/kaoyan-english-grader/SKILL.md` |
| 平台技能市场 | 平台已上架的条目 | 只有本项目实际出现在市场且来源可核验时才可安装 |
| 应用内创建 | 平台内部指令、工作流或个人 Skill | 迁移规则并逐项验收，标记为平台内创建版本 |
| 远程 Agent | Gateway 或远程主机上的 Skill | 在实际运行 Agent 的主机安装 |

**平台技能市场、应用内创建、标准 Skill 文件导入和聊天附件是不同能力。** 市场中名称相似的技能、聊天附件或知识库上传都不能证明本项目已安装。

## 推荐安装方式

支持 Agent Skills 的平台，优先通过其原生目录安装功能或 Skills CLI 安装：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
~~~

指定 Codex：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex
~~~

单文件导入入口可以直接上传 `skills/kaoyan-english-grader/SKILL.md`。ZIP 上传时压缩完整 Skill 目录，保持目录名和 `SKILL.md` 的相对结构。

## 安装后的验收

1. 确认目标目录中存在完整的 `SKILL.md`。
2. 确认 Agent 能发现并调用 `kaoyan-english-grader`。
3. 测试英语一翻译和英语二大作文两种不同评分规则。
4. 核对题型、满分、模拟评分依据和输出结构。
5. 确认评分结果明确标记为练习用途，不表述为官方阅卷分数。

具体产品路径、导入入口和重新加载方式以对应平台当前官方资料为准。

## 平台指南

| 类型 | 指南 |
| --- | --- |
| Agent / IDE | [Claude Code](platforms/claude-code.md)、[Codex](platforms/codex.md)、[Gemini CLI](platforms/gemini-cli.md)、[Cursor](platforms/cursor.md)、[Antigravity](platforms/antigravity.md)、[OpenCode](platforms/opencode.md)、[Qoder](platforms/qoder.md)、[Kimi Code](platforms/kimi-code.md)、[Qwen Code](platforms/qwen-code.md)、[Trae](platforms/trae.md) |
| 桌面应用 | [Claude](platforms/claude.md)、[豆包](platforms/doubao.md)、[QwenWork](platforms/qwenwork.md)、[WorkBuddy](platforms/workbuddy.md)、[元宝](platforms/yuanbao.md) |
| 手机应用与远程入口 | [手机端总览](mobile-apps.md)、[元宝 App](platforms/yuanbao-app.md)、[千问 App](platforms/qwen-app.md)、[豆包手机端](platforms/doubao-mobile.md)、[WorkBuddy 小程序](platforms/workbuddy-mobile.md)、[OpenClaw](platforms/openclaw.md)、[智图Claw](platforms/zhitu-claw.md)、[AionClaw](platforms/aionclaw.md) |
| 其他产品 | [AgentOS](platforms/agentos.md)、[脑花](platforms/brainhua.md)、[灵犀·晓伴](platforms/lingxi-xiaoban.md) |

需要由 Agent 自主完成安装时，先读取仓库根目录 [INSTALL.md](../../INSTALL.md)，并在完成后报告实际安装路径和验证结果。
