<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 考研英语 AI 批改

**面向考研英语（一）（二）主观题的双版本 Agent Skill。** 覆盖翻译、大作文和小作文六类题型，提供题型专属模拟评分、审题核查、逐句批改、全文修订和针对性复盘。

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPL--3.0--or-later-blue.svg)](LICENSE)
[![GitHub Releases](https://img.shields.io/github/v/release/Swcmb/kaoyan-english-grader?display_name=tag)](https://github.com/Swcmb/kaoyan-english-grader/releases)
[![GitHub Actions](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml/badge.svg)](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml)

> 所有分数均为备考训练用的模拟评价，不代表官方阅卷结果、官方评分细则或真实考试分数预测。

## 覆盖六类主观题

| 考试 | 题型 | 模拟满分 |
| --- | --- | ---: |
| 英语一 | 翻译（5 个划线句） | 10 分 |
| 英语一 | 大作文（B 节） | 20 分 |
| 英语一 | 小作文（A 节应用文） | 10 分 |
| 英语二 | 翻译 | 15 分 |
| 英语二 | 大作文（通常为图表作文） | 15 分 |
| 英语二 | 小作文（应用文） | 10 分 |

## 两个独立 Skill

| Skill | 仓库路径 | 规则组织 | 推荐场景 |
| --- | --- | --- | --- |
| 标准版 `kaoyan-english-grader` | `skills/kaoyan-english-grader/` | `SKILL.md` + 六份 `references/` | 默认推荐；平台能完整保留主文件和引用目录 |
| 完整版 `kaoyan-english-grader-full` | `skills/kaoyan-english-grader-full/SKILL.md` | 单个文件内嵌六类全部评分规则 | 兼容替代；平台只接受单个 Skill 文件 |

**标准版是首选。** 只有完整保留标准版的 `SKILL.md` 与 `references/` 目录，才能按项目原始结构直接读取和复用全部评分规则。完整版将六类规则合并进一个独立文件，不依赖外部引用，专门解决平台无法保留引用目录的问题。

支持标准 Skill 目录或完整目录 ZIP 的平台，应优先安装标准版。此类平台也可以安装完整版，但不推荐用完整版替代标准安装。只有平台无法完整保留主文件与引用目录、同时支持单个 `SKILL.md` 导入时，才选择完整版。

## 批改输出

一次完整批改包括审题与任务核查、模拟评分及依据、逐句问题定位、修改建议、完整修订稿和针对性复盘。翻译按句子或意群划分模拟采分点；作文先核查任务完成度和切题性，再评价语言、结构、格式与语气。

## 安装渠道与能力边界

平台技能市场、应用内创建、标准 Skill 文件导入和完整目录安装是不同能力：

- **平台技能市场：** 安装平台已经上架的技能条目。只有本项目真实出现在该市场时，才能通过市场安装本项目；市场中名称相似的技能不代表本项目已安装。
- **应用内创建：** 在产品内部创建指令、工作流或个人 Skill。需要把六类评分规则迁移到平台格式，并逐项核对；这不等于原样导入标准 Skill。
- **标准 Skill 文件导入：** 平台明确支持 Agent Skills 文件格式时，按其要求导入。能保留目录时使用标准版；只接受单个 `SKILL.md` 时使用完整版。
- **完整目录安装：** 安装标准版时必须同时保留主文件和 `references/` 六份评分规则。这是直接复用项目原始评分规则的标准路径。

### 推荐：安装标准版

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

### 使用 Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

指定 Codex：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex
```

用户级安装增加 `-g`。只有确实需要单文件版本时，才将 Skill 名称改为 `kaoyan-english-grader-full`。详见 [Skills CLI 安装指南](docs/installation/skills-cli.md)。

## 使用示例

英语一翻译：

```text
请使用考研英语 AI 批改 Skill。
考试：英语一
题型：翻译
英文原文：（粘贴完整原文及上下文）
我的译文：（按题号粘贴译文）
请按英语一翻译规则模拟评分，逐句解释失分点，提供完整修改版和针对性复盘。
```

英语二大作文：

```text
请使用考研英语 AI 批改 Skill。
考试：英语二
题型：大作文
题目与图表：（粘贴题目或上传清晰图片）
我的作文：（粘贴作文）
请先核实图表对象、时间、单位和主要数据，再检查切题性，给出模拟评分、逐句修改、完整修订稿和复盘。
```

## 评分边界

- 评分档位和翻译采分点均为训练用途的模拟参考。
- 翻译按英文原文和上下文判断，不因措辞不同于参考译文而直接扣分。
- 每项重要评价和扣分应对应题目、原文、译文或图表证据。
- 正确、自然且符合语境的表达可以保留。
- 图像、题目或上下文不完整时，明确说明评价范围和不确定性。
- 不猜测手写内容，不编造图表数据、经历或原文没有的信息。

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
│   ├── installation/
│   ├── standards/
│   └── releasing.md
├── .github/workflows/publish.yml
├── INSTALL.md
├── GEMINI.md
├── LICENSE
└── README.md
```

## 文档

- [文档中心](docs/README.md)
- [安装与版本选择](docs/installation/README.md)
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
