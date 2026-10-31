---
name: run
description: Run the `ion-design` command for the user (Le design de la famille Ion : identité visuelle, mise en page, typographie, mouvement, finitions). Use when the user asks for what ion-design does, or names it.
argument-hint: "[arguments of ion-design]"
---

<!-- First skill of the plugin, the counterpart of the example command: replace it with the
tool's real skills, one folder per verb (`skills/<verb>/SKILL.md`, `name` = the folder). -->

1. Find the command: `ion-design` when it is installed on the machine (`uv tool install
   --editable backend` in its repo), otherwise `uv run --project <its repo>/backend ion-design`.
2. Run `ion-design $ARGUMENTS`; when the arguments are unclear, read `ion-design --help` first
   rather than guessing an option.
3. Report what the command printed, and its exit code when it is not 0, without hiding an error.
