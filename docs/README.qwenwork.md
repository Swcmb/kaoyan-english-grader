<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 千问办公（QwenWork）：安装与使用

QwenWork 支持从技能广场安装技能、在对话中搜索技能，也支持上传本地 `SKILL.md` 或 ZIP。本仓库依赖六份引用规则，推荐使用 ZIP 导入。

## 上传本地 ZIP

1. 从 Gitee 克隆仓库：

   ```bash
   git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
   ```

2. 进入 `skills/kaoyan-english-grader/`，确认包含 `SKILL.md` 和 `references/`。
3. 将该目录内容打包为 ZIP，使 ZIP 根部直接包含主文件和引用目录。
4. 打开 QwenWork，点击左侧 **扩展 → 技能**。
5. 点击 **添加 → 上传技能**，选择 ZIP。
6. 等待解析完成，在“已安装”区域检查状态。

单文件上传适合没有外部引用的 Skill。本仓库应使用完整 ZIP。

## 在对话中搜索安装

可在对话框输入：

```text
请查找并安装考研英语 AI 批改 Skill。
如果技能库中没有对应技能，请明确告诉我，不要创建一个缺少评分规则的版本。
```

确认搜索结果名称、来源和能力说明，再按页面提示安装。

## 从仓库地址获取

官方文档说明可以向 QwenWork 提供开源仓库地址并要求下载到本地技能目录。Gitee 可访问性取决于当前运行环境。

```text
请从这个仓库获取考研英语批改 Skill：
https://gitee.com/ianwusb/kaoyan-english-grader.git

只安装 skills/kaoyan-english-grader 这一个技能。
保留 SKILL.md 和 references/ 下全部题型规则。
完成后报告安装路径，并检查六份规则文件。
```

下载失败时改用 ZIP 上传。

## 使用与验证

直接提出“批改我的考研英语一翻译”，或在输入框输入 `/` 并选择技能。到 **扩展 → 技能 → 已安装** 检查状态。

分别测试英语一翻译和英语二大作文，确认对应规则可读取。

## 更新与卸载

在技能管理区域按当前版本提供的流程更新或卸载。本地 ZIP 导入时，重新打包最新目录并上传。移除前核对技能名称。

## 官方资料

- [QwenWork：技能帮助文档](https://qwenwork.cn/docs/features/skills)
- [阿里云帮助中心：QwenWork Skills](https://www.alibabacloud.com/help/zh/qwenwork/skills)
