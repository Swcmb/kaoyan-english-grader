<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# WorkBuddy 桌面端：安装与使用

WorkBuddy 提供技能搜索、技能创建和本地技能包上传。本项目依赖六份引用规则，目录版上传时应保留完整目录。

## 安装与使用

### 准备 ZIP

将 `skills/kaoyan-english-grader/` 整个目录压缩为 ZIP：

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

### 上传

1. 打开 WorkBuddy 桌面客户端并登录。
2. 进入 **专家·技能·连接器**。
3. 点击 **添加技能 → 上传技能**。
4. 选择 ZIP 并等待解析完成。
5. 在技能列表确认技能出现并启用。

只接收单个文件时，使用[内嵌六类规则的完整单文件版本](../../../dist/kaoyan-english-grader-single-file/SKILL.md)。

## 能力边界

技能搜索用于发现已有条目，创建用于封装平台内工作流，上传用于导入本地文件，三者是不同能力。更新时重新上传最新完整包，并通过实际任务验证六类规则。

## 验收

检查技能状态，并分别测试英语一翻译和英语二大作文，确认完整规则、题型路由与模拟分值可用。

## 本仓库的 Skill 版本选择

若当前导入入口能保留完整目录或 ZIP 内的相对路径，使用标准版 `skills/kaoyan-english-grader/`，确保 `SKILL.md` 与 `references/` 六份规则完整保留。若产品实际只接受单个标准 `SKILL.md` 文件，再使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。技能市场条目、应用内创建和本地文件导入属于不同流程；市场安装要求本项目已真实上架，应用内创建则需手动迁移并核对规则。

## 官方资料

- [WorkBuddy：技能安装与管理](https://cloud.tencent.com/document/product/1831/134432)
