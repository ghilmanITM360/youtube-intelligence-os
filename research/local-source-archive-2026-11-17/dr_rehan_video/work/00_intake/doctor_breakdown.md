# Doctor breakdown: "Blood Pressure After 65: When Is Lower Too Low"

## Source facts (ffprobe + audio scan)
- File: `input/video/Blood Pressure After 65 When Is Lower Too Low.mp4`
- **3:25.75** (205.75 s), **2560×1440 HEVC, 30 fps**, AAC 44.1 kHz stereo, ~14.6 Mb/s
- Audio: **−16.1 LUFS integrated, LRA 3.9 LU**. The level is clean and steady, so it only needs a final normalise to −14.
- Pauses over 0.7 s: 14, and the longest is 1.1 s (1:53). **There is almost no dead air**, so trims will be small.
- Framing: a single wide locked-off shot. Dr. Rehan sits left of centre in an office chair, wearing navy-blue scrubs with an embroidered name. A plain light-grey wall fills about 40% on the left, which is **free space for text**. A monitor on the right shows a red heart. Because the source is 1440p, we can **punch in up to 1.33× at 1080p** with no quality loss, so one camera can be cut as "two angles".
- 9:16 crop: he sits about x 0.25–0.55 of the frame, so a vertical crop is easy, and the 1440 px height is plenty.

## Chapters (timecodes from the supplied transcript; Whisper word timings will refine them)

| # | Time | His point in one plain sentence | Difficulty (1–5) |
|---|---|---|---|
| 1 | 0:00–0:39 | High blood pressure is one of the biggest causes of heart disease (INTERHEART study), so it should always be treated. | 4 |
| 2 | 0:39–1:01 | Older people fall more easily, because their BP can drop when they stand up and make them dizzy. | 3 |
| 3 | 1:01–1:34 | Doctors once thought treating BP in the elderly did more harm than good, but a big trial showed treatment helps (target under 150). | 4 |
| 4 | 1:34–1:57 | Newer advice: elderly people with BP above 140/90, especially with other conditions, should be treated. | 4 |
| 5 | 1:57–2:42 | The choice of medicine depends on the person's other illnesses (prostate, heart artery disease, kidney disease or diabetes). | **5** |
| 6 | 2:42–3:11 | Bottom line: treat it, but adjust the dose, consider other illnesses, and see a trained specialist. | 3 |
| 7 | 3:11–3:25 | Subscribe request. | 1 |

## Jargon list (1-line plain meaning)
- **Hypertension**: high blood pressure.
- **Independent risk factor**: something that raises the risk on its own, even when other things are equal.
- **Coronary artery disease (CAD)**: narrowed pipes that feed the heart muscle.
- **Hyperlipidemia**: high cholesterol and fats in the blood.
- **INTERHEART study**: a large worldwide study of what causes heart attacks.
- **Orthostatic / postural hypotension**: BP drops when you stand up, so you feel dizzy or may fall.
- **Systolic BP**: the top number, the pressure when the heart squeezes.
- **mmHg**: the unit BP is measured in.
- **Antihypertensive**: a BP-lowering medicine.
- **Compelling indications**: other conditions that make treatment clearly needed.
- **Comorbidities**: other illnesses the person has at the same time.
- **Diuretics**: "water tablets" that make you pass more urine.
- **Benign prostatic enlargement (BPH)**: a non-cancer swelling of the prostate in older men.
- **Alpha blockers**: medicines that relax blood vessels, and also the prostate.
- **Beta blockers**: medicines that slow and calm the heart.
- **CKD**: chronic kidney disease, kidneys that slowly lose function.
- **ACE inhibitors / ARBs**: BP medicines that also protect the kidneys.
- **Geriatric cardiologist**: a heart doctor focused on older patients.

## Drop-off risk points
1. **0:00–0:39**: he opens with jargon ("independent risk factor", "hyperlipidemia", "INTERHEART") and gives no situation or story. **This is the biggest risk**, and it is why the cold open is placed before 0:00.
2. **1:22–1:57**: numbers come with no picture ("150 by 90", "140 by 90", repeated cutoffs). We need a visual of the number on a gauge or timeline.
3. **1:57–2:42**: a chain of drug names (alpha, beta, ACE, ARB, diuretic) in 45 s. We need an on-screen "condition → medicine" map. ⚠️ The map must show only the pairs he says.
4. **3:11**: the subscribe call to action ends the content abruptly. The final narrator takeaway should come **before** it, or replace it, depending on the user's choice.

## Lines needing ⚠️ DOCTOR CHECK (said vs likely meant)

| Time | He says | Likely meant / issue | Proposed handling |
|---|---|---|---|
| 0:51 | "orthostatic **hypertension**" | **hypotension**: he defines it as BP *dropping* when standing. (Whisper shows he self-corrects at 2:05, "hyper— postural hypotension", and says "hypotension" correctly at 2:56.) | A narrator clarification card ("BP drops on standing = orthostatic hypotension") plus a correct on-screen label. We do not edit his audio. |
| 1:14 | "**hybrid** clinical trial" | **HYVET** (Hypertension in the Very Elderly Trial) | Show the on-screen label "HYVET trial" only if he confirms it. |
| 1:28 | "less than **150 by 90**" | HYVET's target was **150/80** | Narrator evidence update (as in the user's example, §4). |
| 1:57 | "should not be given **diuretics**" | HYVET itself used **indapamide**, a diuretic | Narrator evidence update: diuretics are not automatically unsuitable. **He must approve this, because it partly corrects him.** |
| 2:13 | "may cause the **flaccid heart disease**" (Whisper: "flexible cardia", low confidence) | Unclear; possibly "falls", "fainting" or "flash pulmonary oedema" | Ask him. Until then, no caption claims a meaning. |
| 2:42 | "**geriatric cardiologists**" | Fine, but it is a niche specialty | The takeaway says "your doctor / a specialist". |

## Transcript check (Whisper large-v3 vs supplied transcript)
Files: `doctor_transcript_whisper.json` (word timings) and `.srt`.

- **The supplied transcript's timecodes drift by up to ~10 s.** For example, "However" is at 0:41 (supplied: 0:39), "The choice of drugs" at 1:57, and "to cut the long story short" at **2:37** (supplied: 2:35–2:42). All cut points now use the Whisper times (`01_script/edl.md` v2).
- **"Hypertension" slip:** it happens only once, at 0:51. At 2:05 he corrects himself ("hyper— postural hypotension"), and at 2:56 he says "hypotension". So there is less to fix than first thought.
- **0:58–0:59 stumble:** "they fall— out… fall down". This is trim candidate T1.
- **1:29–1:32 garbled stretch:** Whisper confidence is about 0, and it hears "150 by 90" twice. The supplied text has "In the earlier clinical trials, the cutoff… was 150 by 90" here. **Listen before deciding** (T2).
- **2:09–2:10:** "directly acting with the director". This is probably "diuretics". There is no caption on this.
- **2:13:** "flaccid heart disease" / "flexible cardia" is still unclear. ⚠️ Ask Dr. Rehan.
- **2:25–2:28:** "where our blockers" = "beta blockers". This is a recognition error, not his speech; the on-screen label says Beta blockers.
- **Ending:** the content ends at 3:10.3 ("geriatric cardiologist"), the subscribe request runs 3:10.3–3:24.9, and the file ends at 3:25.75.
