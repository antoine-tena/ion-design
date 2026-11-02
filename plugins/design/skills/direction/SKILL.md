---
name: direction
description: Find a site's visual direction - two or three directions shown as real mini-pages, the client picks one, it becomes the site's tokens (colours, fonts, spacing, motion level). Second step of the method (brief, direction, build, polish). Use before building the pages of a new site, or when its look is to be redone.
disable-model-invocation: true
argument-hint: "[reference sites, or where the brief is]"
---

Skeleton: the steps hold, each one still to be sharpened on the first sites.

Input: the brief (what the business is, its tone, its audience, its words) and the reference
sites the client likes (`$ARGUMENTS`, or the client's file in the project). Without a brief,
ask for it rather than guessing.

1. **Look at the references**: capture each reference site (phone and computer, as
   `/design:polish` does) and note what works in each: photos, typography, space, colours,
   motion. When the project's organisation keeps a library of references by sector, read the
   sector's too.
2. **Write two or three directions**, each a plan before any code: 4 to 6 named colours, the
   fonts and their role, a sketch of the layout, the principles, the motion level
   (`${CLAUDE_PLUGIN_ROOT}/references/motion-levels.md`). Reread each against the brief and
   `${CLAUDE_PLUGIN_ROOT}/references/generic-signs.md`: remove what would be the default
   choice. The directions differ in kind, not in shade; boldness in one place per direction.
3. **Show them as real mini-pages**: the same content (the home page's top, one section) built
   in each direction, captured on a phone and a computer, side by side.
4. **The client chooses**: never pick for them; a mix of two is a new direction to show again.
5. **Turn the chosen one into tokens**: colours, fonts, spacing scale and motion level in the
   project's tokens file, the single source the sections and pages read. Commit on the work
   branch; the build step starts from there.
