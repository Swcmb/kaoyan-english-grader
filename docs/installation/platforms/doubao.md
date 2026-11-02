<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# 豆包桌面端：创建、导入与开发者上架

豆包桌面端涉及个人技能创建、本地文件导入以及服务方通过开放平台提交审核三种流程，安装对象和使用渠道不同。

## 安装与使用

### 创建个人 Skill

1. 打开豆包电脑版并进入 **工作任务**。
2. 打开侧边栏技能入口，选择创建技能。
3. 填写名称、用途、执行指令、输入要求和输出格式。
4. 保存后在技能列表检查状态，再在工作任务中测试。

### 导入本地 Skill

若当前客户端提供本地导入入口，进入技能管理，选择导入或上传。目录版应包含 `SKILL.md` 和完整 `references/`；只接受单文件时使用[完整单文件版本](../../../dist/kaoyan-english-grader-single-file/SKILL.md)。

### 开发者提交市场审核

服务方需按开放平台资质和技能资源包规范创建技能、提交材料并等待审核；审核通过并发布后，终端用户才能从市场发现该技能。

## 能力边界

个人创建不等于导入标准目录；开发者上架也不是普通用户的即时安装命令。ZIP 限制和入口会随平台规范调整，提交前以最新官方文档为准。

## 验收

检查技能是否出现在目标产品中，并分别测试英语一翻译和英语二大作文。核对题型路由、评分档位、引用规则和输出要求。上传或保存成功不能替代真实任务验证。

## 官方资料

- [豆包开放平台：Skill 接入指南](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide)
- [豆包工作：技能与连接器介绍](https://www.feishu.cn/content/article/7677519271848610746)
