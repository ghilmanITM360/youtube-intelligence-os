# Dr Rehan (ch 30, Decode Your Heart) - thumbnail prompts, 4 videos

Written 2026-11-16. Status: DRAFT prompts, no image generated, no YouTube/Trends test run.

## 1. Evidence used (repo only)

Source: `docs/research/senior-health-2026-09-25/forensic-v2/THUMBNAIL-MATRIX.json` (149 hand-coded thumbnails, LIVE_WEB_VISUAL, 2026-09-25) and `research/senior-health-forensics/reports/*.md`.
Caveat from the file itself: features are pooled across channels, so they are confounded with each channel's template. Treat as direction, not proof. Medians are within-channel outlier multiples (1.0 = channel normal).

| Feature | n with | Median with | Median without | Reading |
|---|---|---|---|---|
| Large number in thumbnail | 74 | 2.13 | 0.80 | Strongest positive among common features |
| Answer withheld | 108 | 1.90 | 0.63 | Withhold the payoff |
| Answer revealed in thumbnail | 14 | 0.47 | 1.76 | 0 of 14 reached 3x. Do not show the answer |
| Medical illustration / 3D render | 99 | 1.76 | 1.00 | Positive |
| Warning icon | 18 | 0.55 | 1.24 | Negative, hit rate 17% vs 39%. Do not use |
| Medicine shown | 34 | 0.87 | 1.27 | Negative |
| High clutter background | 15 | 0.91 | 1.16 | Negative |
| Sketch / illustrated human | 41 | 0.38 | 1.10 | Weak. Use a real photo |
| Real face / doctor persona | 66 / 67 | about 1.1 | about 0.9-1.1 | Neutral. Keeps trust, not a lever |
| Extreme fear (death/die) | 6 | 5.23 | 1.03 | n=6, and a misinformation risk. Do not copy |

Winning layouts seen in the matrix:
- Dr. Okoro, 494K views (2,485x channel normal): text left, foot photo inset, doctor right, red background, yellow arrow at the foot.
- Doctor Thomas, 1.0M (122x): stacked yellow/white text left, doctor right pointing at the text, calm smile, low clutter.
- Dr. Aliza Wright, 219K (1,009x): same text-left / doctor-right frame, yellow/white text.
- Own channel: real clinic-photo presenter, only 56 videos, top video 1,222 views. Confidence is very low; no thumbnail effect can be inferred from it.

Rules taken from the above: one real face, one medical render, one big number or one short question, answer withheld, no warning icon, no medicine, no clutter, max about 6 words.

## 2. Hard constraints for all four

- Use Dr Rehan's REAL photo (his own clinic photo, calm or slight smile, looking at camera). Do not ask an image model to invent his face. Generate the background and the medical render with AI, then composite his photo and the text yourself in Canva/Photoshop. AI models spell text badly.
- Canvas 1280x720 (16:9), safe zone: keep text 80 px from every edge, bottom-right 200x60 px empty (YouTube timestamp).
- Same family on all four so the channel looks like one brand: deep navy-teal background, headline in yellow and white, red only for the one number. Font: heavy condensed sans (Impact / Anton / Bebas Neue style). Text in yellow `#FFD400`, white `#FFFFFF`, accent red `#E5252A`, 4-6 px dark outline.
- Layout: text block on the left 55%, Dr Rehan on the right 40%, one render between or behind. Squint test at 168x94 px: the number and the face must still read.
- Do NOT write "100% safe", "painless", "no risk", or a death/fear claim in any thumbnail.

## 3. Prompts

### 3.1 Home BP script - title "Your Home BP Reading Is Probably Wrong - 5 Mistakes That Add 10-30 Points"

Script check first: the script has four distinct mistakes (cuff size; smoking/caffeine/nicotine; rest 5 minutes with back supported; stress) and then repeats "relax" as "number five". It also says "check after meals", which contradicts the usual guidance (wait about 30 minutes after eating, caffeine or smoking). If the title says 5 and the thumbnail says 5, fix the script to five distinct points. "10-30 points" is not supported in the script; cut it from the title unless the script gives a source. Safer title: "Your Home BP Reading Is Probably Wrong - 5 Mistakes to Fix".

Background plate prompt (AI):
> Photoreal studio-style 16:9 image, 1280x720. Left two thirds: a modern upper-arm automatic blood pressure monitor on a wooden table, its screen large and sharp showing "160/100" in glowing red digits, the cuff wrapped on a forearm resting on the table, slightly too tight so the skin bulges at the cuff edge. Shallow depth of field, soft cool light from the left, deep navy-teal background fading to black on the right edge. Right third left empty and darker for a person to be composited in. No text, no logos, no extra objects, no clutter, no warning symbols, no medicines. Clean, high contrast, hospital-grade realism.

Text overlay (add yourself):
- Line 1, white: "HOME BP" (small)
- Line 2, yellow, huge: "WRONG?"
- Red number badge: "5" with "MISTAKES" under it (only if the script is fixed to 5)
- Doctor: Dr Rehan photo, right, slight smile, one hand pointing to the monitor.

Alternates (text only): "160/100... REAL?" / "STOP TRUSTING THIS NUMBER" / "5 BP MISTAKES".

### 3.2 Angiogram script 01 - title "Is a Coronary Angiogram Dangerous? Cardiologist Explains What Really Happens"

Background plate prompt (AI):
> Photoreal cinematic 16:9 image, 1280x720. A calm cardiac catheterization lab, soft blue light, a patient lying awake and relaxed on the table, a hand at the wrist with a small radial-artery access site and a thin catheter, a large monitor in the background showing a bright black-and-white coronary artery tree. Reassuring, not frightening: no blood, no pain expression, no sharp needle close-up. Left side darker and empty for text, right side left empty for a doctor to be composited. Navy-teal color grade, shallow depth of field. No text, no logos, no warning icons.

Text overlay:
- Yellow, huge: "DANGEROUS?"
- White, smaller, above: "CORONARY ANGIOGRAM"
- Red accent word at the bottom: "AWAKE" (the script says the patient is awake and under local anaesthesia).
- Do not add "3 MIN". The script claims 2-3 minutes; total procedure time in practice is usually longer than that. Use a number only if Dr Rehan confirms it for his own cath lab.

Alternates: "SCARED OF ANGIOGRAM?" / "ANGIOGRAM: THE TRUTH" / "WRIST. AWAKE. SAFE?" (question mark kept so it does not read as a guarantee).

### 3.3 Angiogram script 02 - title "Chest Pain on Exertion? This Is When You Need an Angiogram"

Background plate prompt (AI):
> Photoreal medical 3D render, 16:9, 1280x720. A glowing anatomical human heart, left half of frame, with the coronary arteries on its surface; one artery segment is visibly narrowed, highlighted by a thin yellow circle. A faint silhouette of a senior man in the background holding his chest while walking uphill, rendered soft and out of focus, no pain contortion, no blood. Navy-teal background, subtle light rays, very low clutter. Right third empty and darker for a doctor to be composited. No text, no warning symbols, no medicine.

Text overlay:
- White: "CHEST PAIN"
- Yellow, huge: "WHEN WALKING?"
- Red small tag: "ANGIOGRAM?"
- Keep the narrowed artery as a question; do not write the answer.

Alternates: "ANGINA? DO THIS NEXT" / "WHEN DO YOU NEED AN ANGIOGRAM?" / "CHEST PAIN ON EXERTION".

### 3.4 Angiogram script 03 (or merged 02+03) - title "What Happens in the Cath Lab? Coronary Angiogram Step by Step"

Advice on 02 vs 03: the two scripts overlap heavily (same intro, same angina paragraph). Merge into one video and use this thumbnail; keep 3.3 only if you still publish 02 separately.

Background plate prompt (AI):
> Photoreal 16:9 image, 1280x720, split composition. Left half: close-up of a patient's wrist with a radial-artery catheter site, clean and clinical. Right half: close-up of the groin/upper thigh with a femoral access site, clean and clinical, no blood. A thin white vertical divider in the middle with a small "OR" circle. Identical navy-teal lighting on both halves, shallow depth of field, a cath-lab monitor glowing faintly in the blurred background. No text, no logos, no warning icons, no patient face, no gore. Leave a darker band across the top 30 percent for headline text.

Text overlay:
- Yellow, huge, across the top: "WRIST OR GROIN?"
- White, small, bottom-left: "INSIDE THE CATH LAB"
- Dr Rehan: composited at bottom-right corner, smaller, because the split image is the hero here.

Alternates: "CATH LAB: STEP BY STEP" / "HOW IS AN ANGIOGRAM DONE?" / "RADIAL vs FEMORAL".

## 4. After generating

1. Check the 168x94 px squint test and the dark-mode and light-mode YouTube mockup.
2. Run a Trends and YouTube search check for each topic before you commit to a title/thumbnail pair (not done yet).
3. Keep notes on views, CTR and average view duration per thumbnail after upload, so the next set uses your own evidence instead of the pooled 149-thumbnail matrix.
