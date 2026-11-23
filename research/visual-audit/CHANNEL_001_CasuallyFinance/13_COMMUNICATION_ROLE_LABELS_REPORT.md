# Communication-role labelling pilot (2026-11-20)
Videos: yViMyIVOHkQ (404 states, long), eePIUX0Sd6c (186, long), turJ6VMfUjI (62, Short), CFrVTZBYa3Q (70, Short). 722 states. File: `13_COMMUNICATION_ROLE_LABELS_4VIDEOS.csv`. Script: `tools/label_communication_roles.py`.

Taxonomy (what the viewer is given at that moment): HOST, DATA_VISUAL (chart, number, price), EVIDENCE (third-party article, screenshot, meme, logo), METAPHOR_CHARACTER (anthropomorphic map/bars/earth), CAST_SCENE (people in a scene), PROP_OBJECT, TEXT_POINT (bubble, caption, card), REACTION (pose/expression), ANNOTATION (arrow, ellipse), TIME_NUMBER, OTHER.

Counts: TEXT_POINT 133, PROP_OBJECT 129, DATA_VISUAL 100, CAST_SCENE 99, EVIDENCE 70, REACTION 46, METAPHOR_CHARACTER 44, HOST 40, ANNOTATION 36, TIME_NUMBER 13, OTHER 12.

How labels were made: keyword rules over the existing ledger text (label, visible text, asset ids). No frames were re-viewed. Status: RULE_DRAFT, INFERRED.

Accuracy check (auditor reading the ledger text, not an independent human): 60-state sample 1 = 47/60 (78%); rules fixed; fresh sample 2 = 47/60 (78%); rules fixed; fresh sample 3 = 51/60 (85%). Last small rule fixes (map characters, profile screens, text cards) were applied after sample 3 and are NOT re-checked. Sample 3 is the honest estimate: about 85% agreement with the auditor, unverified by the owner.

Common errors: third-party chart images with a character on top; icons with arrows; scene captions held on screen; blank or question-mark states.

Does it help the decision model? Leave-one-video-out, predicting entering class (CUT, POP_IN, POSE, TEXT_SWAP, OTHER):
| Model | Accuracy |
|---|---|
| Always majority class | 48.6% |
| Previous class only | 38.8% |
| Role + previous class | 40.4% |
Result: NO. Roles do not predict the entering class better than a constant guess. Per video, roles beat the others only in 2 of 4 videos. Training on 3 videos is small, so this is not comparable to the earlier 53% (11 videos). Reading: entering class (cut vs pop-in) looks driven by the editor's rhythm per video, not by what is shown. Role labels may still describe WHAT to show for an idea; that use is untested.

Decision: do not extend labels to more videos for this purpose. Decision-model score stays 1/5.

## Follow-up test: role grammar (next role, duration)
Leave-one-video-out over the same 4 videos (718 transitions). Labels are the INFERRED rule drafts above.

| Predict | Baseline | Result |
|---|---:|---:|
| Next role | majority 10.7% | previous role 26.7% (previous 2 roles 22.3%) |
| Duration MAE (s) | global median 0.874 | median per role 1.016 (worse) |

Reading: the previous role carries some information about the next role (about 2.5x the majority baseline), so a weak storyboard grammar exists. Role does not predict duration. Only 4 videos, labels are drafts, and the next-role gain was not checked against a rule-free baseline, so this stays INFERRED and adds no score.
