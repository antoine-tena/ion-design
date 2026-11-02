---
name: polish
description: Visual audit of a page of a site with screenshots (phones and desktop), a list of finish defects ranked like an art director would, then fixes, until the page holds up. Any frontend (Astro, Nuxt, plain HTML…). To make a page worthy of a high-end site.
disable-model-invocation: true
argument-hint: "<page path, e.g. /events>"
---

Page: `$ARGUMENTS`. The project's visual direction is the reference: its direction or
`design-system` skill if it has one, its tokens (colours, fonts, spacing), its frontend rules
(`.claude/rules/`, the frontend's `CLAUDE.md`). Last step of the method (brief, direction, build,
polish).
Project skills: !`ls .claude/skills 2>/dev/null | tr '\n' ' '`

1. **Prepare**: work on a dedicated `style/…` branch, in its worktree (`/repo:worktree` when
   the project has it). Start the frontend with the project's dev skill (`dev`) if nothing
   listens on its port.
2. **Capture**, screenshots in the scratchpad: the page on phones (375 px at least) and on a
   computer (1440 px), at the top then scrolling, plus the reachable states (button hover, open
   menu, empty form, validation error, loading if it can be triggered). Use what the project's
   stack provides, in this order: its preview skill (`/nuxt:preview` on Nuxt: three phones and
   a computer); a Playwright MCP server if one is enabled; otherwise the project's Playwright
   (`npx playwright screenshot --viewport-size=375,812 <url> <file>.png`).
3. **Critique like an art director**: a table of defects, from most to least visible, in these
   families: hierarchy and typography, alignment and spacing, colours and contrast, consistency
   with the rest of the site, images, missing states (empty, loading, error), motion and
   micro-interactions, mobile, accessibility. Check the page against
   `${CLAUDE_PLUGIN_ROOT}/references/generic-signs.md`. For each defect: what is wrong, why it
   looks "cheap", the fix.
4. **Suggest** 1 to 3 "wow effect" ideas suited to the page (reveal on scroll, animated
   figures, light parallax, video header…), within the site's motion level
   (`${CLAUDE_PLUGIN_ROOT}/references/motion-levels.md`) and its weight budget. Boldness in one
   place only.
5. **Fix** directly, in the project's own idiom: its tokens rather than a new literal colour,
   font or spacing; its styling (utility classes, component styles or CSS) as its frontend rules
   say; its existing UI components rather than new ones.
6. **Recapture** the same views and show before/after; start again at 3 while a visible defect
   remains. Commit on the work branch.
