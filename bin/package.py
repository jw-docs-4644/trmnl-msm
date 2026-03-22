#!/usr/bin/env python3
"""Package the TRMNL plugin files into a ZIP for import."""

import zipfile
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT = PROJECT_DIR / "tmp" / "trmnl-msm.zip"

FILES = [
    PROJECT_DIR / "settings.yml",
    PROJECT_DIR / "views" / "full.liquid",
    PROJECT_DIR / "views" / "half_horizontal.liquid",
    PROJECT_DIR / "views" / "half_vertical.liquid",
    PROJECT_DIR / "views" / "quadrant.liquid",
]


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in FILES:
            zf.write(f, f.name)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
