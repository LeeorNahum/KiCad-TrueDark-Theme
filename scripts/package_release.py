#!/usr/bin/env python3
"""Create a KiCad-compatible TrueDark color theme package."""

from __future__ import annotations

import argparse
import hashlib
import zipfile
from pathlib import Path


PACKAGE_FILES = (
    Path("colors/truedark.json"),
    Path("metadata.json"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="1.0.0")
    parser.add_argument("--output-dir", default="dist")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"truedark-kicad-theme-v{args.version}.zip"

    for package_file in PACKAGE_FILES:
        if not package_file.exists():
            raise FileNotFoundError(package_file)

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for package_file in PACKAGE_FILES:
            archive.write(package_file, package_file.as_posix())

    print(f"Wrote {output_path}")
    print(f"Size: {output_path.stat().st_size} bytes")
    print(f"SHA256: {sha256(output_path)}")


if __name__ == "__main__":
    main()
