# KiCad TrueDark Theme

[![GitHub Release](https://img.shields.io/github/v/release/LeeorNahum/KiCad-TrueDark-Theme?sort=semver)](https://github.com/LeeorNahum/KiCad-TrueDark-Theme/releases/latest)

TrueDark is a color theme for the newest KiCad release that keeps KiCad's default color direction while translating it into a balanced dark theme.

The theme file is `colors/truedark.json`.

## Install

Copy `colors/truedark.json` into your KiCad `colors` directory, restart KiCad, then select `TrueDark` in preferences.

- Windows: `%APPDATA%\kicad\<version>\colors\`
- macOS: `~/Library/Preferences/kicad/<version>/colors/`
- Linux: `~/.config/kicad/<version>/colors/`

For the current KiCad 10 release on Windows, the target path is usually:

```powershell
%APPDATA%\kicad\10.0\colors\
```

## Release Package

Create the installable zip with:

```powershell
python scripts/package_release.py --version 1.0.0
```

The package contains only the KiCad add-on files:

- `colors/truedark.json`
- `metadata.json`
