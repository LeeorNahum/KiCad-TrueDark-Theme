<!-- BEGIN claude-code-compat (generated, do not edit) -->

@AGENTS.md

# Nested AGENTS.md

Before you create, edit, or run files in a directory, read that directory's `AGENTS.md` first when one exists. Only the root `AGENTS.md` is imported above. Nested `AGENTS.md` files hold local rules for their own subtree and are not auto-loaded. The closest `AGENTS.md` at or above a file governs work on that file, so check for one whenever you enter a new part of the tree (a package, an app, or a skill directory).

# Agent Skills Index

These project skills are not Claude Code slash-command skills. When a listed skill is relevant, read its `SKILL.md` path directly instead of trying a Skill tool or slash command.

Each description is the trigger. Respect it, and when it matches the task, read the skill's `SKILL.md` plus any relevant references, assets, scripts, or nearby root files the skill points to.

## [ask-questions](.agents/skills/ask-questions/SKILL.md)

> Use whenever requirements are unclear, multiple paths remain, confidence is low, a real blocker appears, or the user implicitly or explicitly wants questions back, and load it in that turn when the user mentions this skill, asks you to ask questions, or asks for a more interactive back-and-forth. Asks the user more useful questions when clarification, confirmation, unblocking, or sharper direction would help.

## [project-structure](.agents/skills/project-structure/SKILL.md)

> Choose and normalize opinionated project, workspace, and repo structure. Always use when setting up, scaffolding, reorganizing, splitting, auditing, naming, git-initializing, or publishing a project; deciding whether a folder is a local workspace container, planning repo, full project root, web/app repo, firmware/library repo, or canonical publishable repo; installing local skills; or creating root docs and gitignore boundaries.

## [release-versioning](.agents/skills/release-versioning/SKILL.md)

> Use when deciding or making a version bump, including a skill's metadata.version, preparing or publishing a GitHub release, publishing binaries or archives, attaching release assets, syncing README badges and version mentions, updating package or app metadata, or making sure version constants and docs agree before a release. Manages versioned releases and release artifacts across software, apps, firmware, skills, packages, and downloadable builds.

<!-- END claude-code-compat -->
