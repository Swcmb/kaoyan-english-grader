<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# GitHub Releases 发布

本仓库使用 GitHub Actions 将经过检查的 Git 标签发布为 GitHub Release。发布产物为完整仓库源码归档和校验文件。

## 发布触发条件

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

工作流：[publish.yml](../.github/workflows/publish.yml)

## Release 资产

工作流会创建同名 Release，并附加：

| 文件 | 内容 |
| --- | --- |
| `kaoyan-english-grader-vX.Y.Z.zip` | 标签对应的完整仓库 ZIP |
| `kaoyan-english-grader-vX.Y.Z.tar.gz` | 标签对应的完整仓库 TAR.GZ |
| `SHA256SUMS` | 两个归档文件的 SHA-256 校验值 |

Release Notes 由 GitHub 根据标签和上一个版本自动生成。

发布入口：[GitHub Releases](https://github.com/Swcmb/kaoyan-english-grader/releases)。

## 发布前检查

- README、Skill 主文件和六份评分规则已更新。
- 插件清单中的版本号与本次发布版本一致。
- `LICENSE`、第三方版权声明和必要通知完整。
- 标签指向经过检查的提交。
- README、安装指南和引用链接与本次版本一致。

## 版本管理与故障排查

Release 归档从标签指向的提交构建。修订优先使用新版本标签，不要覆盖已发布版本。

若 Release 创建失败，检查 Actions 的 Release job、`contents: write` 权限、标签格式和资产上传日志。确认标签指向的提交存在，且归档文件能够从该提交生成。

发布完成后下载 ZIP 和 TAR.GZ，检查目录结构及 `skills/kaoyan-english-grader/` 下的主文件与六份规则，再核对 `SHA256SUMS`。
