# Transfer test output: "Savings vs credit card / net interest margin" long-form excerpt

Inputs read: Index and Playbook only (no other KB files opened, no web, no render). Format: long-form 1920x1080, white `#FDFDFD` canvas (Playbook sec. 0, 7). Timing: 161 words counted by hand, 0.4 s/word (150 wpm), about 64.4 s. All times are APPROXIMATE; the playbook (step 5) says real ASR times from the final voice take replace them. No source figures are asserted here; every number is marked "verify from the page".

Beat ids = sentence ids (S001-S014), per playbook step 2.

---
## 1. Claim register (CLAIMS_AND_BEATS.csv shape: id, sentence, text, type, needs_evidence, status)

Column set is my guess (playbook only says "id, text, type, needs_evidence Y/N").

| id | sent | claim | type | evidence? | primary source to capture (publisher / page) | note |
|---|---|---|---|---|---|---|
| C-01 | S001 | A typical savings account pays less than a coffee costs per year | comparative figure, UNDEFINED (balance? which coffee?) | Y, blocking | FDIC "National Rates and Rate Caps" page (national savings average); a coffee price needs a source (BLS average price series is for retail grocery coffee, not a cafe cup, so it may not fit) | As worded it is not verifiable. Needs owner decision: reword, or define a balance (e.g. a stated example balance x national rate = $/yr vs a stated coffee price). Do not put on screen until resolved |
| C-02 | S002 | The same bank charges others over 20% on a credit card | number + causal implication ("same bank") | Y | Federal Reserve Board, G.19 Consumer Credit release, table "Interest rates and finance charges" (rate on credit card plans, commercial banks, accounts assessed interest vs all accounts); FRED series copy of the same | "Same bank" is an implication, not a measured fact: the G.19 figure is an industry average across banks. On-screen label must say "average, commercial banks" |
| C-03 | S003 | "Legal" (implicit: nothing illegal here) | legal framing | N for screen, owner check | none needed; avoid any legal claim on screen | Spoken rhetorical question. Do not show a "legal" stamp |
| C-04 | S005 | Bank pays little on deposits, lends at much higher rate, keeps the gap | mechanism, causal | Y (definition-level) | FDIC Quarterly Banking Profile (definition/glossary of net interest income and margin); Federal Reserve Bank explainer on bank net interest income | Mechanism is correct in outline; keep drawn, not screenshot, unless a clean definition page is found |
| C-05 | S006 | The gap is called the net interest margin | terminology | Y | FDIC Quarterly Banking Profile, glossary entry for net interest margin | Official NIM is (interest income - interest expense) / earning assets, a bank-wide ratio. The spoken line equates it with the credit-card-vs-savings gap. Flag to owner (see C-12) |
| C-06 | S007 | Early 1980s: rates so high that banks competed for deposits | date + causal/historical | Y | Federal Reserve History (federalreservehistory.org) page on the Monetary Control Act of 1980 / deregulation of deposit rates; FDIC "History of the Eighties" (Vol. 1) chapter on DIDMCA and Garn-St Germain; FRED prime rate / fed funds series for the high-rate years | Need the exact link between high rates and deposit competition (rate-ceiling phase-out). Verify wording before using "competed" |
| C-07 | S008a | Fed says average credit card rate is above 20% | number + named org + "X said" | Y | same G.19 table as C-02; read the actual latest row and its release date; if the value is not above 20% in the current vintage, the claim must change | "Federal Reserve says" => R-S evidence required. Possible mismatch: G.19 has two series (all accounts vs accounts assessed interest); they differ. State which one |
| C-08 | S008b | Many big-bank savings accounts pay well under 1% | number + vague quantifier | Y | FDIC National Rates and Rate Caps page (national average savings rate) and/or named big-bank published savings APY pages captured with date | "Big-bank" is not the FDIC "national" rate (which is all banks). Prefer 2-3 named big-bank rate pages with retrieval date; avoid naming if licensing/brand concerns, see KB GAPS |
| C-09 | S009-S010 | Worked example: $100 deposit, $90 lent at 20%, you get $0.50, bank keeps the difference | illustrative arithmetic | N (it is hypothetical), but must be labelled | none; internal calc: 90 x 20% = $18.00/yr; 100 x 0.5% = $0.50; gross gap before costs = $17.50 | "Keeps the difference" overstates profit: ignores defaults, reserves, costs, that a deposit funds many loan types, and that 20% is a card rate not the average loan rate. Label drawing "simplified example". Also $0.50 implies a 0.5% rate, not spoken: show it |
| C-10 | S012 | Online banks pay 4% | number, time-sensitive | Y | named online bank savings APY pages (capture date on screen); FDIC national rates page for contrast | Rate moves; tag "as of <retrieved date>" |
| C-11 | S013-S014 | People stay at big banks because switching feels like work ("banks know it") | behavioral, causal, intent claim | Y or soften | CFPB report or research on deposit account switching / consumer inertia; Federal Reserve or academic paper on deposit rate stickiness | "Banks know it" is an intent claim. If no source is found, hold as narrator opinion and do not dress it as a data graphic |
| C-12 | S005-S010 combined | The whole 20% vs 0.5% story = how banks profit | framing | owner flag | FDIC QBP: industry NIM is a few percent, not ~17 points | The excerpt's example implies a ~17.5 point spread; real reported margin is far smaller. Not a script error to fix silently, but I will not draw a chart implying the real margin is that wide. Flag to owner |

---
## 2. Storyboard (scene specs). Times approximate, 0.4 s/word.

Reasoning log (playbook sec. 3 ten questions) is compressed into `why` and `leaves_out`; a full 10-answer log for 14 beats would be a separate file, see KB GAPS.

Global: hard cuts only; one focal subject per scene; red = alarm/callout only, one accent per beat; source tag bottom-left on every evidence scene; host appears only where it adds meaning.

```yaml
- scene_id: S001
  audio: {start: 0.0, end: 5.2}
  narration: "Your savings account probably pays you less than a coffee costs per year."
  claim_ids: [C-01]
  purpose: COMPARISON   # savings payout vs a coffee, scaled
  concept: "a year of interest is tiny"
  visual_concept: "left: drawn savings jar with a few coins; right: one drawn takeaway coffee cup, equal footprint; no numbers until C-01 is resolved"
  composition: {canvas: white, focal: coffee cup right-center, secondary: jar left-center, host: none}
  background: "#FDFDFD"
  main_subject: "jar and cup, hand-drawn"
  character: none
  layers: [bg, jar, coins, cup]
  real_evidence: none (C-01 unresolved)
  on_screen_text: []
  hierarchy: [cup, jar]
  animation: [{t: 0.0, op: cut_in, layer: jar}, {t: 1.8, op: pop_in, layer: cup, dur: 0.2}]
  camera: static
  transition: {in: hard_cut, out: hard_cut}
  sound: voice only
  licensing: original drawing
  acceptance: ["jar and cup same visual weight", "no figure shown that is not in register"]
  why: "pairing two objects is the cheapest honest way to say 'less than'; hook has no source so it stays an object, not a stat"
  leaves_out: "dollar amounts, bank logo"

- scene_id: S002
  audio: {start: 5.2, end: 12.8}
  narration: "And yet the bank that holds it is charging someone else more than twenty percent on a credit card."
  claim_ids: [C-02]
  purpose: EVIDENCE
  concept: "card APR is 20%+"
  visual_concept: "cropped G.19 table row 'credit card plans, commercial banks' on white, ring on the rate cell; small drawn card + stranger silhouette in margin"
  composition: {focal: table crop center 60% width, secondary: drawn card bottom-right 12%}
  main_subject: "Federal Reserve G.19 crop (evidence/federal-reserve/g19_<date>.png, sha256 in manifest)"
  character: none
  layers: [bg, table_crop, ring_red, card_icon, source_tag]
  real_evidence: {file: evidence/federal-reserve/g19.png, url: federalreserve.gov G.19 release, retrieved: TBD, passage: "credit card rate row, latest value"}
  on_screen_text: ["average, commercial banks"]
  hierarchy: [ring_target, row_label, card_icon]
  animation: [{t: 0.0, op: cut_in, layer: table_crop}, {t: 4.6, op: draw_on, layer: ring_red, dur: 0.6, ease: linear steps}]
  camera: static
  transition: {in: hard_cut, out: hard_cut}
  sound: voice only
  licensing: "public Federal Reserve page; source tag; US federal publication"
  acceptance: ["ring lands within 0.3 s of the word 'twenty'", "crop keeps column header + date visible", "label says average, not 'this bank'"]
  why: "R-N + R-S: a named-org number needs the authentic table"
  leaves_out: "other rows, all other columns"

- scene_id: S003
  audio: {start: 12.8, end: 14.4}
  narration: "How is that legal?"
  claim_ids: [C-03]
  purpose: REACTION
  concept: "viewer's question"
  visual_concept: "host centered, head=surprised, '?' drawn shape"
  composition: {focal: host center 40% height, secondary: question mark top-right}
  character: {pose: arms_up_shrug, head: surprised}
  layers: [bg, body, head, qmark]
  animation: [{t: 0.0, op: cut_in, layer: body}, {t: 0.5, op: pop_in, layer: qmark, dur: 0.2}]
  camera: static
  transition: {in: hard_cut, out: hard_cut}
  acceptance: ["expression readable at 110 px head width"]
  why: "R-Q: questions get character/text, not evidence; resets attention after a table"
  leaves_out: "any legal stamp or statute"

- scene_id: S004
  audio: {start: 14.4, end: 16.0}
  narration: "Here is the trick."
  purpose: TEXT-ONLY
  visual_concept: "'The trick' in hand-lettered type centered on white, nothing else"
  layers: [bg, text]
  animation: [{t: 0.0, op: cut_in, layer: text}]
  camera: static
  transition: {in: hard_cut, out: hard_cut}
  acceptance: ["single element on frame"]
  why: "R-T rhetorical beat"
  leaves_out: "everything"

- scene_id: S005
  audio: {start: 16.0, end: 24.4}
  narration: "The bank pays you almost nothing for your money, lends it out at a much higher rate, and keeps the gap."
  claim_ids: [C-04]
  purpose: DIAGRAM   # R-M: one concrete machine, not dashboard
  concept: "money in cheap, out expensive, gap kept"
  visual_concept: "drawn 'bank' box with a pipe in from the left (thin, label 'pays you: low') and a pipe out to the right (thick, label 'charges: high'); the thickness difference is colored red and labelled 'the gap'"
  composition: {focal: bank box center 50%, secondary: you (small stick figure) left, borrower right}
  character: {pose: arm_pointing, head: flat_skeptical}   # host as small narrator bottom-left
  layers: [bg, bank, pipe_in, pipe_out, gap_red, labels, host_body, host_head]
  animation: [{t: 0.0, op: cut_in, layer: bank}, {t: 1.5, op: pop_in, layer: pipe_in}, {t: 4.0, op: pop_in, layer: pipe_out}, {t: 6.8, op: draw_on, layer: gap_red, dur: 0.5}]
  camera: static
  transition: {in: hard_cut, out: hard_cut}
  acceptance: ["pipe widths same px/unit as any later chart", "'gap' appears on 'keeps the gap'"]
  why: "R-X cause -> object showing mechanism; pop-ins staged to the three clauses"
  leaves_out: "numbers (saved for S010)"

- scene_id: S006
  audio: {start: 24.4, end: 28.0}
  narration: "That gap has a name: the net interest margin."
  claim_ids: [C-05, C-12]
  purpose: TEXT-ONLY then definition
  visual_concept: "same bank diagram collapses to the red gap; lettered phrase 'net interest margin' on white with an arrow to the gap"
  layers: [bg, gap_red, text, arrow]
  animation: [{t: 0.0, op: cut_in, layer: gap_red}, {t: 1.8, op: text_swap, layer: text}]
  acceptance: ["term spelled exactly; do not add a formula the narration does not give"]
  why: "naming the term needs the term as on-screen text"
  leaves_out: "NIM formula (see C-12)"

- scene_id: S007
  audio: {start: 28.0, end: 33.2}
  narration: "In the early 1980s, rates were so high that banks competed for deposits."
  claim_ids: [C-06]
  purpose: HISTORY
  visual_concept: "text 'Early 1980s' then a redrawn line chart from a FRED CSV (rates 1978-1985), ring on the peak; small source tag"
  main_subject: "redrawn FRED chart from the data file held locally (evidence/fred/*.csv sha256)"
  layers: [bg, axes, line, ring_red, year_text, source_tag]
  animation: [{t: 0.0, op: text_swap, layer: year_text}, {t: 1.2, op: cut_in, layer: line}, {t: 3.2, op: draw_on, layer: ring_red}]
  acceptance: ["y-axis labelled with series name + unit", "peak value matches CSV row"]
  why: "R-D + HISTORY; no authentic screenshots exist for the period, so a data redraw is the playbook fallback"
  leaves_out: "deregulation details (only if a source supports 'competed')"
  note: "if only a Fed History page supports the deposit-competition claim, use it as a 2-s headline reveal after the chart (template 1)"

- scene_id: S008
  audio: {start: 33.2, end: 43.2}
  narration: "Today, the Federal Reserve says the average credit card rate is above twenty percent, while many big-bank savings accounts still pay well under one percent."
  claim_ids: [C-07, C-08]
  purpose: EVIDENCE   # two-source comparison, template 7
  visual_concept: "two crops side by side on white: LEFT G.19 row (same crop as S002), RIGHT big-bank savings rate pages or FDIC national-rate row; different colour frames per source; ring left on 'twenty', ring right on the sub-1% figure"
  composition: {focal: two crops 44% width each, gap 4%}
  real_evidence: {files: [evidence/federal-reserve/g19.png, evidence/<bank-or-fdic>/rate.png], retrieved: TBD}
  animation: [{t: 0.0, op: cut_in, layer: left_crop}, {t: 2.6, op: draw_on, layer: ring_left}, {t: 4.6, op: pop_in, layer: right_crop}, {t: 8.0, op: draw_on, layer: ring_right}]
  camera: static
  acceptance: ["same px scale per crop, scales differ and are labelled if charts", "retrieved date visible on each tag", "colour per source reused in S012"]
  why: "R-S named org; two numbers contrasted by two documents"
  leaves_out: "any generic dashboard"

- scene_id: S009
  audio: {start: 43.2, end: 46.4}
  narration: "Imagine you hand a bank one hundred dollars."
  claim_ids: [C-09]
  purpose: EXAMPLE
  visual_concept: "host hands a drawn $100 note to a small bank building; label 'simplified example' in the corner"
  character: {pose: arm_extended, head: neutral}
  layers: [bg, bank, note, host_body, host_head, label]
  animation: [{t: 0.0, op: cut_in, layer: host_body}, {t: 1.0, op: slide_in, layer: note, dur: 0.4}]
  acceptance: ["label 'simplified example' present"]
  why: "R-E 'imagine'; literal staged prop"

- scene_id: S010
  audio: {start: 46.4, end: 54.0}
  narration: "It lends ninety of them to a stranger at twenty percent, pays you fifty cents, and keeps the difference."
  claim_ids: [C-09, C-12]
  purpose: DIAGRAM + NUMBER
  visual_concept: "the $100 note splits into $90 (to stranger, arrow labelled '20%') and $10 stays; separate small pouch labelled '$0.50 to you'; the leftover is a red-bordered pile labelled 'bank keeps' with NO computed dollar total unless the owner approves $17.50 gross"
  layers: [bg, note_split, arrow, stranger, pouch_you, pile_red, labels]
  animation: [{t: 0.0, op: cut_in, layer: note_split}, {t: 2.0, op: pop_in, layer: stranger}, {t: 4.2, op: pop_in, layer: pouch_you}, {t: 6.4, op: pop_in, layer: pile_red}]
  acceptance: ["numbers pop at final value", "90 + 10 = 100 visible", "label 'before costs and losses' if total shown"]
  why: "R-N number sentences get large numbers; stagger = clauses"
  leaves_out: "defaults, reserves, costs (add one small caption if owner wants honesty on S010)"

- scene_id: S011
  audio: {start: 54.0, end: 54.8}
  narration: "But wait."
  purpose: CONTRAST
  visual_concept: "host head=surprised, hand up; or strike-through line over the previous 'bank keeps' pile"
  character: {pose: hand_up, head: surprised}
  layers: [bg, body, head]
  animation: [{t: 0.0, op: cut_in, layer: body}]
  why: "R-C"
  note: "0.8 s scene: legal as a hard-cut accent"

- scene_id: S012
  audio: {start: 54.8, end: 56.8}
  narration: "Online banks pay four percent."
  claim_ids: [C-10]
  purpose: NUMBER / EVIDENCE
  visual_concept: "crop of a named online bank's savings APY with ring on the figure; source tag with retrieved date; reuse right-frame colour from S008 for 'savings' only if same source family"
  real_evidence: {file: evidence/<online-bank>/apy.png, retrieved: TBD}
  animation: [{t: 0.0, op: cut_in, layer: apy_crop}, {t: 1.0, op: draw_on, layer: ring_red, dur: 0.5}]
  acceptance: ["APY visible and equals 4% on retrieval day, otherwise the claim and caption change", "tag shows date"]
  why: "R-N + R-S"

- scene_id: S013
  audio: {start: 56.8, end: 60.4}
  narration: "So why does anyone stay at the big banks?"
  purpose: REACTION / question
  visual_concept: "host between two doors/buildings (big bank, online bank), head=flat_skeptical, '?' mark"
  character: {pose: arms_down, head: flat_skeptical}
  animation: [{t: 0.0, op: cut_in, layer: host_body}, {t: 1.2, op: pop_in, layer: qmark}]
  why: "R-Q"

- scene_id: S014
  audio: {start: 60.4, end: 64.4}
  narration: "Because moving money feels like work, and banks know it."
  claim_ids: [C-11]
  purpose: METAPHOR
  visual_concept: "host drags a heavy drawn sack labelled 'my money' toward the other door, sweating head=worried; a small bank figure watches with arms crossed"
  character: {pose: pulling, head: worried}
  animation: [{t: 0.0, op: cut_in, layer: sack_scene}, {t: 2.4, op: pop_in, layer: bank_watcher}]
  acceptance: ["bank watcher appears on 'banks know it', not before"]
  why: "R-X cause; intent claim stays drawn since no data graphic can support it"
  leaves_out: "any statistic on switching until C-11 is sourced"
```

Scene count 14, about 13 hard cuts/min plus 20+ intra-scene pop-ins/draws, giving a states rate in the playbook's 19-53/min range. Median scene length is about 3.6 s, near the 2.9 s prior; longest holds are S008 (10 s) and S005/S010 (about 8 s), allowed because a table/diagram is being explained.

---
## 3. Evidence / source-document treatment

| scene | template (playbook sec. 5) | highlight | timing |
|---|---|---|---|
| S002 | 4 table row emphasis | red ring on the card-rate cell | table cut in at sentence start (5.2 s); ring ~4.6 s after entry on "twenty" (within the reference median 4.8 s) |
| S007 | 5 official chart (redrawn from FRED CSV) | red ring on the peak | text 'Early 1980s' at start; chart at +1.2 s; ring at +3.2 s |
| S008 | 7 two-source comparison | red ring left on "twenty", red ring right on the sub-1% figure; different frame colour per source | left in at start; ring +2.6 s; right crop +4.6 s; ring +8.0 s |
| S012 | 1 headline reveal + ring | red ring on APY | crop at start; ring +1.0 s (figure is first words, so shorter than median) |
| S006/C-06 optional | 1 headline reveal | yellow marker only if a Fed History sentence matches narration | 2 s |
| S010, S014 | none | hypothetical, drawn, not a source | labelled "simplified example" |

Not covered by evidence (and why): S001 (undefined claim), S003/S004/S009/S011/S013 (rhetorical/staged), S014 (intent claim). Highlighted words must equal the narrated claim (playbook step 9); if G.19 value differs from "above twenty percent", change the on-screen text to the verified value and flag the narration.

---
## 4. Asset specs (method, owner)

| asset | method | owner | note |
|---|---|---|---|
| host rig (body poses: arms_down, arms_up_shrug, arm_pointing, arm_extended, hand_up, pulling; heads: neutral, surprised, flat_skeptical, worried, smile) | generate (Codex), transparent PNG layers + anchor.json | Codex produces, Claude validates alpha/anchors/pairings sheet | one-pass set approval, no repeated master loops |
| bank building / big-bank vs online-bank icons | generate in the same style (2 variants) | Codex | no real logos |
| jar, coins, coffee cup, sack, doors, $ note, pouch | generate | Codex | one prop per concept |
| pipes, arrows, rings, labels, 'gap' red band, text cards | procedural (PIL/SVG) | Claude | exact numbers |
| FRED chart | procedural redraw from CSV | Claude | scale-labelled |
| G.19 crop, FDIC rate crop, bank APY crops | screenshot (authentic capture, manifest with URL/date/sha256) | Claude | needs missing screenshot-layer renderer (crop, marker, ring, zoom) and capture helper (playbook sec. 11 "missing capabilities") |
| source tags | procedural | Claude | >=3.4% frame height, bottom-left |
| reuse | check `PRODUCTION_SYSTEM/asset_registry.json` for existing poses/props before ordering | Claude | I did not open it |

Fonts: OFL only (Patrick Hand, Caveat Brush for numerals, Atkinson Hyperlegible for tags), per playbook sec. 7.

---
## 5. Character poses/expressions per beat

S001 none; S002 none (card icon only); S003 arms_up_shrug + surprised; S004 none; S005 arm_pointing + flat_skeptical (small, bottom-left); S006 none; S007 none; S008 none; S009 arm_extended + neutral; S010 none (host leaves, objects carry); S011 hand_up + surprised; S012 none; S013 arms_down + flat_skeptical; S014 pulling + worried. Host appears in 6 of 14 scenes, always as reaction, example, or scale reference. Head swaps are hard, no lip sync, no idle bob.

---
## 6. Financial graphic choices

- S005/S010: pipe-and-box machine and a physical split of one $100 note, because the lesson is a flow and a gap; a number dashboard would show rates but not why the bank profits (R-M: money abstraction -> one concrete object).
- S002/S008/S012: real publisher tables/rate pages, because narration names the Federal Reserve (R-S); a stat tile would carry no proof.
- S007: one line chart from a held data file, because history is a shape (HISTORY), with ring on the peak; no KPI cards, no sparkline grid.
- S001: object pairing, not a bar chart, because the claim is unsourced.
- Not used: gauge/arrow "rate up" widgets, side-by-side KPI tiles of 20% vs 0.5% (I wanted one for S008, see KB GAPS).

---
## 7. Motion specs and editing decisions

- All transitions: hard cuts at sentence starts (S001-S014 boundaries are sentence starts). No cross-dissolves, no camera moves, no zooms (a ZOOM_IN document zoom is allowed by the playbook for S002 if the table text is under phone-legibility; default static).
- Pop-ins: 3-6 frames at 24 fps (S001 cup, S003 '?', S005 pipes, S010 stranger/pouch/pile, S013 '?', S014 watcher). Stagger 0.4-0.7 s only where clauses are separate; S005 uses clause-timed 2-2.5 s gaps because the sentence is long.
- Draw-ons: rings 0.5-0.6 s, linear steps (S002, S007, S008, S012).
- Number pop at final value only (S010 $90, 20%, $0.50). No counters.
- Holds: S002 table ~7 s still; S008 ~10 s with 4 internal events; S005 about 8 s with 4 events. Stills stay still.
- Slide-in only: S009 note (0.4 s), the single eased move.
- Host never idle-animates.
- Audio: voice only plus optional light bed; no sound claims. Narration is the master: no edits; any edited seam needs a human listen.

---
## 8. Acceptance criteria

Technical: decodes clean, 1920x1080, fps/duration match the voice master, last word not truncated, hard-cut boundaries clean.
Content: every on-screen number maps to a claim id and a verified value from the evidence file on retrieval date; C-01 resolved before any figure appears in S001; S002/S007/S008/S012 rings land within 0.3 s of the spoken figure; highlighted/ringed words equal the narrated claim; S010 labelled "simplified example" and does not show a total profit unless owner approves; "average" wording on card rate; source tag (publisher + date) bottom-left on every evidence scene; S008 scales labelled and per-source colours consistent through S012.
Visual: figures legible at 25% frame height (phone); expression readable at 110 px head width; no tofu glyphs, arrows are shapes; one red accent per beat; no decorative imagery; no dashboard widgets.
Process: 15-20 s proof of S002+S008+S010 reviewed by an independent reviewer; max 2 fix loops; SHA-256 manifest for evidence; final file reviewed by a reviewer who is not the author.

---
## KB GAPS (honest list)

Unclear / missing / forced guesses:
1. The playbook's "10 questions" are a reasoning log but no file or format says where it lives or how long it must be; I compressed to `why`/`leaves_out`. Unclear whether the log is mandatory per beat.
2. Claim-register columns are only hinted ("id, text, type, needs_evidence Y/N"). The pointer is to `V1/RESEARCH_DOSSIER.md`, which I was told not to open; I invented status/source columns.
3. No rule for scripts that contain misleading or unsupported claims (here: C-01 "less than a coffee", C-09/C-12 "keeps the difference" implying a ~17-point margin vs. real net interest margin definition, C-02 "the bank that holds it" implying the same bank). Sec. 13 handles unverifiable claims and voice/script mismatches but not "true but misleading framing". I flagged to owner; the KB has no escalation channel.
4. No rule for illustrative/hypothetical numbers (S009-S010): how to label, whether to show derived totals ($18, $17.50). I invented the "simplified example" label.
5. No guidance for evidence of a historical period (early 1980s) where no authentic screenshot exists. I used the "redrawn chart from a data file" fallback by inference; it's allowed by sec. 5 last line but not shown for history.
6. No guidance on how many scenes/beats to merge: playbook says "one scene per beat", but very short sentences ("Here is the trick.", "But wait.") become 0.8-1.6 s scenes. Is that fine? Unknown; I kept them.
7. Timing: no stated words-per-second for planning other than the 150 wpm in this task; the playbook says to use ASR times (step 5), which I do not have. All times are guesses.
8. Evidence-ring timing: median 4.8 s after source enters is given, but my sentence-driven timing (the figure is 0.4 s per word in) conflicts; I picked sentence-driven for S002 and the median for S008.
9. "Federal Reserve says" has two possible G.19 series; the playbook has no rule for choosing between two defensible official numbers.
10. Using named bank/competitor rate pages on screen (brand/rights/advertising-look): rights are "[U]" in the KB. I proposed capturing named bank pages with dates and recommended no logos; the playbook's licensing field is a single sentence with no policy.
11. No rule for shots with two evidence crops that are different document types (table vs bank web page): scale/color rule exists only for charts.
12. Character: no rule for when the host should NOT carry the beat; I defaulted to "reaction, example, scale reference". No spec for small-host-in-corner sizing beyond "15%" in the template.
13. The playbook says "faster imagination in storyboards" (owner pref) but gives no definition; I did not know how inventive a metaphor may be (pipes, door scene).
14. Codex vs Claude split is clear for artwork vs procedural; unclear who owns "prop illustrations that must also carry exact numbers" (e.g. note with $90). I made Claude add labels over Codex art.
15. No rule for the hook/opening seconds (S001-S002) or for question-sequence runs (S003-S004 back to back); R-Q and R-T conflict on it.
16. I did not open `22_LONGFORM_VISUAL_DNA.md`, BEAT_STATS, or EVIDENCE_FRAMES, so any claim here that cites a stat (13 cuts/min, 3.6 s median) is from the playbook only.
17. Fee-free ambiguity: playbook sec. 8 says hold still, but the rule for allowed "slide_in" count per minute is absent.

Temptations I noticed and handled:
- Dashboard: for S008 and S010 I wanted a 20% / 0.5% big-number tile pair. Rejected for two source crops (S008) and a physical split (S010).
- Constant motion: wanted a counting-up interest figure in S010 and a slow push-in on the table; rejected (playbook sec. 7-8).
- Decorative imagery: wanted a stock bank-building photo and money-rain on S005/S001; rejected, used mechanism drawings.
- No evidence: S001 and S011-S014 have no authentic source. S001 is a real gap (the claim cannot be verified as worded); S013-S014's behavioral claim needs a source or must stay narrator opinion. I listed both rather than faking a chart.
- Smaller temptation: showing a "$17.50 profit" total; held back as it overstates real bank profit.

Not tested: nothing was rendered, no web access, no ASR; sources named are publishers/pages I believe exist, but their current values are unverified.
