<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../LICENSE.
-->

# 第三方内容与许可证审查规范

本规范适用于复制、改编、翻译、重命名、vendor、再分发或发布第三方代码、Skill、Prompt、配置、模板、文档、图片、字体、数据和二进制材料。

**许可证判断必须落实到具体文件或明确路径范围。仓库整体声明不能替代文件级来源证据。**

## 适用范围

| 操作 | 是否需要审查 |
| --- | --- |
| 复制第三方文件、代码片段、Skill、Prompt、配置或模板 | 是 |
| 将依赖源码 vendor 到仓库 | 是 |
| 翻译、改写或重命名第三方材料 | 是 |
| 发布包含第三方材料的产物 | 是 |
| 独立实现相同功能 | 无需第三方许可判定；仍需确定新文件许可标识 |

公开可访问不等于允许复制、修改或再分发。改写和翻译第三方材料仍需审查。

## 1. 明确判定单位

| 类别 | 示例 | 检查重点 |
| --- | --- | --- |
| 源码 | `.c`、`.h`、`.py`、`.rs`、Makefile | 文件头、源码许可、版权声明 |
| 文档与文字 | README、`docs/**`、注释、模板 | 文档许可、署名和改编条件 |
| 数据与配置 | TOML、YAML、Schema、样例数据 | 来源、授权范围和第三方内容 |
| 第三方产物 | vendor 依赖、字体、图片、二进制 | 独立许可证、NOTICE 和再分发条件 |

目标范围使用具体路径或 glob，例如 `src/**/*.c`、`skills/vendor-skill/**`，不要用未经证实的“整个项目”作为判定单位。

## 2. 按证据强度核查

依次检查文件级 `SPDX-License-Identifier` 与版权声明、明确覆盖目标路径的 `LICENSE` / `COPYING`、文件内来源标记与许可文本，以及上游 README、贡献指南或发布说明中的明确声明。

证据冲突时保留冲突信息并暂停判定。SPDX 标识说明许可证类型，不单独证明版权归属，也不替代署名义务。

## 3. 避免错误推断

| 错误推断 | 正确处理 |
| --- | --- |
| 根目录许可证自动覆盖全部文件 | 核对许可范围和文件级标识 |
| README 声明证明所有文件使用同一许可证 | 继续检查来源和独立声明 |
| 子目录许可证覆盖其他目录 | 仅按明确范围解释 |
| 文件有 SPDX 就表示署名完成 | 检查版权人、来源、LICENSE 和 NOTICE |
| 仓库公开即允许复制 | 未声明许可按“未声明”处理 |

## 4. 每项结论记录证据

记录上游许可证 URL 或仓库路径、适用条款、原文件路径、版权/SPDX/来源证据、目标文件路径或 glob。

同时记录上游仓库、版本或提交 SHA、获取日期、修改方式、目标路径和需要保留的通知文件。缺少关键证据时标记为 **未声明 / 待确认**，暂停复制、改编和再分发。

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

本仓库原创内容采用 `GPL-3.0-or-later`，完整文本位于根目录 [LICENSE](../../LICENSE)。新增原创 Markdown 文件添加 `SPDX-License-Identifier: GPL-3.0-or-later` 文件级标识。

第三方文件保留上游 SPDX 标识、版权声明和许可证。仓库默认许可证不会覆盖独立授权的第三方文件。新增第三方材料后，检查许可证全文、适用 NOTICE、文件级来源和改编追溯关系。

更换项目许可证、删除上游通知或扩大现有许可证范围前，必须取得维护者明确授权。证据冲突或授权边界不清时暂停操作，并报告路径、证据和未解决问题。
