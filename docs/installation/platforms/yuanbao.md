<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# 腾讯元宝：技能市场与专属智能体

腾讯元宝提供技能浏览、安装和调用入口，也支持配置专属智能体。市场条目与个人智能体配置属于不同能力。

## 安装与使用

### 安装市场技能

1. 更新元宝 App 或电脑端并登录。
2. 打开侧边栏的 **技能**。
3. 进入 **全部**，按类别浏览或搜索。
4. 查看详情、提供方和授权要求。
5. 按页面提示安装或使用。

### 配置专属智能体

当前版本提供技能或知识库配置时，进入智能体创建/编辑页面，填写角色和任务指令，选择平台已有能力，保存后用新对话测试。

## 能力边界

配置专属智能体不等于上传标准 Skill 文件夹。普通用户能否导入本地 `SKILL.md` 或完整 Skill 目录，以当前产品入口为准。元宝开放平台属于服务方接入与审核渠道，不是普通用户即时安装命令。

## 验收

检查技能状态，并分别测试英语一翻译和英语二大作文，确认完整规则、题型路由与模拟分值可用。

## 本项目 Skill

本仓库只提供一个自包含的标准 Agent Skill，六类题型的完整评分规则全部内嵌于 `skills/kaoyan-english-grader/SKILL.md`。安装时导入 `skills/kaoyan-english-grader/` 目录即可；平台明确只接受单文件时，直接导入该目录中的 `SKILL.md`。该 Skill 不依赖额外的规则文件或运行时服务。

## 官方资料

- [元宝官方：技能上新与安装步骤](https://weibo.com/2/detail/5354654420435913)
- [元宝技能入口与调用介绍](https://www.xmsumi.com/detail/4386)
