---
name: run
description: Run the `glaze` command for the user (Le design de la famille Keramos : identité visuelle, mise en page, typographie, mouvement, finitions). Use when the user asks for what glaze does, or names it.
argument-hint: "[arguments of glaze]"
---

<!-- First skill of the plugin, the counterpart of the example command: replace it with the
tool's real skills, one folder per verb (`skills/<verb>/SKILL.md`, `name` = the folder). -->

1. Find the command: `glaze` when it is installed on the machine (`uv tool install
   --editable backend` in its repo), otherwise `uv run --project <its repo>/backend glaze`.
2. Run `glaze $ARGUMENTS`; when the arguments are unclear, read `glaze --help` first
   rather than guessing an option.
3. Report what the command printed, and its exit code when it is not 0, without hiding an error.
