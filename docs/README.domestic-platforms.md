<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 国内 AI 平台与手机端 Skill 安装指南

本文补充国内 AI 助手、开发工具和手机 App 的 Skill 使用方式。这里区分两种能力：

- **导入自定义 Skill**：可以导入本仓库的 `SKILL.md` 和 `references/` 规则文件，或从标准 Agent Skill 目录读取。
- **安装市场技能**：只能安装平台技能市场中已有的能力，不能据此推断平台支持导入任意第三方 `SKILL.md`。

本仓库的批改 Skill 依赖六份 `references/*.md` 题型规则。只导入 `SKILL.md` 而遗漏 `references/`，会导致题型路由后无法读取完整评分规则。

## 桌面端与开发工具

| 产品 | 自定义 Skill 支持 | 安装入口 / 方式 | 安装范围与注意事项 |
|---|---|---|---|
| 豆包（工作任务模式） | 支持创建自定义 Skill；开放平台支持开发者提交技能包 | 电脑版工作任务模式进入技能相关入口，通过对话创建自定义技能；服务方可通过豆包开放平台上传 ZIP 技能包 | 官方公开的 ZIP 上传流程面向开发者，涉及企业资质和平台审核。个人用户是否能导入任意本地 `SKILL.md`/文件夹，以及 `.agent/skills/` 是否为当前正式扫描目录，尚缺少稳定的官方说明；以客户端版本为准。 |
| 腾讯元宝 | 有限支持 | App 或电脑端侧边栏进入「技能」，浏览并安装平台提供的技能 | 普通用户侧的公开流程以技能市场安装、使用为主。服务方可以通过元宝开放平台接入技能；这不代表普通用户可以直接导入任意本地 `SKILL.md`。 |
| WorkBuddy | 支持 | 桌面端进入「专家·技能·连接器」→「添加技能」→「上传技能」，导入本地技能包；也可以查找或创建技能 | 支持用户级和项目级技能。常见目录为用户级 `~/.workbuddy/skills/`、项目级 `.workbuddy/skills/`；部分版本/工作区也会扫描 `.agents/skills/`。目录优先级和实际路径以当前版本文档为准。 |
| 千问办公（QwenWork） | 支持 | 左侧「扩展」→「技能」；可从 Skill 广场安装、在对话中搜索安装，或上传本地 `SKILL.md` 及辅助文件 | 官方文档列出的本地目录为 `~/.qwenworkcn/skills/`。也可以在对话中提供开源仓库地址，让它下载并安装；Gitee 地址是否可直接拉取取决于当前网络与版本。 |
| Trae / TraeCode | 支持 | 「设置」→「技能与命令」→「创建」→选择全局/项目→导入 `SKILL.md` 或包含技能文件的 ZIP；也可从插件市场安装 | 项目级：`.trae/skills/`。全局：macOS/Linux `~/.trae-cn/skills/`，Windows `%USERPROFILE%/.trae-cn/skills/`。当前官方 IDE 文档描述的是 TraeCode 的 Skill 能力，没有将其限定为 SOLO 模式。 |
| Qoder | 支持 | IDE 终端使用 Skills CLI，或手动放置 Skill 文件夹；IDE 会话、Quest 和 CLI 均支持 Skills | 用户级：`~/.qoder/skills/`；项目级：`.qoder/skills/`。 |

### Qoder 与 Trae：从 Gitee 安装

Vercel Skills CLI 当前列出 Qoder、Trae CN 为受支持的 Agent 目标。国内网络环境可以使用本仓库的 Gitee 源：

**Qoder（IDE / Quest / CLI）**

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent qoder
```

**Trae CN**

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent trae-cn
```

安装后在对应 Agent 的 Skill 列表中确认已加载，并测试它是否能读取六份题型规则文件。

### WorkBuddy：桌面端与手机端

桌面端可以通过「上传技能」导入本地技能包。用户级与项目级目录可以分别用于跨项目复用和当前项目协作；常见目录为：

```text
用户级：~/.workbuddy/skills/kaoyan-english-grader/
项目级：.workbuddy/skills/kaoyan-english-grader/
```

如果 WorkBuddy 当前版本通过通用 Agent Skill 目录发现技能，也可以将整个技能文件夹放在项目级 `.agents/skills/` 下。首次安装后按客户端提示刷新或重启，并在技能管理界面确认加载结果。

WorkBuddy 微信小程序是手机端入口。官方文档说明可以通过 SkillHub 安装技能包，并在对话输入框的「添加技能」入口中为当前对话启用技能。手机端的主要路径是 SkillHub，不应将其描述为支持从手机文件管理器直接导入任意 ZIP。

## 手机 App：市场使用与自定义导入的区别

| 产品 | 手机端已确认的 Skill 能力 | 自定义导入情况 |
|---|---|---|
| WorkBuddy 微信小程序 | 可通过 SkillHub 安装技能包，并在当前对话中添加技能 | 官方公开流程以 SkillHub 安装为主；未确认手机端可直接上传本地 `SKILL.md`/ZIP。 |
| 千问 App（含工作助理） | 手机端「工作助理」→「技能」可浏览和调用技能 | 目前公开资料确认的是技能广场使用；与桌面端千问办公（QwenWork）的本地 `SKILL.md` 上传能力分开看待。 |
| 腾讯元宝 App | 侧边栏「技能」可安装和使用平台技能 | 普通用户端以市场技能为主；任意本地 Skill 文件导入尚无公开依据。 |
| 脑花 | App Store 当前列出的 iPhone App 支持调用和沉淀个人 Skill，强调把协作流程、标准和方法转成可复用能力 | 属于应用内工作流沉淀；未确认可导入标准 Agent Skill 文件夹或 ZIP。当前 App Store 列表显示仅适用于 iPhone。 |
| 智图Claw | iPhone/iPad App 支持浏览、安装和管理技能包，并连接智图 Gateway | App Store 描述没有说明可从本地导入 ZIP/TAR.GZ；不要将技能市场能力等同于任意本地包导入。 |
| 灵犀·晓伴 | Android App 介绍包含「AI 工具与技能中心」及第三方技能扩展 | 已确认技能扩展能力，尚未找到标准 `SKILL.md` 或本地 ZIP 导入说明。 |
| AgentOS（艾嘿） | 产品介绍曾提及技能商店与自定义技能 | 当前上架状态存在不确定性；第三方商店追踪记录显示其 iOS 应用在 2026-10-07 前后已无法正常获取。此项仅作产品线索，暂不列为稳定安装目标。 |
| AionClaw | 官方网站介绍内置/社区 Skills，并支持手机聊天渠道远程联动桌面端 | 官方下载页列出 Windows、macOS 和云端服务，未确认有独立 Android/iOS App；应归为手机远程操控入口，而非手机原生 Skill 安装器。 |

## 本仓库 Skill 的导入要求

1. **保留完整目录。** 本 Skill 的结构是 `SKILL.md` 加 `references/` 下六份题型规则文件。通过支持 ZIP 的平台导入时，应把 `skills/kaoyan-english-grader/` 目录中的内容一起打包，并确保 ZIP 内的 `SKILL.md` 位于技能包根目录。
2. **单文件上传时补齐引用文件。** 对于只提供 `SKILL.md` 上传入口的平台，按平台要求同时上传 `references/` 中的六份 Markdown 文件；如果平台无法保留相对目录，需确认它是否支持读取辅助文件。
3. **市场型平台不要误判。** 腾讯元宝、千问 App 等手机端可以安装平台市场中的技能，但市场安装能力不等于可以把本仓库文件直接导入个人账号。
4. **安装后验证。** 分别提交英语一翻译、英语二大作文测试，确认 Agent 能读取对应规则文件、区分题型分值，并按中文输出批改结果。

## 官方文档与产品页面

- [豆包开放平台：Skill 接入指南](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide)
- [腾讯元宝：官方账号的技能安装入口说明](https://www.sina.cn/media/7914117279)
- [豆包：工作任务模式与自定义技能功能报道](https://www.ithome.com/0/992/607.htm)
- [WorkBuddy：技能安装与管理](https://cloud.tencent.com/document/product/1831/134432)
- [WorkBuddy：微信小程序简介](https://www.codebuddy.cn/docs/workbuddymini/quick-start/Overview)
- [WorkBuddy：小程序添加附件与技能](https://www.codebuddy.cn/docs/workbuddymini/features/Attachments-and-Skills)
- [千问办公：技能帮助文档](https://qwenwork.cn/docs/features/skills)
- [TraeCode：技能（Skill）](https://docs.trae.cn/ide_skills)
- [Qoder IDE：Skills](https://docs.qoder.com/zh/extensions/skills)
- [Qoder CLI：技能](https://docs.qoder.com/zh/cli/Skills)
- [Vercel Skills CLI：支持的 Agent 与目录](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [脑花 App Store 页面](https://apps.apple.com/cn/app/脑花-ai-全能助手/id6762169454)
- [智图Claw App Store 页面](https://apps.apple.com/cn/app/智图claw/id6760357112)
- [灵犀·晓伴 App Store 页面](https://apps.apple.com/cn/app/灵犀-晓伴/id6766031151)
- [千问 App：手机端工作助理技能入口说明](https://www.sina.cn/news/detail/5345244153646127.html)
- [AgentOS（艾嘿）：应用商店状态追踪](https://chrome-stats.com/d/id6759725374)
- [AionClaw 官方网站](https://www.aionclaw.cn/)
