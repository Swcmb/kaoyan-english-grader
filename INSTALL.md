<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Agent 安装协议

用户要求安装 `kaoyan-english-grader` 时，读取并执行本协议。具备相应工具和权限时直接完成安装与验证，不要只复述教程。

## 安装对象

| 项目 | 内容 |
| --- | --- |
| GitHub | https://github.com/Swcmb/kaoyan-english-grader |
| Gitee | https://gitee.com/ianwusb/kaoyan-english-grader |
| Skill 名称 | `kaoyan-english-grader` |
| 标准目录版 | `skills/kaoyan-english-grader/` |
| 单文件完整版本 | `dist/kaoyan-english-grader-single-file/SKILL.md` |

默认只安装本 Skill，不安装仓库级开发配置、其他插件或无关文件。

## 先区分安装能力

| 类型 | 实际安装对象 | 完整规则的获取方式 |
| --- | --- | --- |
| 标准 Skill 导入 | Skill 文件夹或完整 ZIP | 保留 `SKILL.md` 和 `references/` 六份文件 |
| 单文件 Skill 导入 | 独立 `SKILL.md` | 使用本仓库内嵌六类规则的单文件版本 |
| 平台技能市场 | 平台已上架的技能条目 | 只有本项目真实上架后才能直接安装 |
| 应用内创建 | 产品内部工作流、指令或个人技能 | 人工迁移并逐项核对六类规则 |
| 手机远程连接 Agent | 远程主机上的 Agent 与 Skill | Skill 在远程主机执行 |

技能市场、应用内创建和标准 Skill 文件导入是不同能力。不能根据名称相似、普通附件上传成功或个人 Skill 保存成功，推断本项目已经完整安装。

## 安装流程

### 1. 识别宿主和范围

确认 Agent、操作系统、Shell、工作区、可用安装器和权限。区分项目级与用户级；存在活动工作区且用户未指定范围时，优先项目级，否则使用宿主文档定义的用户级目录。

安装路径必须来自宿主官方文档、原生安装器或已验证的同类 Skill，不得猜测。

### 2. 选择目录版或单文件版

默认使用标准目录版，结构如下：

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

宿主只接受一个文件时，使用 `dist/kaoyan-english-grader-single-file/SKILL.md`。该文件已内嵌六类完整规则，不需要外部引用目录。

### 3. 选择实际支持的安装方式

1. **原生 Skill 管理器：** 宿主支持标准目录、仓库导入或完整 ZIP 时使用。
2. **Skills CLI：** Agent ID 必须来自当前官方支持清单。
3. **手动安装：** 将完整目录放入宿主已确认的发现路径。
4. **UI 文件导入：** 按平台要求选择完整目录 ZIP 或单文件版，检查辅助文件保留情况。
5. **应用内创建：** 无标准导入能力时，可将规则迁移至平台内部格式，但必须标记为平台内创建版本。

Skills CLI 示例：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent <verified-agent-id>
```

GitHub 源：

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent <verified-agent-id>
```

用户级安装选项按 CLI 当前版本增加 `-g`。执行前检查[官方 Agent 清单](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)和 `npx skills --help)。

### 4. 保护已有文件

安装前检查目标目录。只有确认现有副本来自本仓库且适合更新时才替换。遇到来源不明或内容不同的同名目录，停止覆盖并报告冲突。

不得删除其他 Skill、修改无关配置、执行仓库中的无关脚本，或申请安装所不需要的高权限。

### 5. 验证安装

目录版检查主文件、六份引用文件、相对路径和 Agent 发现状态。单文件版确认文件完整导入，并分别测试英语一翻译和英语二大作文，核对题型路由、评分档位和输出要求。

CLI 退出码、上传成功提示或下载完成不等于安装验收通过。

## 更新和卸载

更新前确认来源和版本。目录版整体更新主文件与引用目录；单文件版整体替换文件。卸载前确认范围和路径，只移除本 Skill 对应副本。

## 完成报告

报告所用安装方法、选择原因、项目级或用户级范围、实际路径、文件检查结果、Agent 发现状态、两个题型的验证结果和仍需用户完成的操作。

未通过检查时说明具体阻塞点。不得将部分下载或未经验证的副本报告为安装成功。
