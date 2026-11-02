<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# QwenWork：安装与使用

QwenWork 提供技能广场、对话搜索、开源仓库获取和本地文件上传。本项目的六类题型评分规则全部内嵌在唯一的 `SKILL.md` 文件中。

## 安装与使用

### 本地 Skill 上传

1. 打开 QwenWork。
2. 进入 **扩展 → 技能**。
3. 点击 **Install Skill** 或当前页面提供的上传入口。
4. 上传完整的 `skills/kaoyan-english-grader/` 目录，或平台明确提供单文件导入时上传其中的 `SKILL.md`。
5. 等待导入完成，在已安装区域检查状态。

### 从仓库获取

在 QwenWork 对话或仓库获取入口中，可以提供以下指令：

~~~text
请从这个仓库获取考研英语批改 Skill：
https://gitee.com/ianwusb/kaoyan-english-grader.git

只安装 skills/kaoyan-english-grader。
该目录中的 SKILL.md 已包含英语一、英语二六类题型的完整评分规则。
安装后报告实际路径，并验证英语一翻译和英语二大作文。
~~~

也可以在技能广场搜索并安装平台已有条目。市场条目与本地文件导入是不同渠道。

## 能力边界

技能广场安装的是平台收录条目；本地上传和从仓库获取是独立渠道。项目 Skill 是自包含文件，不需要额外的评分规则文件或运行时服务。实际可用的上传格式和入口以当前 QwenWork 客户端为准。

## 验收

确认技能出现在目标产品的已安装列表，并分别测试英语一翻译和英语二大作文，核对题型路由、模拟分值、评分依据和输出要求。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。

## 官方资料

- [QwenWork：Skills 官方文档](https://docs.qwenwork.ai/desktop/skills)
- [QwenWork：技能帮助文档](https://qwenwork.cn/docs/features/skills)
