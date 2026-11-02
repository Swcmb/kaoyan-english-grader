<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# WorkBuddy 桌面端：安装与使用

WorkBuddy 提供技能搜索、技能创建和本地技能包上传。本项目的六类题型完整评分规则均内嵌在一个 `SKILL.md` 文件中。

## 安装与使用

### 准备 ZIP

将 `skills/kaoyan-english-grader/` 整个目录压缩为 ZIP：

~~~text
kaoyan-english-grader/
└── SKILL.md
~~~

### 上传

1. 打开 WorkBuddy 桌面客户端并登录。
2. 进入 **专家·技能·连接器**。
3. 点击 **添加技能 → 上传技能**。
4. 选择 ZIP 并等待解析完成。
5. 在技能列表确认技能出现并启用。

只接收单个文件时，使用[本项目完整 Skill 文件](../../../skills/kaoyan-english-grader/SKILL.md)。

## 能力边界

技能搜索用于发现已有条目，创建用于封装平台内工作流，上传用于导入本地文件，三者是不同能力。更新时重新上传最新完整包，并通过实际任务验证六类规则。

## 验收

检查技能状态，并分别测试英语一翻译和英语二大作文，确认完整规则、题型路由与模拟分值可用。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [WorkBuddy：技能安装与管理](https://cloud.tencent.com/document/product/1831/134432)
