# Independent artwork review — V1 Rent opening test

A separate vision-capable reviewer inspected the PNGs, the room composites at 1080p, the SH004 frame, Visual DNA and storyboard. SHA-256 was recomputed. PASS means suitable for the opening test, not production registration or a full-video approval.

| Asset | SHA-256 | Verdict | Evidence and limitation |
|---|---|---|---|
| CH-MASTER | 12852084f48ab6992d0d769d2d19b426cb16f207f883dbae3db5edbe1487ee05 | PASS | Original curly-haired identity, recognizable clothing, readable hands; subtle shading and greater detail than reference. Front view only. |
| CH-P1 neutral | 12852084f48ab6992d0d769d2d19b426cb16f207f883dbae3db5edbe1487ee05 | PASS | Same image as master, readable at tested scale; closed mouth only. |
| CH-P3 bill | 43e29cf9d47d8581926ac9f84ead26911d14ca9a3032f908069ec5bfe6ddafba | PASS | Identity, clothing and stance align with master; both hands touch blank paper. Bill cannot move separately. |
| BG-ROOM | b5094b609ac112e4f8ec1510c98c545a09214569ed3c1900875f28f16dec4132 | PASS | Warm room, usable negative space; softly shaded rather than reference's flatter field. |
| BG-TABLE | c660ea667bab704f42b915cb35cd112708d58da4f2008b383de18aaea9cc7960 | PASS | Plausible perspective and scale in inspected composite; independently movable. |

At the tested composite scale no obvious halo or clipping was observed. The existing hard-cut preview does not validate movement, lip sync or actual renderer integration. Current storyboard requires the renter holding a bill, but does not specify animated content, independent bill motion, replacement, or a highlight behind fingers. The complete sprite is sufficient for the opening test if the paper remains blank. If content must go behind fingers or the document must move, separate bill and foreground hands are needed.

Production registration: none. Reference comparisons: character_consistency.jpg and source SH004_f309.png. Master and neutral candidates are byte-identical.
