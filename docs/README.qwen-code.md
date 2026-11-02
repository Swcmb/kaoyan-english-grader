<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Qwen Code：安装与使用

Qwen Code 支持 Agent Skills，可从项目目录、用户目录和扩展中发现技能。本指南对应 Qwen Code，不涉及千问手机 App 或 QwenWork。

## 通过 Skills CLI 安装

在项目根目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent qwen-code
```

用户级安装增加 `-g`。

## 手动安装路径

将完整技能目录复制到：

| 范围 | 首选目录 | 通用兼容目录 |
| --- | --- | --- |
| 项目级 | `.qwen/skills/kaoyan-english-grader/` | `.agents/skills/kaoyan-english-grader/` |
| 用户级 | `~/.qwen/skills/kaoyan-english-grader/` | `~/.agents/skills/kaoyan-english-grader/` |

若两处存在同名技能，Qwen Code 优先使用专属目录。保留 `SKILL.md` 与 `references/` 六份规则的相对位置。

## 调用与验证

1. 输入 `/skills` 查看可用技能。
2. 输入 `/kaoyan-english-grader`，或直接提出批改任务。
3. 分别测试英语一翻译和英语二图表作文。
4. 确认 Agent 读取了对应的 `references/` 文件。

技能未出现时检查目录深度：正确结构是“技能目录/`SKILL.md`”，不要将整个仓库再嵌套一层。

## 更新与卸载

Skills CLI 安装使用 `npx skills update`。手动安装时完整替换技能目录；卸载时只删除对应范围下的 `kaoyan-english-grader/`。

## 官方资料

- [Qwen Code：Agent Skills](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/)
- [Skills CLI：Qwen Code 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
