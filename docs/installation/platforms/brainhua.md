<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# 脑花 App：创建与沉淀个人 Skill

脑花的 Skill 能力侧重将协作中验证有效的流程、标准和方法沉淀为个人可复用能力。此流程属于应用内创建。

## 安装与使用

1. 在 iPhone App Store 搜索“脑花 - AI 全能助手”，或打开官方页面。
2. 安装并登录。
3. 选择一项重复执行的任务，如作文批改或结构化报告。
4. 与脑花完成任务，明确输入、判断标准、步骤和输出。
5. 检查结果后，将验证过的流程沉淀为个人 Skill。

创建时可以说明：覆盖英语一、英语二的翻译、大作文和小作文；先识别考试与题型；所有分数均为练习模拟评价；输出中文讲解、评分依据、修订稿和复盘。

## 安装边界

公开 App Store 介绍确认应用内 Skill 能力，但未说明支持标准 Agent Skill 文件夹或 ZIP 导入。应用内创建产生的是平台内部 Skill。若用本项目规则创建，应逐项核对六类档位、输出要求和边界。

## 验收

检查技能是否出现在目标产品的技能列表，并分别提交英语一翻译和英语二大作文测试。确认题型路由、分值、对应规则和输出结构正确。上传成功或保存成功不能替代实际调用验证。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`，不依赖额外的规则文件或运行时服务。目录安装时导入 `skills/kaoyan-english-grader/`；平台明确只接受单文件时，导入该目录中的 `SKILL.md`。

## 官方资料

- [脑花：App Store](https://apps.apple.com/cn/app/%E8%84%91%E8%8A%B1-ai-%E5%85%A8%E8%83%BD%E5%8A%A9%E6%89%8B/id6762169454)
