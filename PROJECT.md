# KiCad TrueDark Theme

Minimal repo for one thing: `colors/truedark.json`, a balanced dark theme for the newest KiCad release that preserves KiCad's default color language.

## Deliverables

- `colors/truedark.json`: the theme to copy into KiCad's `colors` folder.
- `metadata.json`: KiCad package metadata for release/package compatibility.
- `scripts/package_release.py`: creates the release zip.

## Theme Rules

- Neutral backgrounds, grids, page limits, text, and worksheet colors should be dark-mode equivalents of KiCad defaults.
- Colorful layers and semantic highlights should keep the default hue direction and relative balance.
- Readability and familiar KiCad meaning beat mathematically perfect inversion.
- Do not turn this into a novelty/editor-inspired theme.
