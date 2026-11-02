# Motion by level

A site's level of motion is chosen once, in its direction; each level adds to the one before.
JavaScript arrives only where an effect needs it, and the page's weight budget still holds.

| Level | Technique | Note |
| --- | --- | --- |
| 1, sober | CSS only: reveal on scroll (scroll-driven animations), transitions between pages (view transitions) | Chrome and Edge since 2023, Safari since September 2025; Firefox keeps them behind a setting and shows the page without motion: it must read fine that way. |
| 2, modern | Plus the Embla carousel (MIT, lighter than Swiper) and Motion (MIT) for a few effects | |
| 3, highly animated | Plus GSAP, and Lenis (MIT) for smooth scrolling | GSAP is free for client sites; its licence only forbids visual animation tools competing with Webflow. |

Every level honours `prefers-reduced-motion`: the content is there without the motion.
