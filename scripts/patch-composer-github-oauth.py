#!/usr/bin/env python3
"""Patch pre-2.10 composer/composer to accept modern GitHub installation tokens.

GitHub Actions issues ghs_ tokens with JWT-style segments (dots + base64url
hyphens). Older composer/composer rejects those in BaseIO::loadConfiguration.
Composer 2.10+ removed that validation (composer/composer#12856). This script
applies the same change to a vendored copy so older Shopware pins keep working.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

VALIDATION_MARKER = "Your github oauth token for"
DEFAULT_BASE_IO = Path("vendor/composer/composer/src/Composer/IO/BaseIO.php")

# Remove the github-oauth character validation block (comment + if + throw).
VALIDATION_BLOCK = re.compile(
    r"\n"
    r"[ \t]*// allowed chars for GH tokens[^\n]*\n"
    r"(?:[ \t]*//[^\n]*\n)*"
    r"[ \t]*if \(!Preg::isMatch\([^;]+?\)\) \{\n"
    r"[ \t]*throw new \\UnexpectedValueException\([^;]+?\);\n"
    r"[ \t]*\}\n"
)


def patch_file(path: Path) -> str:
    if not path.is_file():
        return f"composer/composer BaseIO.php not found at {path}, skipping patch"

    source = path.read_text(encoding="utf-8")
    if VALIDATION_MARKER not in source:
        return "composer/composer already accepts modern GitHub tokens, skipping patch"

    patched, count = VALIDATION_BLOCK.subn("\n", source, count=1)
    if count != 1:
        raise SystemExit(
            f"Failed to locate github oauth token validation block in {path}"
        )

    path.write_text(patched, encoding="utf-8")

    if VALIDATION_MARKER in path.read_text(encoding="utf-8"):
        raise SystemExit(
            f"composer BaseIO.php still contains github oauth token validation after patch: {path}"
        )

    result = subprocess.run(
        ["php", "-l", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(
            f"php -l failed for {path}:\n{result.stdout}{result.stderr}"
        )

    return f"Patched {path}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "base_io",
        nargs="?",
        type=Path,
        default=DEFAULT_BASE_IO,
        help=f"Path to BaseIO.php (default: {DEFAULT_BASE_IO})",
    )
    args = parser.parse_args(argv)

    print(
        "Patching composer github-oauth token validation "
        "(composer/composer#12856)"
    )
    print(patch_file(args.base_io))
    return 0


if __name__ == "__main__":
    sys.exit(main())
