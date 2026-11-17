# Training Overlap Check

```
TRAINING_OVERLAP = NONE
```

Method: searched the frozen release's own transcript corpus only
(`01_master_data/MASTER_SENTENCES.csv`, 604 meaningful sentences across all 14
source videos) plus `SOURCE_VIDEO_INDEX.csv`. No internet search for matching
content was performed, per protocol §50 and §5.

## What was searched, and found

| Term | Hits in the 604-sentence corpus |
|---|---|
| `caffeine` | 0 |
| `energy drink` | 0 |
| `blood pressure` | 0 |
| `cardiac` | 0 |
| `doctor` | 0 |
| `patient` | 0 |
| `coffee` | 1 |
| `heart` | 1 |

Both single hits are incidental noun co-occurrences in unrelated questions:

- `weird_and_worrying_questions` S0000 — a question about chilling teeth until
  they shatter on drinking a hot cup of coffee. The word "coffee" appears; the
  subject is thermal fracture of enamel.
- `what-if-earth-grew-1cm-every-second` S0086 — a sentence about hearts being
  unable to pump blood to the brain under increased gravity. The word "heart"
  appears; the subject is planetary growth.

Neither video is about coffee, caffeine, energy drinks, blood pressure,
cardiovascular health, medical advice, or a doctor answering a patient. No
source video in the 14-video index is a medical or health video of any kind;
all 14 are xkcd-style physical-hypothetical explainers.

## Conclusion

The supplied coffee/heart script is **not** one of the 14 training/reference
scripts, and its subject matter, register (a doctor answering patients),
speaker structure (attributed first-person clinical opinion) and topic domain
(cardiovascular health) are all absent from the reference corpus. This is a
genuine different-niche generalisation input.

Two consequences worth stating plainly, since they bear on how the first pass
should be read:

1. **No medical visual precedent exists in the brain.** There is no corpus
   evidence for how this style handles a doctor figure, a patient, a
   consultation, a medical symbol or a caution mark. Those five decisions were
   made by transferring the corpus's *general* grammar (minimal stick figures,
   line-art icons, restrained accent colour, one-frame reveals) onto new
   subjects. They are the least evidence-backed decisions in the plan and the
   most useful ones for a reviewer to challenge.
2. **No CTA precedent exists either.** None of the 14 source videos ends on a
   channel call-to-action. VISUAL 05's F05.4 is therefore an extrapolation:
   it reuses the corpus's dominant `STATE_REPLACEMENT` grammar and keeps the
   established plate, line weight and character, but the corpus does not
   confirm that this is how these videos would end.
