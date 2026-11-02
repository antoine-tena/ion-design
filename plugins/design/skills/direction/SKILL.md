---
name: direction
description: Find a site's visual direction - two or three directions shown as real mini-pages, the client picks one, it becomes the site's tokens (colours, fonts, spacing, motion level). Second step of the method (brief, direction, build, polish). Use before building the pages of a new site, or when its look is to be redone.
disable-model-invocation: true
argument-hint: "[reference sites beyond the brief]"
---

Skeleton: the steps hold, each one still to be sharpened on the first sites.

Input: the brief `design/brief.md` (`/design:brief`), and through it the client's file it
names; `$ARGUMENTS` adds reference sites. Without a brief, run `/design:brief` first rather
than guessing; an open question it marks as changing the direction waits for its answer.

1. **Look at the references** the brief lists: capture each one (phone and computer, as
   `/design:polish` does) and note what works in each: photos, typography, space, colours,
   motion. When the project's organisation keeps a library of references by sector, read the
   sector's too.
2. **Write two or three directions**, each a plan before any code: 4 to 6 named colours, the
   fonts and their role, a sketch of the layout, the principles, the brief's motion level
   (`${CLAUDE_PLUGIN_ROOT}/references/motion-levels.md`), within what it marks as fixed. Reread
   each against the brief and `${CLAUDE_PLUGIN_ROOT}/references/generic-signs.md`: remove what
   would be the default choice. The directions differ in kind, not in shade; boldness in one
   place per direction, where the brief's "To remember" points.
3. **Show them as real mini-pages**: the same content (the home page's top, one section) built
   in each direction, captured on a phone and a computer, side by side.
4. **The client chooses**: never pick for them; a mix of two is a new direction to show again.
5. **Turn the chosen one into tokens**: colours, fonts, spacing scale and motion level in the
   project's tokens file, the single source the sections and pages read. Commit on the work
   branch; the build step starts from there.
