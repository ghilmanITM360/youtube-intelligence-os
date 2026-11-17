# Narration script: "Blood Pressure After 65: When Is Lower Too Low?"
Decode Your Heart with Dr. Rehan · narrator layer v1 · 2026-11-02

**Story mechanism:** a treatment that protects your heart must also be safe for you.
**Viewer promise:** by the end, you'll know why "lower" isn't always "better" after 65, and which warning signs to tell your doctor about.
**Timecodes:** real source times from Whisper (see `edl.md`). The supplied transcript's times run up to ~10 s off.
**Base:** the user's example (`input/references/example_narration_style.md`). It is kept in tone and structure, and tightened for pace. Every change from it is listed at the end.

## Self-audit (Script Engine prompt 7)
| Check | Score / result |
|---|---|
| Naturalness | 9/10 |
| Clarity | 9/10 |
| Rhythm (staccato in the hook, longer lines later) | 8/10 |
| Voice consistency (calm, second person, no hype) | 9/10 |
| Voiceover readiness (no tongue-twisters, short sentences) | 9/10 |
| 10-year-old / 70-year-old test | Pass on every line. U01 is the densest, and it gets an on-screen card |
| 4-part hook (H01) | Situation ✔ · contradiction ✔ · reason to watch ✔ · handover ✔ |
| Open loops | 2 opened, 2 closed (see the retention map) |
| New medical claims | All are marked ⚠️ DOCTOR CHECK (J02 last line, the whole of U01) |
| Narrator share | ≈ 150 s of ~355 s ≈ **42%**. This is above the kit's 15–25%. Your own example is already ~105 s, and the corrections (J02, U01) are needed. The lean cut at the end brings it to ~36% |

## Retention map
- **Central argument:** after 65, blood pressure should still be treated, but the target and the medicine must fit the person, so that treatment doesn't cause dizziness and falls.
- **Acts:**
  1. Hook + intro: "is lower always better?"
  2. Why high BP must be treated (DR 0:00–0:40)
  3. The twist: falls and BP drops on standing (DR 0:40–1:39)
  4. What number counts as high (DR 1:39–1:56)
  5. The right medicine for the right person (DR 1:56–2:36) + evidence update
  6. Bottom line + takeaway + subscribe
- **Open loops:**
  - **L1** "Should it go even lower?" (H01) → closed by the doctor at 2:36–3:10 and by O01.
  - **L2** "How do doctors protect the heart without new danger?" (B02) → closed by the doctor at 1:56–2:36.
  - At most 2 loops are ever open at once.
- **Drop-off fixes:**
  - 0:00–0:40 jargon → H01/I01 before it, on-screen labels, and J01 straight after.
  - 1:25–1:56 numbers → a gauge/number visual and B01.
  - 1:56–2:36 drug chain → B02 before it, and an on-screen "condition → medicine" map using only his pairs.
  - The abrupt subscribe ending → O01 placed before it.
- **Breath:** a 0.5 s held frame with no music before O01's "never change your medicine on your own".

---

## Timeline

### [H01] COLD OPEN (recommended: Hook A, "the good news that isn't")  ~21 s
> You're 72. Your blood pressure is finally coming down.
> That sounds like good news.
> But now, every time you stand up… the room spins.
> So should your blood pressure go even lower?
> Or does your treatment need a second look?
> After 65, controlling blood pressure matters. But so does avoiding dangerous drops.

- **On screen:** `LOWER… OR TOO LOW?`
- **Visual idea:**
  - A huge BP reading ticks down digit by digit. These are illustrative numbers; no number is spoken.
  - On "stand up", the ECG/BP line dips hard and the frame tilts 2°.
  - Then a split card: **Protect the heart | Avoid dizziness & falls**.
- **Why it works:**
  - Situation: age 72, BP finally falling.
  - Contradiction: "But… the room spins."
  - Reason to watch: "even lower, or a second look?"
  - Handover: into I01.

### [I01] DR. REHAN INTRO  ~15 s
> Here's Dr. Rehan Omer, Consultant Interventional Cardiologist and Diabetologist.
> That means he opens blocked heart arteries without open surgery, and he treats diabetes too.
> He'll explain why the right blood pressure target isn't the same for everyone.

- **On screen:**
  - The lower third on his first frame: `Dr. Rehan Omer` / `Consultant Interventional Cardiologist & Diabetologist`.
  - Small series tag: `DECODE YOUR HEART`.
- The plain meaning is taken from `kit/05` (the facts the user supplied). No hospital or city.

### [DR 0:00.0 → 0:40.2] Dr. Rehan: high BP is one of the biggest causes of heart disease, so it should always be treated.
- **On-screen labels** (plain meaning, 2 s each):
  - `Hyperlipidemia = high cholesterol`
  - `INTERHEART = a large worldwide heart-attack study`
- Trims: none planned. The exact out-point is "…underlying hypertension." (to be set from Whisper word timings).

### [J01] after "underlying hypertension" (0:40)  ~12 s
> In plain words: after high cholesterol, high blood pressure is one of the strongest causes of blocked heart arteries.
> That's why it should be treated.
> But after 65, there's a catch.

- **On screen:** `#2 CAUSE OF BLOCKED HEART ARTERIES` with cholesterol as #1, ghosted. This is his own ranking ("after hyperlipidemia").
- The handover leads straight into his "However, people who are elderly…".

### [DR 0:40 → 0:59.6] Dr. Rehan: older people fall more easily. Their BP can drop when they stand, so they feel dizzy and fall.
- **On screen:** an outline figure rises from a chair; the BP line dips under it.
- The label reads **`Orthostatic hypotension`** (correct spelling). His audio says "hypertension". The audio is not edited.

### [J02] after "…they fall down." (0:59.6)  ~23 s
> Quick fix on one word.
> When blood pressure drops as you stand up, it's called orthostatic hypo-tension. "Hypo" means low.
> You get up, your pressure falls, and you may feel dizzy, or even faint.
> ⚠️ DOCTOR CHECK → That's why a doctor may check your blood pressure sitting and standing.
> So, with falls in the picture… should older people be treated at all?

- **On screen:** `HYPER = HIGH` struck through → `HYPO = LOW ✓`. Then two cuffs side by side, labelled "sitting" and "standing".
- The last line bridges into his "So in those patient population, initially it was thought…".
- ⚠️ "Hypo-tension" corrects his wording, so Dr. Rehan must OK it. The "sitting and standing" line comes from the user's example, but he does not say it.

### [DR 0:59.6 → 1:39.2] Dr. Rehan: doctors once thought treating BP in the elderly did more harm than good. Then a big trial showed treatment helps (systolic under 150).
- **On screen:**
  - `OLD BELIEF: treatment = more harm`, stamped out.
  - `TRIAL: treat it` → `top number < 150`.
  - **Only the systolic number is shown** (he says "systolic"). His "150 by 90" is corrected later in U01.
- The trial label `HYVET` appears only after Dr. Rehan confirms that "hybrid" = HYVET. ⚠️

### [B01] after "…millimeters of mercury." (1:39.2)  ~6 s
> So what counts as "high" for an older person?
> That line has moved over the years.

- **On screen:** a horizontal number line with a marker sliding from 150 toward 140.

### [DR 1:39.2 → 1:56.3] Dr. Rehan: newer advice says older people with BP above 140/90, especially with other conditions, should be treated.
- **On screen:** `140/90 + other conditions → treat`. "Compelling indications" is shown as `other conditions that make treatment clearly needed`.

### [B02] after "…should always be treated." (1:56.3)  ~17 s
> Here's the challenge.
> Leave high blood pressure untreated, and your heart is at risk.
> Lower it carelessly, and dizziness and falls become the risk.
> So how do doctors protect the heart without adding new danger?
> By choosing the medicine to fit the person.

- **On screen:** a balance scale with ❤️ protect on one side and ⚠️ falls on the other. It levels out on "fit the person".
- This opens loop L2. The user's bridge was moved here from 1:28, because 1:57 is where he answers it.

### [DR 1:56.3 → 2:36.2] Dr. Rehan: the choice of medicine depends on the person's other illnesses.
- **On screen:** a "condition → medicine" map that builds row by row, **only with his pairs**:

  | Condition | Medicine he names |
  |---|---|
  | Prostate enlargement (BPH) | Alpha blockers |
  | Coronary artery disease | Beta blockers |
  | Kidney disease (CKD) / diabetes | ACE inhibitors / ARBs |

- At 2:00–2:14 ("no diuretics… may cause the flaccid heart disease"; Whisper hears "flexible cardia"), only `Avoid sudden drops in BP` is shown. ⚠️ No caption claims a meaning for "flaccid heart disease".

### [U01] EVIDENCE UPDATE, after "…ACE inhibitors or ARBs." (2:36.2)  ~27 s  ⚠️ DOCTOR CHECK (whole block)
> One point needs a little more detail.
> Diuretics, often called water tablets, aren't automatically off-limits for older adults.
> In fact, the HYVET trial, in people aged 80 and over, used one, and aimed for 150 over 80.
> Today, there's no single target for everyone.
> Doctors also weigh dizziness, frailty, kidney function and other conditions.
> Even some prostate medicines can make blood pressure drop when you stand.

- **On screen:** a light-3D comparison chart, labelled by trial/guideline and age group:
  - `HYVET (80+) · 150/80`
  - `Dr. Rehan's newer cutoff · 140/90`
  - `Today: individual target`
- ⚠️ This partly corrects him (diuretics, 150/80, alpha blockers). **It cannot go in without his approval.** The source is the user's clinical note: HYVET used indapamide, a diuretic, and targeted 150/80 in people aged 80+.

### [DR 2:36.2 → 3:10.3] Dr. Rehan: bottom line: treat it, adjust the dose, consider other illnesses, and see a trained specialist.
- **On screen:** three ticks: `✓ treat` · `✓ adjust the dose` · `✓ look at other illnesses`.
- At 2:56 he correctly says "postural hypotension" (Whisper). The label matches.

### [O01] FINAL TAKEAWAY, after "…geriatric cardiologists." (3:10.3)  ~27 s
> So, what should your blood pressure be after 65?
> There's no one number that's right for everyone.
> The real question is: is it being controlled *safely*?
> If you feel dizzy when you stand, keep falling, or feel unwell after your medicine, talk to your doctor.
> The goal isn't just a lower number. It's better protection.
> *(0.5 s breath)*
> And never change your blood pressure medicine on your own.

- This closes loop L1.
- **On screen:** `NOT LOWER. SAFER.`, then three warning signs as icons (dizzy on standing · repeated falls · unwell after medicine).
- **Disclaimer card** (text only, 3 s): `For education only. Talk to your own doctor before changing any medicine.`

### [DR 3:10.3 → 3:25.7] Dr. Rehan: subscribe request. **Kept, as the user asked.**
- **On screen:** a subscribe pill, animated.

### [END CARD] ~4 s
- **On screen:** `Decode Your Heart` / `with Dr. Rehan`.
- **[O02] optional** ~2 s:
  > Decode your heart, with Dr. Rehan.

---

## Options: alternative cold opens

**Hook B: "the pill that worked too well"** ~17 s (angle: hidden cost / unexpected consequence)
> Your mother takes her blood pressure pill every morning, right on time.
> Then one day she gets out of bed, feels light-headed… and falls.
> The pill did its job. Maybe too well.
> After 65, the danger isn't only high blood pressure. It's also how fast, and how far, it comes down.

- Supported by him: falls and fractures from an exaggerated drop (2:44–2:56).
- Strongest with viewers' adult children. Visual: an empty bedside, a pill organiser, the BP line dropping.

**Hook C: "the belief that flipped"** ~15 s (angle: contradiction / cause and effect)
> For years, many doctors believed something surprising.
> In older people, treating high blood pressure might do more harm than good.
> Then a major trial changed that thinking.
> But it left a new question: how low is too low?

- Supported by him at 0:59–1:39.
- Smart, but it starts with doctors rather than the viewer, so it hooks less in the first 3 s.

**Recommendation: A.**
- It is your own situation and is told in the second person, so a 65+ viewer recognises themselves in the first sentence.
- The contradiction ("good news… but the room spins") is real, not invented suspense.
- B is a close second. It would suit a family-focused Short later.

---

## Changes from the user's example (and why)
1. **Hook:** "you feel dizzy" became "the room spins". It is more concrete and staccato. "After 65, controlling…" moved from the intro into the hook as the reason to watch.
2. **Intro:** added one plain-meaning line for the titles (from `kit/05`).
3. **Bridge "Here's the challenge":** moved from 1:28 to **1:56**, where he answers it. "Heart and brain" became "heart", because he does not mention the brain. A short B01 now sits at 1:28.
4. **Orthostatic clarification:** placed at **0:59.6**, right after he describes it, and adds the gentle "hypo = low" fix for his slip.
5. **Evidence update:** placed at **2:36**. At 2:49 he is mid-sentence. It is about 20% shorter, with the same facts.
6. **Takeaway:** the same content, tightened. It sits before his subscribe request, since that is kept.
7. **Added J01** (plain-words recap of 0:00–0:39). This is the biggest drop-off risk.

## Lean cut (≈ −24 s → ~36% narrator)
- Drop J01 (on-screen labels only): −12 s.
- Drop J02's ⚠️ "sitting and standing" line: −5 s.
- Drop the U01 prostate line: −5 s.
- Drop O02: −2 s.
