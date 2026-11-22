# 22 LONG-FORM VISUAL DNA: CH001 (Casually Finance), landscape videos

Added 2026-11-21 on owner approval. **Scope: landscape long-form only (1920x1080, 1280x720).** Files 05/09/06/13/21 describe Shorts (1080x1920, mostly one deep video) and stay unchanged; this file does not overwrite them. Where a long-form value differs from a Shorts value, this file governs for long-form productions.

Source of every number: `productions/new-original-video-v1-rent-01/V1_RENT_STYLE_FIDELITY_AUDIT.md` and its `style_audit/` (scripts in `style_audit/tools/`, sheets in `style_audit/*.jpg`). Nothing was re-analysed for this file. Corpus: `/Users/ghilmankhan/workprojects/videos in mp3/CasuallyFinance` (34 landscape of 216 files).

Labels: **[M]** measured by script on pixels; **[V]** viewed on contact sheets/frames; **[I]** interpretation (not proven). No exact production-tool knowledge is claimed.

## 1. Evidence and limits
- [M] Background class on 2,544 long-form frames (34 videos, first 300 s, 1 frame/4 s): 82.9% light, 4.6% flat colour, 12.5% "full" (everything else, includes photos and dark screenshot plates). Shorts: 98.3 / 0.5 / 1.2.
- [V] Five long-forms inspected in detail: Every Type of Investor, Drowning in Debt, Crypto Is a Brilliant Scam, Something Feels Off About 2026, Brace For Impact.
- [M] Geometry from two host appearances (3 crops); head-region change over one 8 s window; frame-diff statistics over the first 75 s of 6 long-forms.
- Limits: the other 29 long-forms were only counted, not viewed. Host geometry rests on two appearances. No audience test.

## 2. Principles (each with its evidence class)

| # | Principle | Class | Evidence |
|---|---|---|---|
| L1 | **Default canvas is white or near white.** Environments are single beats, not backdrops. | [M] | 82.9% light long-form frames; per-video light share median about 0.9. |
| L2 | A detailed environment (street, club, party room, restaurant) appears as one beat; the host stays a thin stick figure inside it. | [V] | Off-2026 0:31, Crypto restaurant, Drowning club. |
| L3 | **The recurring host is one thin line-body rig with a large round head.** | [M]+[V] | head h / figure h = 0.38, 0.38, 0.31; body line about 1.6-2.5% of figure height; outline about 1.6% of figure height. |
| L4 | Expression is a **head swap on the same body** (smile, flat mouth, worried, sunglasses). | [V] | Same body in Brace 0:07 and 0:46, Investor 0:55. |
| L5 | **No lip sync.** Head region changed 11 times in 8 s, all instant swaps with static frames between. | [M] | Brace 0:06-0:14 head-region diff. |
| L6 | Richer characters (Uncle Sam, hooded figure, teacher) exist only as story roles, not as the narrator. | [V] | Drowning 0:02, Crypto 0:22/0:55. |
| L7 | **Rhythm is hard cuts and held frames.** 17-35 hard cuts per 75 s in five long-forms (one fast montage 133); exactly-still frames 84-96% in five of six sampled (38% in one). | [M] | `motion.py`. |
| L8 | Pop-ins are staggered small objects (e.g. `?` marks); no continuous idle motion on the host. Reference content is 24 fps stepped inside 30 fps files. | [V]+prior | `brace_mouth_strip.jpg`; 21 §E42. |
| L9 | **Financial graphics are simple and drawn**, or real screenshots; the key figure gets a **red hand-drawn arrow or circle**. Two-colour line charts with hand-lettered legend. | [V] | SHEET3 (Investor 1:04, Off-2026 0:16, Drowning 1:22). |
| L10 | **Type is hand-lettered or Comic-style**, large, high contrast, short. Screenshots carry their own source text. | [V] | SHEET4. |
| L11 | One focal subject per beat. | [V]+[M] | contact sheets + cut counts. |

## 3. Interpretations (not proven)
- I-L1 The thin rig is the channel's reusable design system across scene types (supported by L2-L4; two appearances measured).
- I-L2 Rolling counters and eased tweens are not part of the grammar (none seen in the sampled frames; not exhaustively tested).
- I-L3 The channel probably works in vector/raster drawing tools with stepped holds; not verified.

## 4. Reusable production rules for ORIGINAL work (identity-neutral)
These keep the principle, never the reference's artwork.
1. **Canvas:** `#FDFDFD`. A room/scene plate only for a beat that needs the place, 1-3 s, then back to white.
2. **Host rig:** thin line body (line width about 2.5% of figure height), head about 0.31-0.38 of figure height, separate head and body layers, 3 arm poses minimum, 5 head drawings minimum. The head, hair, clothing hint and palette are ORIGINAL; never trace or reuse the reference's face, hair or exact outfit.
3. **Expressions** are drawings swapped at hard cuts at meaningful words (a claim lands, a question, a reveal). No mouth animation.
4. **Beat length:** 2-4 s median; aim for 20-30 beats per 75 s as a guide, set by meaning and the narration's own breaks, not by the number.
5. **Motion:** hard cut between beats; objects pop in (about 3 frames at 24 fps) at the word they describe, staggered by about 0.4-0.7 s; **no idle bob**; hold everything else still; ease only a deliberate slide.
6. **Graphics:** drawn axes or flat drawn bars on white; the key number gets a red arrow or circle that draws on in steps; numbers pop in at the final value (a rolling counter shows wrong intermediate values, so do not use one).
7. **Type:** hand-lettered style for labels and callouts, large enough for a phone (labels at least 5% of frame height). Source tags use a plain face, at least 3.4% of frame height, with sufficient contrast, bottom-left.
8. **Accuracy:** a drawn chart still carries the exact verified number, source and date; "derived" values are labelled.

## 5. What this does not claim
Exact tools, exact timing curves, the channel's colour management, or that the same grammar holds across all 34 landscape videos.

## 6. Cross-reference
Shorts: 05, 06, 09, 13, 21. V1 application: `productions/new-original-video-v1-rent-01/V1_RENT_LONGFORM_STYLE_RULES.md` (written after the proof).
