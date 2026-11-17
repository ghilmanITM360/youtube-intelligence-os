# Visual Story — Coffee / Heart Short

Blind first pass. Visual grammar derived only from frozen Production
Intelligence Brain v1.0.0. Script unchanged.

## The one-line logic

The video draws a model, keeps drawing it until the viewer owns it, strikes it
out, deletes it, and replaces it with a different model. Everything else —
the energy-drink comparison, the three factors — hangs off that single spine.

## Sequence

```
BINARY MODEL DRAWN          coffee + heart, fork to GOOD? / BAD?
DOCTOR ENTERS, STRIKES IT   same frame, one red stroke
  ── hard cut ──
SECOND CONTAINER APPEARS    mug vs tall unbranded can
STRENGTH COMPARED           more stimulation marks over the can
CAUTION ADDED               one caution mark over the can only
  ── hard cut ──
BINARY RETURNS              now a patient asking a doctor
STRUCK AGAIN                one red stroke
MODEL DELETED               fork and labels removed; the space goes empty
  ── hard cut ──
REPLACEMENT MODEL           coffee → arrow → person → response reading
SECOND PERSON               same coffee, different reading
  ── hard cut ──
THREE FACTORS               blood pressure / heart response / quantity, one at a time
CTA                         factor list replaced by a video card with a play mark
```

## Why this shape and not another

**The binary is drawn twice on purpose.** The script rejects it twice (B02,
B07–B08), so it has to exist on screen twice. The second occurrence is not a
repeat of the first frame — it is re-staged as a consultation (doctor + patient)
so the rejection lands as something said to a person, not as a slide edit.

**The deletion is the hinge.** B08 removes the fork and leaves blank field.
That empty space is the argument: the old model is gone before the new one
arrives. The corpus's single most common motion type is `STATE_REPLACEMENT`
(230/438, 53%) — removing and replacing illustrated content inside a locked
frame is the grammar this corpus actually speaks.

**The energy-drink section is a detour, and is staged as one.** It is the only
place in the script where two physical objects are compared, so it gets the
only side-by-side composition in the video. It never touches the heart, the
doctor, or the fork — keeping it visually separate stops it contaminating the
central message with a second argument.

**The payoff is a person, not a verdict.** B09–B10 move the reading from the
cup to the body. Two people, one coffee, two different readings — which is the
main message stated as a picture rather than as a caption.

**The CTA does not change visual language.** Same off-white field, same line
weight, same doctor figure already on screen. Only the left-hand stack is
swapped for a video card. There is no end-screen, no glossy panel, no motion
the rest of the video has not already used.

## Shot-to-beat map

| Shot | Beats | Words | Base image | Est. duration |
|---|---|---|---|---|
| SH01 | B01, B02 | 1–17 | IMG01 | 4.3s ESTIMATED |
| SH02 | B03, B04, B05 | 18–48 | IMG02 | 7.9s ESTIMATED |
| SH03 | B06, B07, B08 | 49–80 | IMG03 | 8.1s ESTIMATED |
| SH04 | B09, B10 | 81–106 | IMG04 | 6.6s ESTIMATED |
| SH05 | B11, B12 | 107–130 | IMG05 | 6.1s ESTIMATED |

Total 33.1s ESTIMATED (130 words ÷ 3.93 words/sec, the measured delivery rate
of the 8 portrait videos in the frozen corpus). No measured timings exist —
no voice track has been recorded.

## Brain evidence for the overall shape

- **5 shots, not 9.** The frozen corpus's 8 portrait videos run 25–37 narration
  words per shot (407w/13, 430w/17, 510w/14, 523w/15, 333w/9). 130 words at
  that density is 4–5 shots. The per-shot median duration that falls out
  (6.6s) matches the portrait median of 6.45s. An earlier one-shot-per-concept
  draft produced 9 shots at 14 words each — half the corpus's shot length —
  and was rejected against this evidence.
- **Content changes inside the frame, not between frames.** 522/581 states
  (89.8%) report a LOCKED/STATIC camera (`VISUAL_DNA.md`). Every shot here is
  a locked frame whose illustrated content is added to or replaced.
- **Hard cuts only.** All 186 internal shot boundaries in the corpus measure a
  0.0s gap; zero fades, dissolves or wipes exist anywhere
  (`DECISION_RULES.md` §7). Every transition below is a hard cut.
