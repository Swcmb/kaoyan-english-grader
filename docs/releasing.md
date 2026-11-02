<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../LICENSE.
-->

# GitHub Releases 发布

仓库通过 GitHub Actions 将经过检查的 Git 标签发布为 GitHub Release。附件包括完整源码归档和 SHA-256 校验文件；两个 Skill 均包含在源码归档中。

## 触发条件

推送符合以下格式的标签时触发：

```text
vMAJOR.MINOR.PATCH
vMAJOR.MINOR.PATCH-prerelease
```

例如：

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

工作流见 [publish.yml](../.github/workflows/publish.yml)。

## Release 资产

| 文件 | 内容 |
| --- | --- |
| `kaoyan-english-grader-vX.Y.Z.zip` | 标签对应的完整仓库 ZIP |
| `kaoyan-english-grader-vX.Y.Z.tar.gz` | 标签对应的完整仓库 TAR.GZ |
| `SHA256SUMS` | 两个源码归档的 SHA-256 校验值 |

Release Notes 由 GitHub 根据标签和上一个版本生成。发布入口：[GitHub Releases](https://github.com/Swcmb/kaoyan-english-grader/releases)。

## 从源码包安装 Skill

- **标准版（推荐）：** `skills/kaoyan-english-grader/`。安装整个目录，确保 `SKILL.md` 与 `references/` 六份评分规则保持原有相对位置。
- **完整版（单文件）：** `skills/kaoyan-english-grader-full/SKILL.md`。该文件内嵌六类完整评分规则，适用于只接受单个 Skill 文件的平台。

支持标准目录或完整目录 ZIP 的平台应优先安装标准版。完整版是兼容替代，不建议取代标准安装。

## 发布前检查

- [ ] README、安装文档和版本说明描述当前实际能力。
- [ ] 标准版主文件和六份规则已检查，目录结构完整。
- [ ] 完整版六类规则均已内嵌，且不依赖外部引用文件。
- [ ] 两个 Skill 的名称和目录互不冲突。
- [ ] 插件清单版本号与发布版本一致。
- [ ] 根目录 `LICENSE`、文件级版权和第三方通知完整。
- [ ] 标签指向经过审查的提交。
- [ ] 文档链接、安装步骤和示例与该版本一致。
- [ ] GitHub 页面渲染正常，归档可下载。

## 版本管理与故障排查

修订已发布内容时使用新版本标签，不覆盖已发布版本。创建失败时检查 Actions Release job、`contents: write` 权限、标签格式和资产上传日志。

发布后下载 ZIP 与 TAR.GZ，检查两个 Skill 的目录结构、主文件和评分规则，再校验 `SHA256SUMS`。归档校验通过不代表 Skill 已在任何平台完成安装测试。
