<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# 千问 App：手机端技能广场

千问 App 的工作助理提供技能入口，用户可从技能广场浏览和调用技能。手机端市场与桌面端 QwenWork 的文件导入分别管理。

## 安装与使用

1. 安装或更新千问 App 并登录。
2. 进入 **工作助理 → 技能**。
3. 点击 **更多技能** 进入技能广场。
4. 按分类浏览或搜索关键词。
5. 打开技能卡片，查看说明并按界面提示安装或调用。
6. 返回工作助理，使用匹配任务测试技能。

## 能力边界

公开资料确认手机端的技能浏览和调用入口，尚未确认普通用户可从手机文件系统导入任意第三方 `SKILL.md` 或 ZIP。需要完整规则时，使用桌面端 [QwenWork](qwenwork.md) 文件上传，或支持标准 Agent Skills 的开发工具。

## 验收

确认技能出现在目标产品的已安装列表，并分别测试英语一翻译和英语二大作文，核对对应规则、分值和输出要求。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [千问：手机端工作助理技能入口介绍](https://www.sina.cn/news/detail/5345244153646127.html)
- [千问 App Store 页面](https://apps.apple.com/cn/app/%E5%8D%83%E9%97%AE-%E9%98%BF%E9%87%8Cai%E5%8A%A9%E6%89%8B/id6466733523)
