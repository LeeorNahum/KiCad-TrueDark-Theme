# Agent Guidance

This repo builds TrueDark, a color theme for the newest KiCad release, keeping KiCad's default color direction while translating it into a balanced dark theme.

## Working Principles

- Keep this repo minimal. It is a theme repo, not a planning repo.
- Do not add placeholder folders, `.gitkeep` files, long research notes, or process docs.
- Keep durable guidance in this file, user-facing instructions in `README.md`, and concise project intent in `PROJECT.md`.
- Delete `TASKS.md` before publishing if it ever gets reintroduced during active work.
- Preserve KiCad's default color meaning unless a dark-mode adjustment is needed for contrast or readability.
- Treat `colors/truedark.json` as the source artifact. Do not add generators unless they are clearly needed and reproducible.
- Keep the releaseable theme under `colors/` and generated zip files under ignored `dist/`.
- Do not commit local KiCad configuration directories or machine-specific paths.
- Prefer the newest KiCad release unless the user explicitly changes compatibility goals.

## Theme Rules

- Neutral colors should start from an HSL lightness inversion, then be adjusted only when usability requires it.
- Saturated colors should keep their hue direction and role, with dark-theme lightness and chroma tuned by judgment.
- Accessibility and visual familiarity matter more than mathematically perfect inversion.
- If a color change changes the user's expected KiCad meaning, document why.
