<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# 豆包 App：手机端使用技能

豆包手机端主要用于调用账号当前可用的技能。个人技能创建和本地文件管理以电脑版工作任务模式及当前客户端能力为准。

## 安装与使用

1. 更新并打开豆包 App。
2. 登录与电脑版相同的账号。
3. 在对话或功能入口选择账号可用的技能。
4. 按技能要求提供资料和必要授权。
5. 检查返回结果中的数据、事实和执行内容。

需要创建或导入个人技能时，使用豆包电脑版技能管理入口，再确认同一账号是否同步到手机端。

## 能力边界

手机端附件上传属于任务资料输入，不代表安装了 Skill。普通用户从手机文件系统导入标准 Skill 目录或 ZIP 的流程尚未确认。

## 验收

检查技能是否出现在目标产品中，并分别测试英语一翻译和英语二大作文。核对题型路由、评分档位、引用规则和输出要求。上传或保存成功不能替代真实任务验证。

## 本仓库的 Skill 版本选择

技能市场只安装平台实际上架的条目；只有能够核验本项目的发布者和来源时，才能称为安装了本项目。应用内创建生成平台内部 Skill，需要将六类评分规则迁移并逐项核对，不能视为标准文件导入。若当前版本明确支持标准 Skill 目录或完整 ZIP，优先安装标准版；若只能导入单个标准 `SKILL.md`，使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。支持标准目录的平台也可安装完整版，但不推荐替代标准版。

## 官方资料

- [豆包开放平台：Skill 接入指南](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide)
- [豆包工作任务模式技能功能介绍](https://www.sina.cn/news/detail/5334379914069294.html)
