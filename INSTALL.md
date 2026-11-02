<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Agent 安装协议

用户要求安装本项目时，读取并执行本协议。具备相应工具和权限时直接完成安装与验证，不要只复述教程。

## 仓库与 Skill

| 项目 | 内容 |
| --- | --- |
| GitHub | https://github.com/Swcmb/kaoyan-english-grader |
| Gitee | https://gitee.com/ianwusb/kaoyan-english-grader |
| 标准版 Skill | `skills/kaoyan-english-grader/` |
| 完整版 Skill | `skills/kaoyan-english-grader-full/SKILL.md` |
| 标准版名称 | `kaoyan-english-grader` |
| 完整版名称 | `kaoyan-english-grader-full` |

默认只安装本项目的一个 Skill，不安装仓库级开发配置、其他插件或无关文件。

## 先区分平台能力

| 能力 | 实际对象 | 本项目的处理方式 |
| --- | --- | --- |
| 平台技能市场 | 平台已上架的技能条目 | 只有市场中真实存在本项目条目时才从市场安装 |
| 应用内创建 | 产品内部指令、工作流或个人 Skill | 迁移规则并逐项核对六类题型，标记为平台内创建版本 |
| 标准 Skill 文件导入 | 平台识别的 Agent Skill 文件 | 按平台支持格式导入；能保留完整目录时优先使用标准版 |
| 完整目录安装 | 标准版主文件与引用目录 | 同时保留 `SKILL.md` 和 `references/` 六份规则，按原始结构直接复用全部评分规则 |
| 单文件 Skill 导入 | 一个独立的 `SKILL.md` | 平台无法保留目录、但支持单文件 Skill 导入时使用完整版 |

**标准版是默认选择。** 只有完整保留标准版主文件与引用目录，才能直接按项目原始结构读取全部评分规则。完整版将六类规则合并到一个文件中，作为目录结构受限时的兼容方案。支持标准 Skill 的平台也能安装完整版，但不推荐用它替代标准安装。

市场、应用内创建和文件导入属于不同能力。普通聊天附件、知识库文件或保存的提示词不自动构成已安装 Skill。

## 安装决策

1. **支持标准 Skill 目录或完整目录 ZIP：** 安装 `skills/kaoyan-english-grader/`，完整保留 `SKILL.md` 和 `references/`。
2. **只支持单个标准 `SKILL.md` 导入：** 安装 `skills/kaoyan-english-grader-full/SKILL.md`。
3. **只有技能市场：** 检查市场是否真实上架本项目；未上架时不能声称已安装本项目。
4. **只有应用内创建：** 按平台内部格式迁移规则，核对六类题型、评分档位、输出要求和边界；报告为平台内创建版本。
5. **手机只提供远程 Agent 入口：** 在实际运行 Agent 的 Gateway 或主机安装 Skill，手机端只负责连接和交互。

如果平台提供多个选项，优先采用原生标准目录导入，其次使用完整目录 ZIP；单文件完整版仅用于无法保留目录结构的情况。

## 安装流程

### 1. 识别宿主与安装范围

确认 Agent/应用名称、版本、操作系统、Shell、工作区、可用安装器和权限。区分项目级与用户级；存在活动工作区且用户未指定范围时，优先项目级，否则按宿主文档选择用户级目录。

安装路径和命令必须来自宿主官方文档、原生安装器或已验证的当前版本，不得猜测。

### 2. 安装标准版

默认目录结构：

```text
kaoyan-english-grader/
├── SKILL.md
└── references/
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
```

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent <verified-agent-id>
```

GitHub 源：

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent <verified-agent-id>
```

用户级安装选项按 CLI 当前版本增加 `-g`。执行前检查[官方 Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)和 `npx skills --help`。

### 3. 安装完整版

仅当平台无法完整保留标准版主文件与引用目录、但明确支持单个 `SKILL.md` Skill 导入时使用。

文件路径：`skills/kaoyan-english-grader-full/SKILL.md`。该文件内嵌六类题型的完整评分规则，不依赖外部文件。通过 Skills CLI 安装时使用 Skill 名称 `kaoyan-english-grader-full`。

支持标准目录的 Agent 可以安装完整版，但应优先保留标准版目录结构。

### 4. 保护已有文件

安装前检查目标目录。只有确认现有副本来自本仓库且适合更新时才替换。遇到来源不明或内容不同的同名目录，停止覆盖并报告冲突。

不得删除其他 Skill、修改无关配置、执行仓库中的无关脚本，或申请安装所不需要的高权限。

### 5. 验证安装

标准版检查主文件、六份引用文件、相对路径和 Agent 发现状态。完整版确认单文件完整导入，并检查六个题型章节均存在且可被调用。

分别测试英语一翻译与英语二大作文，核对题型路由、评分档位、评分依据和输出要求。CLI 退出码、上传成功提示或下载完成不等于安装验收通过。

应用内创建的版本还需逐项对照六类评分规则，并明确其为平台内部实现。

## 更新与卸载

更新前确认来源和版本。标准版整体更新主文件与引用目录；完整版整体替换单文件；平台内创建版本按产品的编辑和版本管理流程更新。卸载前确认范围和路径，只移除本项目对应副本。

## 完成报告

报告实际使用的平台与版本、安装渠道、所选 Skill 版本、选择原因、项目级或用户级范围、实际路径、文件检查结果、Agent 发现状态、两个题型的验证结果和仍需用户完成的操作。

未通过检查时说明具体阻塞点。不得将市场中相似技能、部分下载或未经验证的副本报告为本项目安装成功。
