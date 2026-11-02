<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 第三方内容与许可证审查规范

本规范用于审查引入、改编、翻译、复制或再分发的第三方代码、Skill、Prompt、模板、文档、图片、字体、数据、模型和二进制文件。它是仓库发布前的工程检查流程，不构成法律意见。

## 目标与适用范围

审查单位应具体到文件、目录或明确的资产集合。公开可访问不等于允许复制、修改或再分发；翻译和改写也可能构成受许可约束的衍生内容。

| 场景 | 是否审查 |
| --- | --- |
| 从其他仓库复制或改写文件 | 是 |
| 引入第三方 Skill、Prompt、模板或文档 | 是 |
| 使用第三方图片、字体、数据集、模型或二进制 | 是 |
| 将第三方文件纳入源码归档或发布包 | 是 |
| 独立实现相同功能 | 无需对方许可证授权判断，仍需确认新文件的来源与许可 |

## 1. 明确判定单位

| 类别 | 示例 | 检查重点 |
| --- | --- | --- |
| 源码 | `.c`、`.h`、`.py`、`.rs`、Makefile | 文件头、源码许可证和版权声明 |
| 文档与文字 | README、`docs/**`、注释、模板 | 文档许可、署名和改编条件 |
| 数据与配置 | TOML、YAML、Schema、样例数据 | 来源、授权范围和第三方内容 |
| 第三方资产 | vendor 依赖、字体、图片、二进制 | 独立许可证、NOTICE 和再分发条件 |

目标范围使用具体路径或 glob，例如 `src/**/*.c`、`skills/vendor-skill/**`。不要使用未经证实的“整个项目”作为判定单位。

## 2. 按证据强度核查

依次检查：

1. 文件级 `SPDX-License-Identifier` 和版权声明。
2. 明确覆盖目标路径的 `LICENSE`、`COPYING` 或其他许可文件。
3. 文件中的来源标记、原作者声明和许可文本。
4. 上游 README、贡献指南、发布说明和权利人明确声明。

证据冲突时保留冲突信息并暂停判定。SPDX 标识说明许可证类型，但不单独证明版权归属，也不能替代署名义务。

## 3. 避免错误推断

| 错误推断 | 正确处理 |
| --- | --- |
| 根目录许可证自动覆盖全部文件 | 核对许可证的适用范围与文件级标识 |
| README 声明证明所有文件都使用同一许可证 | 继续检查文件来源和独立声明 |
| 子目录许可证覆盖其他目录 | 仅按文件和许可证明确声明的范围解释 |
| 文件有 SPDX 就表示署名已经完成 | 检查版权人、来源、LICENSE 和 NOTICE |
| 仓库公开即允许复制 | 未声明许可时按“未声明”处理 |

## 4. 记录每项结论的证据

至少记录上游仓库或资产地址、版本或提交 SHA、获取日期、源文件路径、许可证 URL 或原文、适用条款、目标路径、修改方式，以及必须保留的版权和通知文件。

缺少关键证据时标记为 **未声明 / 待确认**，暂停复制、改编和再分发。不要用项目整体的许可证替代文件级来源核查。

## 5. 常见许可证兼容性边界

| 许可证 | 处理原则 |
| --- | --- |
| MIT / BSD-2-Clause / BSD-3-Clause / ISC | 通常可与 GPL 系列组合；保留原始版权和许可通知，其他 BSD 变体单独核验 |
| Apache-2.0 | 与 GPL-3.0 兼容；与 GPL-2.0-only 不兼容；保留 Apache 许可证及适用 NOTICE |
| GPL-2.0-only | 不要与 GPL-3.0-only 代码合并为受单一 GPL 版本约束的作品 |
| GPL-2.0-or-later | 权利人允许后续版本时可选择 GPL-3.0；仍需核对原始声明 |
| 专有或未声明 | 未取得明确授权前停止复制和再分发 |

GNU 将 Apache-2.0 列为与 GPL-3.0 兼容；Apache Software Foundation 也说明 Apache-2.0 软件可纳入 GPL-3.0 项目。Apache-2.0 与 GPL-2.0 的不兼容不能泛化为与 GPL-3.0 不兼容。

不得编造 `Apache-2.0-exception` 等 SPDX 例外标识。`WITH` 只能引用 SPDX 例外清单中的真实标识。复杂链接关系、衍生作品边界、专利条件和多许可证组合应单独审查。

参考资料：

- [GNU：许可证兼容性与重新许可](https://www.gnu.org/licenses/license-compatibility.en.html)
- [Apache Software Foundation：Apache 2.0 与 GPL 兼容性](https://apache.org/licenses/GPL-compatibility.html)
- [GNU GPL FAQ：GPLv2 与 GPLv3 兼容性](https://www.gnu.org/licenses/gpl-faq.en.html#v2v3Compatibility)
- [SPDX：许可证例外清单](https://spdx.org/licenses/exceptions-index.html)

## 6. 本仓库许可政策

本仓库原创内容采用 `GPL-3.0-or-later`，完整文本位于根目录 [LICENSE](../../LICENSE)。新增原创 Markdown 文件应包含文件级 `SPDX-License-Identifier: GPL-3.0-or-later` 标识。

第三方文件保留上游 SPDX 标识、版权声明和许可证。仓库默认许可证不会覆盖独立授权的第三方文件。新增第三方材料后，检查许可证全文、适用 NOTICE、文件级来源和改编追溯关系。

更换项目许可证、删除上游通知或扩大现有许可证范围前，必须取得维护者明确授权。证据冲突或授权边界不清时暂停操作，并报告路径、证据和未解决问题。
