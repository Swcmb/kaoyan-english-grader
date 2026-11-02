<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

<div align="center">

# 考研英语 AI 批改

**面向考研英语一、英语二六类主观题的双版本 Agent Skill**

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPL--3.0--or-later-blue.svg)](LICENSE)
[![GitHub Releases](https://img.shields.io/github/v/release/Swcmb/kaoyan-english-grader?display_name=tag)](https://github.com/Swcmb/kaoyan-english-grader/releases)
[![GitHub Actions](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml/badge.svg)](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml)

<img src="docs/assets/hero.png" alt="Kaoyan English Grader — AI-powered English Exam Evaluation" width="100%">

<p>
  <a href="#快速开始">快速开始</a> ·
  <a href="#支持题型">支持题型</a> ·
  <a href="#两个独立-skill">两个独立 Skill</a> ·
  <a href="#核心能力">核心能力</a> ·
  <a href="#安装方式">安装方式</a> ·
  <a href="#使用案例分享">使用案例</a> ·
  <a href="docs/README.md">文档</a>
</p>

</div>

> **评分说明：** 所有分数均为考研备考训练用的模拟评价，不代表官方阅卷结果、官方评分细则或真实考试分数预测。

## 项目简介

考研英语 AI 批改（Kaoyan English Grader）是一个面向 AI Agent 的考研英语主观题批改 Skill，覆盖英语一和英语二的翻译、大作文及小作文六类题型。

项目提供两个独立 Skill：标准版采用 `SKILL.md` + `references/` 六份评分规则，完整版将六类评分规则全部内嵌到单个 `SKILL.md`。两个版本均包含题型判断、错误分析和完整批改流程，让支持 Agent Skills 的 AI Agent 按照统一的评价标准完成模拟批改。

**核心特点：**

- **双版本 Skill：** 标准版保留 `SKILL.md` 与 `references/` 目录，完整版单文件内嵌全部规则。
- **六类题型：** 覆盖考研英语一、英语二翻译、大作文和小作文。
- **完整评分规则：** 评分标准可直接查看、维护和复用。
- **证据驱动：** 重要评价和失分判断对应具体的题目、原文、译文或图表信息。
- **完整反馈：** 提供模拟评分、逐句分析、修改建议、完整修订稿和针对性复盘。
- **跨平台复用：** 支持标准 Agent Skills 目录安装，以及平台提供的单文件 Skill 导入。
- **自包含设计：** 完整版不依赖外部评分规则目录、MCP 服务、远程资源或额外运行时；标准版按原始目录结构复用全部规则。

## 快速开始

使用 [Skills CLI](https://skills.sh/) 安装标准版 `kaoyan-english-grader`。

**GitHub：**

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader --skill kaoyan-english-grader
```

**Gitee：**

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader
```

指定安装到 Codex（GitHub 示例；使用 Gitee 时替换为上方 Gitee 地址）：

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent codex
```

用户级安装增加 `-g`。只有确实需要单文件版本时，才将 Skill 名称改为 `kaoyan-english-grader-full`。

安装完成后，在支持 Agent Skills 的 AI Agent 中提交作文或翻译，并指定使用 `kaoyan-english-grader` Skill，即可开始批改。

## 支持题型

覆盖考研英语一和英语二的六类主观题。

| 考试   | 题型                     | 模拟满分 |
| :----- | :----------------------- | -------: |
| 英语一 | 翻译（5 个划线句）       |    10 分 |
| 英语一 | 大作文（B 节）           |    20 分 |
| 英语一 | 小作文（A 节应用文）     |    10 分 |
| 英语二 | 翻译                     |    15 分 |
| 英语二 | 大作文（通常为图表作文） |    15 分 |
| 英语二 | 小作文（应用文）         |    10 分 |

标准版评分规则收录于：

[`skills/kaoyan-english-grader/SKILL.md`](skills/kaoyan-english-grader/SKILL.md) 及 `references/` 下六份题型规则。

完整版评分规则收录于：

[`skills/kaoyan-english-grader-full/SKILL.md`](skills/kaoyan-english-grader-full/SKILL.md)。

## 两个独立 Skill

| Skill | 仓库路径 | 规则组织 | 推荐场景 |
| :--- | :--- | :--- | :--- |
| 标准版 `kaoyan-english-grader` | `skills/kaoyan-english-grader/` | `SKILL.md` + 六份 `references/` | 默认推荐；平台能完整保留主文件和引用目录 |
| 完整版 `kaoyan-english-grader-full` | `skills/kaoyan-english-grader-full/SKILL.md` | 单个文件内嵌六类全部评分规则 | 兼容替代；平台只接受单个 Skill 文件 |

**标准版是首选。** 只有完整保留标准版的 `SKILL.md` 与 `references/` 目录，才能按项目原始结构直接读取和复用全部评分规则。完整版将六类规则合并进一个独立文件，不依赖外部引用，专门解决平台无法保留引用目录的问题。

支持标准 Skill 目录或完整目录 ZIP 的平台，应优先安装标准版。此类平台也可以安装完整版，但不推荐用完整版替代标准安装。只有平台无法完整保留主文件与引用目录、同时支持单个 `SKILL.md` 导入时，才选择完整版。

## 核心能力

### 翻译批改

围绕英文原文及上下文，对译文进行逐句或按意群分析。

- **语义分析：** 定位关键词义、核心信息、逻辑关系和指代对象。
- **句法分析：** 拆解句子主干、从句、修饰成分及复杂结构。
- **采分点分析：** 根据原文信息量划分模拟采分点，识别误译、漏译和语义偏差。
- **译文修订：** 提供完整修改译文，保留准确、自然的原有表达。
- **错题复盘：** 总结失分原因、关键表达和可迁移的翻译方法。

### 作文批改

先核对题目要求和写作任务，再评价内容、语言、结构及表达效果。

| 题型             | 重点检查内容                                       |
| :--------------- | :------------------------------------------------- |
| 英语一大作文     | 图画信息、寓意理解、主题表达、论证与语言           |
| 英语二大作文     | 图表对象、时间、单位、数据准确性、主要趋势与比较   |
| 英语一、二小作文 | 写作身份、收件对象、交际目的、必答要点、格式与语气 |

### 完整批改反馈

一次完整批改可以提供以下内容：

1. **任务核查：** 确认题目要求，区分已完成、部分完成和缺失的信息。
2. **模拟评分：** 给出分数、评分档位和具体评价依据。
3. **逐句分析：** 定位语法、词汇、搭配、逻辑和表达问题，区分必须修改与可选优化。
4. **完整修订稿：** 提供修改后的译文或作文，尽量保留原文中准确且自然的表达。
5. **针对性复盘：** 整理主要失分原因、值得保留的表达、可迁移的语言素材和下一步练习重点。

## 使用示例

### 英语一翻译

```text
请使用考研英语 AI 批改 Skill。

考试：英语一
题型：翻译
英文原文：（粘贴完整原文及上下文）
我的译文：（按题号粘贴译文）

请按照英语一翻译规则进行模拟评分，
逐句解释失分点，提供完整修改译文，
并进行针对性复盘。
```

### 英语二大作文

```text
请使用考研英语 AI 批改 Skill。

考试：英语二
题型：大作文
题目与图表：（粘贴题目或上传清晰图片）
我的作文：（粘贴作文）

请先核实图表对象、时间、单位和主要数据，
再评价切题性、内容、语言和结构。

给出模拟评分、逐句修改、完整修订稿和针对性复盘。
```

## 使用案例分享

以下为外部平台上的分享案例，仅用于展示不同 AI Agent/平台中的使用流程与批改输出形态。链接可访问性、页面内容及分享状态由对应平台和分享者控制；案例中的评分仍属于训练用模拟评价，不代表官方阅卷结果。

| 平台 | 案例链接 |
| :--- | :--- |
| 豆包 | [查看案例](https://www.doubao.com/thread/x2JUY1OVNn1nJwsKa) |
| DeepSeek | [查看案例](https://chat.deepseek.com/share/gscicu2sygm0bgantm) |
| ChatGPT | [查看案例](https://chatgpt.com/share/6ae858d6-7298-83e9-b0a9-0c1233efcd62) |
| Trae | [查看案例](https://share.traecontent.cn/share/.HSEGS3O66C0J7?enter_from=pc) |
| Grok | [查看案例](https://grok.com/share/c2hhcmQtNA_4470c6e2-96df-47e2-a704-78a21c2badb7) |
| ChatGLM | [查看案例](https://chatglm.cn/share/7FpgHWiE) |
| Kimi | [查看案例](https://www.kimi.com/share/1a19b9c5-cef2-8042-8000-0000e812461c) |
| WorkBuddy | [查看案例](https://www.workbuddy.link/p/Tv43s0sCbLxhLLmb1Cyta2) |

> 若链接无法打开，可能是分享已过期、需要登录或被平台限制访问。请以本地安装后的实际批改结果为准。

## 安装方式

本项目提供标准 Agent Skill 文件。根据宿主平台的能力，可以选择以下安装方式。

### 1. 使用 Skills CLI

推荐通过 [Skills CLI](https://skills.sh/) 从 GitHub 或 Gitee 安装标准版。

**GitHub：**

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader --skill kaoyan-english-grader
```

**Gitee：**

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader
```

**指定 Codex（GitHub 示例）：**

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent codex
```

使用 Gitee 时，将地址替换为 `https://gitee.com/ianwusb/kaoyan-english-grader.git`。用户级安装增加 `-g`。只有确实需要单文件版本时，才将 Skill 名称改为 `kaoyan-english-grader-full`。详见 [Skills CLI 安装指南](docs/installation/skills-cli.md)。

### 2. 推荐：安装标准版

将下列指令交给支持标准 Agent Skills 的助手：

```text
请安装 Git 仓库中的「考研英语 AI 批改」标准版 Skill。

GitHub：https://github.com/Swcmb/kaoyan-english-grader
Gitee：https://gitee.com/ianwusb/kaoyan-english-grader

安装 skills/kaoyan-english-grader/ 完整目录，保留 SKILL.md 和 references/ 下六份评分规则。
先检查目标目录是否存在同名技能，再使用当前 Agent 支持的安装方式。
安装后验证主文件、六份规则和技能发现状态，并报告实际路径。
```

也可以让 Agent 读取 [INSTALL.md](INSTALL.md) 并执行安装协议。

### 3. 手动安装或导入文件

标准版目录结构：

```text
kaoyan-english-grader/
├── SKILL.md
└── references/
    └── （六份题型评分规则）
```

完整版目录结构：

```text
kaoyan-english-grader-full/
└── SKILL.md
```

将仓库中的对应目录放入宿主平台支持的 Skill 发现目录。根据平台支持的导入方式：

- **目录安装：** 标准版必须将完整的 `kaoyan-english-grader/` 目录放入 Skill 发现路径，同时保留 `SKILL.md` 和 `references/`。
- **ZIP 导入：** 压缩完整 Skill 目录，并保留目录名称和内部文件结构。支持标准目录时优先导入标准版。
- **单文件导入：** 平台明确只接受单个 Skill 文件时，导入完整版 `kaoyan-english-grader-full/SKILL.md`。

### 4. 区分不同的平台能力

平台技能市场、应用内创建、标准 Skill 文件导入和完整目录安装属于不同的能力。

| 方式                | 实际含义                                                     |
| :------------------ | :----------------------------------------------------------- |
| 平台技能市场        | 安装市场实际发布的条目。需要核验条目发布者与仓库来源。只有本项目真实出现在该市场时，才能通过市场安装本项目。 |
| 应用内创建          | 将评分规则迁移到产品内部指令或个人 Skill，需要逐项核验规则是否完整。这不等于原样导入标准 Skill。 |
| 标准 Skill 文件导入 | 平台明确支持 Agent Skills 文件格式时，按其要求导入。能保留目录时使用标准版；只接受单个 `SKILL.md` 时使用完整版。 |
| 完整目录安装        | 安装标准版时必须同时保留主文件和 `references/` 六份评分规则。这是直接复用项目原始评分规则的标准路径。 |

聊天附件、普通知识库上传和保存提示词不自动构成已安装 Skill。

不同平台的安装入口、目录要求和能力边界见[安装与平台选择](docs/installation/README.md)。

### 5. 验证安装

安装后，确认 Agent 已发现并加载 Skill，再分别使用英语一翻译和英语二大作文进行测试。

重点检查：

- 是否正确识别考试类型和题型。
- 是否使用对应题型的模拟满分。
- 是否按照 Skill 中的评分规则给出评价。
- 评分依据是否对应具体的题目和作答内容。
- 标准版是否保留 `SKILL.md` 与 `references/` 六份规则。
- 是否能够提供逐句修改、完整修订稿和复盘。

## 评分原则

本项目强调有依据的模拟评价和可执行的修改建议。

- **模拟参考：** 评分档位和翻译采分点服务于备考训练，不构成官方逐项扣分表。
- **原文优先：** 翻译依据英文原文和上下文判断，不因表达不同于参考译文而直接扣分。
- **证据对应：** 每项重要评价和失分判断都应有题目、原文、译文或图表信息作为依据。
- **保留有效表达：** 正确、自然且符合语境的表达可以保留，不为了复杂句式或生僻词而强行改写。
- **明确不确定性：** 图片、题目或上下文不完整时，应说明评价范围和不确定性。
- **拒绝无依据推断：** 不猜测无法辨认的手写内容，不编造图表数据、个人经历或原文没有的信息。

## 项目结构

```text
kaoyan-english-grader/
├── skills/
│   ├── kaoyan-english-grader/
│   │   ├── SKILL.md
│   │   └── references/             # 六类题型规则
│   └── kaoyan-english-grader-full/
│       └── SKILL.md                # 六类规则全部内嵌
├── docs/
│   ├── assets/
│   │   └── hero.png
│   ├── installation/
│   └── standards/
├── .github/
│   └── workflows/
│       └── publish.yml
├── INSTALL.md
├── GEMINI.md
├── LICENSE
└── README.md
```

## 文档

| 文档                                                         | 内容                             |
| :----------------------------------------------------------- | :------------------------------- |
| [文档中心](docs/README.md)                                   | 项目文档索引                     |
| [安装与平台选择](docs/installation/README.md)                | 不同平台的安装方法与能力边界     |
| [Skills CLI 安装指南](docs/installation/skills-cli.md)       | 使用 Skills CLI 安装和管理 Skill |
| [手机端使用渠道](docs/installation/mobile-apps.md)           | 手机端的使用方式                 |
| [Agent 安装与验收协议](INSTALL.md)                           | 安装要求与验收标准               |
| [GitHub 内容写作与 Markdown 排版规范](docs/standards/github-content-writing.md) | GitHub 内容组织和 Markdown 规范  |
| [公开开源项目文档规范](docs/standards/open-source-docs.md)   | 公开项目文档编写规范             |
| [本机与私有项目文档规范](docs/standards/local-dev-docs.md)   | 本机与私有项目的文档规范         |
| [第三方内容与许可证审查规范](docs/standards/third-party-license-review.md) | 第三方内容与许可证审查           |
| [GitHub Releases 发布说明](docs/releasing.md)                | 版本发布与发布说明               |

## GitHub Releases

推送符合格式的版本标签后，GitHub Actions 创建 Release，并附加完整源码 ZIP、TAR.GZ 和 SHA-256 校验文件。

[查看 Releases](https://github.com/Swcmb/kaoyan-english-grader/releases) · [发布工作流](.github/workflows/publish.yml)

## License

本仓库原创内容采用 [GNU General Public License v3.0 or later](LICENSE)。

第三方材料保留各自版权声明、许可证及必要通知。

---

<div align="center">

[GitHub Repository](https://github.com/Swcmb/kaoyan-english-grader) · [Gitee Repository](https://gitee.com/ianwusb/kaoyan-english-grader) · [Releases](https://github.com/Swcmb/kaoyan-english-grader/releases) · [发布工作流](.github/workflows/publish.yml)

</div>
