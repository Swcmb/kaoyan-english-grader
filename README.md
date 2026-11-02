<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 考研英语 AI 批改

**一个自包含的 Agent Skill，覆盖考研英语一、英语二翻译、大作文和小作文六类主观题。** 将完整评分规则直接写入一个 `SKILL.md`，支持标准 Agent Skills 目录安装，也支持平台提供的单文件 Skill 导入。

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPL--3.0-or-later-blue.svg)](LICENSE)
[![GitHub Releases](https://img.shields.io/github/v/release/Swcmb/kaoyan-english-grader?display_name=tag)](https://github.com/Swcmb/kaoyan-english-grader/releases)
[![GitHub Actions](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml/badge.svg)](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml)

> 所有分数均为备考训练用的模拟评价，不代表官方阅卷结果、官方评分细则或真实考试分数预测。

## 六类题型，一个完整 Skill

| 考试 | 题型 | 模拟满分 |
| --- | --- | ---: |
| 英语一 | 翻译（5 个划线句） | 10 分 |
| 英语一 | 大作文（B 节） | 20 分 |
| 英语一 | 小作文（A 节应用文） | 10 分 |
| 英语二 | 翻译 | 15 分 |
| 英语二 | 大作文（通常为图表作文） | 15 分 |
| 英语二 | 小作文（应用文） | 10 分 |

完整评分规则全部位于 [skills/kaoyan-english-grader/SKILL.md](skills/kaoyan-english-grader/SKILL.md)。Skill 只有一个主文件，不依赖外部评分规则目录、MCP 服务、远程资源或额外运行时。

## 批改能力

**翻译批改**按句子或意群分析原文，定位关键词义、句子主干、修饰关系、指代和逻辑信息。模拟采分点根据原文信息量划分，局部误译和漏译对应处理，并提供完整修改译文与复盘。

**作文批改**先核对题目任务、内容要点和切题性，再评价语言、结构、衔接、格式与语气。英语一大作文检查图画寓意和论证；英语二大作文核对图表对象、时间、单位、数据与主要趋势；小作文检查身份、对象、交际目的和必答要点。

一次完整批改可包含：

- 题目与任务核查，明确已完成、部分完成和缺失的信息。
- 模拟评分及具体依据，区分题型评分档位与局部错误。
- 逐句分析，标记必须修改的问题和可选优化。
- 完整修订稿，尽量保留准确、自然的原有表达。
- 针对性复盘，整理主要问题、可迁移表达和下一步练习重点。

## 安装

### 使用 Skills CLI

在支持标准 Agent Skills 的环境中运行：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
~~~

指定 Codex：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex
~~~

也可以使用 GitHub 源：

~~~bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
~~~

### 手动安装或导入文件

标准 Skill 目录结构：

~~~text
kaoyan-english-grader/
└── SKILL.md
~~~

支持标准 Agent Skills 目录的宿主，将 `skills/kaoyan-english-grader/` 放入其 Skill 发现路径。平台支持 ZIP 上传时，压缩完整 Skill 目录并保留目录名。平台明确只接受单个 Skill 文件时，可直接导入 `skills/kaoyan-english-grader/SKILL.md`。

安装后检查 Agent 是否发现并加载 Skill，再用英语一翻译和英语二大作文验证题型路由、评分满分、评分依据和输出结构。

### 三种平台能力需要区分

| 能力 | 说明 |
| --- | --- |
| 平台技能市场 | 安装市场真实上架的条目。只有能核验本项目发布者和来源时，才代表安装了本项目。 |
| 应用内创建 | 将六类评分规则迁移到产品内部指令或个人 Skill，并逐项核验；这属于平台内创建。 |
| 标准 Skill 文件导入 | 导入本仓库的 `SKILL.md` 或完整 Skill 目录，直接复用文件中的规则。 |

聊天附件、知识库上传和保存提示词不自动构成已安装 Skill。平台具体入口、目录和能力边界见[安装指南](docs/installation/README.md)。

## 使用示例

英语一翻译：

~~~text
请使用考研英语 AI 批改 Skill。
考试：英语一
题型：翻译
英文原文：（粘贴完整原文及上下文）
我的译文：（按题号粘贴译文）

请按英语一翻译规则模拟评分，逐句解释失分点，
提供完整修改版和针对性复盘。
~~~

英语二大作文：

~~~text
请使用考研英语 AI 批改 Skill。
考试：英语二
题型：大作文
题目与图表：（粘贴题目或上传清晰图片）
我的作文：（粘贴作文）

请先核实图表对象、时间、单位和主要数据，
再检查切题性，给出模拟评分、逐句修改、
完整修订稿和复盘。
~~~

## 评分边界

- 评分档位和翻译采分点均为训练用途的模拟参考，不是官方逐项扣分表。
- 翻译按英文原文和上下文判断，不因措辞不同于参考译文而直接扣分。
- 每项重要评价和扣分都应对应题目、原文、译文或图表证据。
- 正确、自然且符合语境的表达可以保留，不为追求复杂句或生僻词而强行改写。
- 图像、题目或上下文不完整时，明确说明评价范围和不确定性。
- 不猜测手写内容，不编造图表数据、经历或原文没有的信息。

## 项目结构

~~~text
kaoyan-english-grader/
├── skills/
│   └── kaoyan-english-grader/
│       └── SKILL.md
├── docs/
│   ├── installation/
│   └── standards/
├── .github/workflows/publish.yml
├── INSTALL.md
├── GEMINI.md
├── LICENSE
└── README.md
~~~

## 文档

- [文档中心](docs/README.md)
- [安装与平台选择](docs/installation/README.md)
- [Skills CLI 安装指南](docs/installation/skills-cli.md)
- [手机端使用渠道](docs/installation/mobile-apps.md)
- [Agent 安装与验收协议](INSTALL.md)
- [GitHub 内容写作与 Markdown 排版规范](docs/standards/github-content-writing.md)
- [公开开源项目文档规范](docs/standards/open-source-docs.md)
- [本机与私有项目文档规范](docs/standards/local-dev-docs.md)
- [第三方内容与许可证审查规范](docs/standards/third-party-license-review.md)
- [GitHub Releases 发布说明](docs/releasing.md)

## GitHub Releases

推送符合格式的版本标签后，GitHub Actions 创建 Release，并附加完整源码 ZIP、TAR.GZ 和 SHA-256 校验文件。

[查看 Releases](https://github.com/Swcmb/kaoyan-english-grader/releases) · [发布工作流](.github/workflows/publish.yml)

## License

本仓库原创内容采用 [GNU GPL-3.0-or-later](LICENSE)。第三方材料保留各自版权声明、许可证和必要通知。
