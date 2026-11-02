---
name: brief
description: Write a site's design brief - audience, main action, character, what is fixed, photos, references, motion level 1 to 3, the one thing to remember - from the client's file without copying it, in design/brief.md. First step of the method (brief, direction, build, polish). Use before /design:direction on a new site, or when the client's file has changed what the site is for.
disable-model-invocation: true
argument-hint: "[path of the client's file]"
---

Input: the client's file (`$ARGUMENTS`, otherwise `dossier/dossier.toml` in the site, which
ion-deal copies there). Output: `design/brief.md` in the site, which `/design:direction` reads.
Its headings and what goes under them: `${CLAUDE_PLUGIN_ROOT}/references/brief-template.md`;
a filled one: `${CLAUDE_PLUGIN_ROOT}/references/brief-example.md` (an invented salon).

1. **Prepare**: work on a dedicated branch, in its worktree (`/repo:worktree` when the project
   has it). An existing `design/brief.md` is updated, never overwritten blind.
2. **Read the whole file**, then its folders: the long texts (`textes/`), the captures of the
   liked sites (`references/`), and the photos themselves (open a sample of each subject; count
   what holds at large size). Without a client's file, ask the user for the same answers rather
   than guessing; a file that ion-deal still finds incomplete (`ion deal check`) is completed
   first, in the file.
3. **Write each heading of the template** in the project's language. Facts already in the file
   are named by their field (`shop.tagline`), never copied. Each statement says its source: a
   field, a client answer with its date, or `hypothesis`. The character words come from the
   client's words, never from the sector's habits; read them against
   `${CLAUDE_PLUGIN_ROOT}/references/generic-signs.md`.
4. **Set the motion level**: the wished animation (`brand.animation_level`: « sobre » 1,
   « moderne » 2, « très animé » 3), never above the level sold (`contract.level`). A lower
   level the audience would argue for goes to the open questions, never decided for the client.
5. **List the open questions**, each with who answers it (`contract.approver`). Never contact
   the client: give the questions to the user, and write their answers back with their date.
   An answer that is a fact of the file (a page, an hour, a colour to avoid) goes into the
   file, and the brief names its field.
6. **Hand over**: commit `design/brief.md` on the work branch. `/design:direction` starts once
   no open question changes the direction.
