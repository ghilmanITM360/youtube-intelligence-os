# 05 — Resume priority queue

Inputs: `03_VISUAL_ANALYSIS_COVERAGE.csv` (210 + 11 + 88 + 29 + 44 + 63 + 3 = 448 unique videos; 454 MP4 files).

## Channel comparison

| Channel | Established method | Validated progress | Local source | Reuse value | Writer risk | Next-step cost |
|---|---|---|---|---|---|---|
| CasuallyFinance | Strongest (A) | 38 complete, 10 structural | 210 unique (48 analysed set + 162 never-touched) | Very high: DNA docs at n=38 | **Machine A owns the branch**; B lacks numpy/PIL/whisper | Long-form 125 min total |
| casual_economics | Sampled structural (A) | 11/11 structural, 0 AV | 11/11 | Medium | Codex branch, closed | Needs human listening (owner) |
| xkcd Channel (What If) | Brain v1.0.0 | 12 historical | 88 | High once audited | External corpus | Audit before reuse |
| PrimateEconomics | None before today | 1 pilot (PARTIAL) | 29 | High (finance topic, animated) | None | Low |
| MonkeBiznis | None before today | 1 pilot (PARTIAL) | 63 | Medium | None | Low |
| PrimitiveEducation | None before today | 1 pilot (PARTIAL) | 44 (36 Shorts) | Medium | None | Very low (Shorts 11–35 s) |
| BarelyEvolved | None before today | 1 pilot (PARTIAL) | 3 | Medium (long-form history) | None | Low (2 left) |

## Ordered queue

1. **CF long-form LF-0 pilot `o3FQcd91MIs` (278 s)** — on **Machine A** with its existing pipeline (`STATUS.json → longform_procedure`). It is the oldest started, unfinished, highest-reuse item. It is not run on B, to avoid a second writer and new dependencies. Usage on 2026-10-23 is five-hour 4 % / weekly 1 %, so the 2026-10-20 usage blocker no longer applies.
2. **CF `turJ6VMfUjI` (63 s Short)** — newly unblocked: the source exists only on Machine B (`CasuallyFinance/…[turJ6VMfUjI].mp4`, sha256 in 02). Copy it to Machine A, or run here after the owner approves the deps. Finishing it completes all 39 CF Shorts known locally.
3. **Finish the 3/3 Barely Evolved set:** `GNaBxt_zIRA` (545 s), `mNLNb-Z4T0M` (557 s). It is the only channel where full coverage is achievable now.
4. **Second sample per new channel (Shorts vs long-form contrast):**
   - Primate Short `ktfog3MhqJY` (26 s);
   - MonkeBiznis Short `Mr1Y2pX5p94` (17 s);
   - Primitive long-form `KyBWJPaF1KI` (206 s);
   - Primate long-form `zszKDZwYYV0` (736 s).
5. **Promote the 4 pilots PARTIAL → COMPLETE:** frame-accurate state list (ffmpeg `tblend`/`signalstats` detector, see 04 C-2), then author each interval.
6. **xkcd:** audit What If brain coverage for the 12 mapped IDs against the B copies (ID match; hashes differ). Then sample unanalysed videos: `5k8ciEx__5w` (21 s Short) and `PUtI3xoaHx0` (159 s long-form). The title candidates `rGZ6TsXvi8E` and `TIDHee_Q5Gk` may correspond to the unresolved SRC01/SRC02. These are title matches only and are not verified.
7. **CF 161 never-touched videos:** only after decision 1 (which machine/pipeline owns CF).
8. **Casual Economics:** nothing visual is pending that can be done without human listening.

## Blocked / owner decisions

- Human listening and full AV sign-off: no agent can do it. It needs a person watching with sound.
- New Python dependencies on Machine B: need owner approval (pinned versions).
- Which machine writes CF editing forensics: currently Machine A.
