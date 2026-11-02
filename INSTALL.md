<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Agent 安装与验收协议

用户要求安装本项目时，读取并执行本协议。具备相应工具和权限时，直接完成安装与验证，并报告真实结果。

## 项目与 Skill

| 项目 | 内容 |
| --- | --- |
| GitHub | https://github.com/Swcmb/kaoyan-english-grader |
| Gitee | https://gitee.com/ianwusb/kaoyan-english-grader |
| Skill 名称 | `kaoyan-english-grader` |
| Skill 目录 | `skills/kaoyan-english-grader/` |
| Skill 主文件 | `skills/kaoyan-english-grader/SKILL.md` |

本仓库只提供一个自包含的标准 Agent Skill。英语一、英语二翻译、大作文和小作文六类题型的评分规则全部写在同一个 `SKILL.md` 中，不依赖额外的评分规则文件、远程资源、MCP 服务或外部运行时。

默认只安装本项目 Skill，不安装仓库级开发配置、其他插件或无关文件。

## 先识别平台提供的能力

| 能力 | 实际对象 | 本项目的处理方式 |
| --- | --- | --- |
| 平台技能市场 | 平台已经上架的技能条目 | 只有市场中真实存在且能核验来源的项目条目，才通过市场安装 |
| 应用内创建 | 产品内部指令、工作流或个人 Skill | 将本 Skill 的规则迁移到平台格式，逐项核对六类题型，并标记为平台内创建版本 |
| 标准 Agent Skill 导入 | 平台识别的标准 Skill 文件或目录 | 按平台要求导入本项目的完整 Skill 目录 |
| ZIP 文件上传 | 平台接受的 Skill 压缩包 | ZIP 内保留 `kaoyan-english-grader/SKILL.md` 的目录结构 |
| 单文件导入 | 平台明确提供的单文件 Skill 导入入口 | 导入完整的 `skills/kaoyan-english-grader/SKILL.md` |

**市场、应用内创建和文件导入是不同能力。** 普通聊天附件、知识库文件或保存的提示词不自动构成已安装 Skill。市场中名称相似的技能也不代表本项目已上架。

## 安装决策

1. **支持标准 Agent Skills 目录：** 安装 `skills/kaoyan-english-grader/`，目录中包含唯一的完整 `SKILL.md`。
2. **支持 ZIP 上传：** 将 `skills/kaoyan-english-grader/` 目录打包，保留目录名和主文件。
3. **只支持单个标准 `SKILL.md` 导入：** 导入 `skills/kaoyan-english-grader/SKILL.md`。
4. **只有技能市场：** 检查市场是否真实上架本项目；未上架时不能声称已安装本项目。
5. **只有应用内创建：** 按平台内部格式迁移规则，核对六类题型的评分档位、评分要求、输出结构和模拟评分边界。
6. **手机只提供远程 Agent 入口：** 在实际运行 Agent 的 Gateway 或主机安装 Skill；手机端只负责连接和交互。

## 安装流程

### 1. 识别宿主与安装范围

确认 Agent 或应用名称、版本、操作系统、Shell、工作区、可用安装器和权限。区分项目级与用户级；存在活动工作区且用户未指定范围时，优先项目级，否则按宿主官方文档选择用户级目录。

安装路径和命令必须来自宿主官方文档、原生安装器或已验证的当前版本，不得猜测。

### 2. 使用 Skills CLI

在支持 Vercel Skills CLI 的环境中，可从仓库安装：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent <verified-agent-id>
~~~

也可以使用 GitHub 源：

~~~bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent <verified-agent-id>
~~~

Agent ID 以 CLI 当前官方清单为准。用户级安装按 CLI 当前版本增加 `-g`。执行前检查 `npx skills --help` 和官方 Agent 清单。

### 3. 手动安装或上传

标准 Skill 目录结构：

~~~text
kaoyan-english-grader/
└── SKILL.md
~~~

将整个目录放到宿主官方文档指定的 Skill 发现路径。若平台提供 ZIP 上传，则压缩时保留 `kaoyan-english-grader/` 作为目录根；若平台明确提供单文件上传入口，可以直接上传 `SKILL.md`。

平台要求的目录层级、ZIP 根目录和重新加载方式可能不同。按具体宿主指南执行，不要将聊天附件上传误认为 Skill 安装。

### 4. 保护已有文件

安装前检查目标目录。只有确认现有副本来自本仓库且适合更新时才替换。遇到来源不明或内容不同的同名目录，停止覆盖并报告冲突。

不得删除其他 Skill、修改无关配置、执行仓库中的无关脚本，或申请安装所不需要的高权限。

### 5. 验证安装

检查以下项目：

- Skill 目录和 `SKILL.md` 文件存在，文件内容完整。
- 相应 Agent 能发现并加载 `kaoyan-english-grader`。
- 六类题型均能正确识别并读取各自规则。
- 英语一翻译能够按 10 分制批改。
- 英语二大作文能够按 15 分制完成图表核查、模拟评分和修订。
- 输出包含对应题型要求的评分依据、逐句分析、修改稿或复盘。
- 所有分数均明确标记为练习模拟评价。

CLI 退出码、上传成功提示或下载完成不等于安装验收通过。应用内创建的版本还需逐项对照六类规则，并明确标记为平台内部实现。

## 更新与卸载

更新前确认来源和版本。标准目录安装时更新整个 Skill 目录；单文件导入时替换完整 `SKILL.md`；平台内创建版本按产品的编辑与版本管理流程更新。

卸载前确认范围和路径，只移除本项目对应副本，不影响其他 Skill。

## 完成报告

报告实际使用的平台与版本、安装渠道、项目级或用户级范围、实际路径、文件检查结果、Agent 发现状态、题型验证结果和仍需用户完成的操作。

未通过检查时说明具体阻塞点。不得将市场中相似技能、部分下载或未经验证的副本报告为本项目安装成功。
