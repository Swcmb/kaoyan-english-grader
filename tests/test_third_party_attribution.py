# Copyright (C) 2026 kaoyan-english-grader contributors
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import hashlib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTED_FILES = (
    Path("skills/check-the-licence-before-you-copy/SKILL.md"),
)
UPSTREAM_APACHE_LICENSE_GIT_BLOB_SHA = "d645695673349e3947e8e5ae42332d0ac3164cd7"
UPSTREAM_URL = "https://github.com/everywan-dev/claude-code-engineering"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    payload = f"blob {len(data)}\0".encode("ascii") + data
    return hashlib.sha1(payload).hexdigest()


class ThirdPartyAttributionTests(unittest.TestCase):
    def test_upstream_apache_license_is_preserved_verbatim(self) -> None:
        license_path = ROOT / "LICENSES" / "Apache-2.0.txt"
        self.assertTrue(license_path.is_file(), "Missing upstream Apache-2.0 license text")
        self.assertEqual(
            git_blob_sha(license_path),
            UPSTREAM_APACHE_LICENSE_GIT_BLOB_SHA,
            "Apache-2.0 license text changed; restore the verbatim upstream copy",
        )

    def test_notice_records_upstream_origin_and_rightsholder(self) -> None:
        notice_path = ROOT / "NOTICE"
        self.assertTrue(notice_path.is_file(), "Missing NOTICE file")
        notice = notice_path.read_text(encoding="utf-8")
        for required in (
            "THIRD-PARTY MATERIALS",
            "skills/check-the-licence-before-you-copy/SKILL.md",
            "Copyright 2026 everyWAN",
            UPSTREAM_URL,
            "Apache License, Version 2.0",
            "LICENSES/Apache-2.0.txt",
            "Translated the skill from English into Chinese",
            "Updated: 2026-11-02",
        ):
            with self.subTest(required=required):
                self.assertIn(required, notice)

    def test_every_adapted_file_keeps_file_level_attribution(self) -> None:
        notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
        for relative_path in ADAPTED_FILES:
            with self.subTest(path=str(relative_path)):
                path = ROOT / relative_path
                self.assertTrue(path.is_file(), f"Adapted file was moved or deleted: {relative_path}")
                content = path.read_text(encoding="utf-8")
                self.assertIn("Copyright 2026 everyWAN", content)
                self.assertIn(UPSTREAM_URL, content)
                self.assertIn("SPDX-License-Identifier: Apache-2.0", content)
                self.assertIn("修改说明：", content)
                self.assertIn("修改日期：2026-11-02", content)
                self.assertIn(str(relative_path), notice)

    def test_repository_license_is_gpl_3_or_later(self) -> None:
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        copying_text = (ROOT / "COPYING").read_text(encoding="utf-8")
        self.assertTrue(license_text.startswith("GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007"))
        self.assertIn("END OF TERMS AND CONDITIONS", license_text)
        self.assertEqual(copying_text, license_text)


if __name__ == "__main__":
    unittest.main()
