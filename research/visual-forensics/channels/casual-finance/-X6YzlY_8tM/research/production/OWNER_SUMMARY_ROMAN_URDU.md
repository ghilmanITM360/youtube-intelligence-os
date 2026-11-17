# OWNER SUMMARY (Roman Urdu) — -X6YzlY_8tM "The SpaceX IPO... It's Worse Than You Think" (Checkpoint J)

**Verdict: `VIDEO_005_PARTIAL_STRUCTURE_SECOND_PASSED` — `CT_SCAN_COMPLETE` NAHI diya.** Audio sun'ni baqi hai aur semantic certification nahi hui.

1. **Video ID confirm?** Source SHA-256 `adff6676…1463ec` manifest se match karta hai (is session mein dobara compute kiya). 1280×720, 24 fps, 21,410 frames. Identity `HIGH_CONFIDENCE_NEEDS_REVIEW` (live YouTube page dobara check nahi hua).
2. **Decoded frames:** 21,410. Decode karna aur dekhna alag hain.
3. **Shots:** shot count verify nahi hua. Structural unit state/composition hai.
4. **Visual states:** 478 states (18,604 frames) aur 284 compositions. 109 unowned gaps (2,806 frames, 13.1%) alag segments rakhe, absorb nahi kiye. Frame partition mein 0 unaccounted, 0 overlap (sirf structural).
5. **Events:** 802 edit events (53.9/min). Sab se zyada FULL_REPLACE 216, ADDITIVE_ENTRY 188, POSE_SWAP 71, OBJECT_MOTION 61.
6. **Reviewers:** R01–R11 sab ka output hai (821 items): 733 CONFIRMED, 47 RECLASSIFIED, 23 NOT_A_CHANGE, 13 SPLIT, 4 UNVERIFIED, 1 NO_SPLIT. 429 candidates abhi sirf first-pass par hain.
7. **CONFIRMED sample:** 572 mein se sirf 143 dobara dekhe gaye: 137 theek, 3 reclassified, 3 unverified (2.1% ghalat type, 2.1% unverified). Yeh sab 572 ka second-pass nahi hai.
8. **Merge aur gaps:** 200 merge flags par rulings: 194 accept, 6 alag rakhe. 43 gap-crossing merges ka faisla gap review ke baad hua (2 gap mein nayi composition mili). Saare 109 gaps sirf SAMPLED hain: 76 neighbour ka continuation, 33 mein nayi composition/transition ka claim.
9. **Splits:** 13 SPLIT proposals mein se 5 measured hard cut se supported (EP0188, 0206, 0211, 0212, 0229); 8 sirf reviewer ke multi-event claims hain.
10. **Viewing quality:** 176 items native resolution par, 343 evidence jpg se, 302 sampled. Contact sheets se poora inspection ka dawa nahi.
11. **Techniques (OBSERVED):** hard cut ke baad elements ek ek karke pop-in, pose swap, teacher/board scenes, news/company cards, rocket/satellite doodles, podcast clip embedded. Rang, typeface, easing: UNAVAILABLE.
12. **Pacing (MEASURED):** state median 1.21 s, p90 3.33 s; 32.1 states per minute.
13. **ASR alignment:** machine ASR (Whisper base, 214 sentences, suna nahi). 54.2% sentences boundary ke 0.25 s ke andar shuru hoti hain jabke shuffled baseline 31.5% (p95 35.5%): narration aur cuts mein asli taalluq nazar aata hai, lekin text/timing unverified.
14. **Chhoti cheezein chhootne ka risk:** Haan. Gaps aur bohat se merges sampled hain; chhote text/micro-events miss ho sakte hain. EP0342 UNVERIFIED rehta hai; frames 6237–6349 mein EP0229 ke multiple boundaries reviewer claim hain.
15. **MEASURED / INFERRED:** MEASURED = frame counts, durations, diffs, ASR overlap. OBSERVED = reviewer ne frames mein dekha. INFERRED = story function. UNAVAILABLE = colours, typeface, easing, audio.
16. **Validation:** `validate_v2.py` PASS aur 4 negative tests DETECTED; reviewer outputs ke validators (negative test sameet) PASS. Semantic validation nahi hui.
17. **CT_SCAN_COMPLETE?** Nahi.
18. **Audio / AV:** `AUDIO_NOT_VERIFIED`, `AV_CERTIFICATION_BLOCKED`. Checklist: `production/AUDIO_HUMAN_REVIEW_CHECKLIST_v2.md`.
19. **Source MP4, Finance repo:** MP4 ko haath nahi lagaya; `integrated_v1/` overwrite nahi hua (naya `integrated_v2/`); Finance worktree, PR #36 aur stashes ko haath nahi lagaya.
20. **Agle improvements:** (a) 429 first-pass candidates ka second pass, (b) 109 gaps native resolution par, (c) additive-element merge rule par stricter test, (d) colour/typeface sampling, (e) insaan ki listening, (f) cold-start test ek asli classifier ke saath. Cold-start test sirf retrieval completeness par PASS hua.
