#!/usr/bin/env python3
"""Delete newly added files in the current project root.

This script only operates on files in the same directory as itself.
Directories are ignored.
"""

from __future__ import annotations

from pathlib import Path


# Files currently present in the repository root.
PRESERVED_FILES = {
    ".env",
    ".gitignore",
    ".python-version",
    "LICENSE",
    "README.md",
    "README_zh.md",
    "allocate_gpu.sh",
    "clean.py",
    "conf.yaml",
    "conf.yaml.example",
    "dataloader.py",
    "install.sh",
    "run_dataset.py",
    "pyproject.toml",
    "uv.lock",
}


def main() -> None:
    root = Path(__file__).resolve().parent
    removed = []

    for path in root.iterdir():
        if not path.is_file():
            continue
        if path.name in PRESERVED_FILES:
            continue
        path.unlink()
        removed.append(path.name)

    if removed:
        print("Removed files:")
        for name in sorted(removed):
            print(f"- {name}")
    else:
        print("No new root-level files to remove.")


if __name__ == "__main__":
    main()
