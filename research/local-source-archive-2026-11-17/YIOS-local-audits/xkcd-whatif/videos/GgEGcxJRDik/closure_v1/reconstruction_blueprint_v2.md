# Reconstruction blueprint v2 — GgEGcxJRDik (closure v1; rv1 blueprint unchanged)
Use A = internal evidence-matched test only (source art, script, voice, names and branding are not reusable). Use B = ORIGINAL transfer: new subject and drawings, PROMPT_PACK_v2 locks and original branding; never the source logo, title lockup, creator name or recurring characters.
Global: 1080x1920, 24 fps CFR, 2000 f. Persistent rotated-Earth equirectangular MAP_FILL map (green/khaki/pale-blue/grey/teal) explored by camera moves; magenta city dots with hand-lettered names; red ovals for emphasis; white circular vignettes for landmark jokes; typeset question card + lecture board at the start.

| State | Frames | Enter (event @frame, length) | Image prompt (rv1 description verified on native/half-scale view; corrections applied) |
|---|---|---|---|
| VS001 | 0–42 | first frame | White canvas; grey rounded box upper with small serif text "What would the world's largest cities be like if the land masses were rotated by 90 degrees?"; black-ink blackboard frame middle with one grey globe on a stand at left of board; stick figure lower-left holding a sheet of paper, hand on hip. |
| VS002 | 44–105 | POP_ON_OBJECT @f43, 1 f | Same as G0001 plus right-pointing arrow and a second globe (landmasses turned) on the blackboard; question box and stick figure unchanged. |
| VS003 | 119–133 | SCENE_SWAP_ZOOM_IN @f106, 13 f | Map close-up: ASIA and EUROPE upper in hand-lettered caps, NORTH AMERICA centre-left; light-blue ice with black mountain marks along lower coast; grey ocean strip at bottom, white below. No city labels. |
| VS004 | 135–175 | POP_ON_LABEL @f134, 1 f | Map with "MEXICO CITY" label and magenta dot lower-left, NORTH AMERICA, ASIA, EUROPE labels; white strip at bottom. |
| VS005 | 177–211 | POP_ON_OBJECT @f176, 1 f | Map with Mexico City label and circular vignette of a building drawn in black ink inside a white circle, left-centre. |
| VS006 | 228–333 | PAN_RIGHT_TO_LEFT_FAST @f212, 16 f | Map centred on "JAKARTA" (dot, upper-left) with "AUSTRALIA" green/beige landmass left; ice and grey ocean upper; white strip at top. |
| VS007 | 349–431 | PAN_WITH_WRITE_ON_LABEL @f334, 15 f | Map of northern Asia with labels KOLKATA and DELHI (magenta dots), ASIA, EUROPE, AFRI(CA) cropped right; ice light-blue; white strip at top. |
| VS008 | 442–449 | ZOOM_OUT @f432, 10 f | Wide map: KOLKATA, DELHI, HONG KONG labels with magenta dots; ASIA, EUROPE, NORTH AMERICA, cropped AF at right; ice along north. |
| VS009 | 457–460 | WRITE_ON_LABEL @f450, 7 f | Wide map with labels MANILA, HONG KONG, KOLKATA, DELHI; no other new elements. |
| VS010 | 469–472 | WRITE_ON_LABEL @f461, 8 f | Wide map with MANILA, HONG KONG, KOLKATA, DELHI, KARACHI labels with magenta dots. |
| VS011 | 480–612 | WRITE_ON_LABEL @f473, 7 f | Wide map with labels MANILA, HONG KONG, KOLKATA, DELHI, MUMBAI, KARACHI; ASIA EUROPE NORTH AMERICA; ice north. |
| VS012 | 628–695 | ZOOM_OUT_WITH_POP_ON_LABELS @f613, 15 f | Whole-world map band, all city labels with magenta dots: KOLKATA MUMBAI KARACHI DELHI HONG KONG SHANGHAI SEOUL OSAKA TOKYO BEIJING MOSCOW CAIRO LONDON LOS ANGELES NEW YORK CITY MEXICO CITY; no marks. |
| VS013 | 697–704 | ANNOTATION_CIRCLE @f696, 1 f | Map with red oval around SEOUL only. |
| VS014 | 706–715 | ANNOTATION_CIRCLE @f705, 1 f | Red ovals around SEOUL and OSAKA. |
| VS015 | 717–725 | ANNOTATION_CIRCLE @f716, 1 f | Red ovals around SEOUL OSAKA TOKYO. |
| VS016 | 727–736 | ANNOTATION_CIRCLE @f726, 1 f | Red ovals around SEOUL OSAKA TOKYO SHANGHAI. |
| VS017 | 738–849 | ANNOTATION_CIRCLE @f737, 1 f | Map with five red ovals: SEOUL OSAKA TOKYO SHANGHAI NEW YORK CITY. |
| VS018 | 862–1005 | ZOOM_IN_WITH_POP_OFF_MARKS @f850, 12 f | Zoomed map, Asia upper and North America lower; city labels without red ovals. |
| VS019 | 1018–1042 | PAN_RIGHT_FAST @f1006, 12 f | Map centred on Africa and Middle East: labels DELHI MUMBAI KARACHI MOSCOW CAIRO NILE LONDON NEW YORK CITY SAO PAULO; green land south of Cairo. |
| VS020 | 1044–1148 | POP_ON_OBJECT @f1043, 1 f | Map with circular vignette of a shoreline scene (palms, sun, water) left of Cairo; labels as G0037. |
| VS021 | 1161–1317 | PAN_DOWN_LEFT_FAST @f1149, 12 f | Map close on SAO PAULO and BUENOS AIRES labels with magenta dots; South America; Africa upper-left; grey ocean bottom, white below; no vignette. |
| VS022 | 1330–1430 | PAN_UP_LEFT_FAST @f1318, 12 f | Map with Asia upper, North America lower: labels HONG KONG SHANGHAI SEOUL OSAKA TOKYO BEIJING MOSCOW LONDON LOS ANGELES NEW YORK C MEXICO CITY; white strip at bottom. |
| VS023 | 1432–1566 | POP_ON_OBJECT @f1431, 1 f | Same map with small white clouds above LOS ANGELES (a few cloud shapes). |
| VS024 | 1579–1736 | PAN_UP_RIGHT_FAST @f1567, 12 f | Map with labels KOLKATA DELHI MUMBAI KARACHI MOSCOW CAIRO LONDON NEW YORK CITY BEIJING; no vignette. |
| VS025 | 1749–1917 | ZOOM_IN @f1737, 12 f | Zoomed map: DELHI MUMBAI KARACHI MOSCOW CAIRO LONDON NEW YORK CITY large hand-lettered labels with magenta dots; no vignette. |
| VS026 | 1919–1999 | POP_ON_OBJECT @f1918, 1 f | Same map with circular vignette of two small characters at a table between MOSCOW and LONDON; held to end. |

Motion: 1-frame pops for labels, ovals and vignettes; city names typed letter by letter; 11 whole-frame camera zooms/pans of 10–15 f with bell-shaped (ease-in-out) change curves and motion blur on fast pans.
Continuity: one map drawing for the whole video; labels persist once added; camera framing is the only thing that changes between map states besides overlays.
QA: (1) use A frame compare per state at native res; (2) every onset within ±1 frame of the ledger; (3) pops change on exactly 1 frame, multi-frame events match the measured curve (activity_curves.csv); (4) holds still (<0.1% changed px excluding grain); (5) all text exactly as transcribed in CLOSURE.md and legible at 320 px width; (6) use B originality check.
Not done: per-video render test (not required by contract v1).
