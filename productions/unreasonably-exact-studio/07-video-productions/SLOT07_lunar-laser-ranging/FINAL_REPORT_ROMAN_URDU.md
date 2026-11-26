# Slot 07: V2 Premium Editorial Revision, final report

**Mukhtasar:** V2 ban gaya hai, 1080×1920 resolution aur 96.000 s ka. V1 ko haath nahi lagaya gaya. Har maloom defect ya to theek hua hai ya uski wajah likh di gayi hai. Lekin V2 ko na kisi ne asal speed par dekha hai, na suna hai, na mute viewer test hua hai, aur owner approval bhi baqi hai.

## Files

- **Videos:** `renders/roughcut_v2/ROUGH_CUT_V2_PREMIUM.mp4` (bina captions) aur `ROUGH_CUT_V2_PREMIUM_CAPTIONS.mp4` (captions ke saath).
- **Captions:** `ROUGH_CUT_V2.srt`, `CAPTION_STYLE_COMPARISON.png` aur `CAPTION_STYLE_NOTES.md`.
- **Sound:** `SFX_LICENCE_MANIFEST.csv`, `SOUND_DESIGN_CUE_SHEET.csv` aur `renders/roughcut_v2/stems/`.
- **Audits:** `ON_SCREEN_TEXT_AUDIT.csv`, `AI_GENERATED_APPEARANCE_AUDIT.md` aur `SCIENTIFIC_COMPREHENSION_QA.md`.
- **QA aur report:** `V1_V2_IMPROVEMENT_REPORT.md`, `FINAL_PRODUCTION_QA.md` aur `qa/V2_TIMESTAMPED_CORRECTION_LIST.csv`.

## V1 se V2: kya badla

| Masla | V1 | V2 |
|---|---|---|
| Opening 3.5–7 s | sirf halki hawa | curiosity pad; "Not to light it up" par do girte notes; "question" par teen uthte notes; fire par tick aur glint. Is hisse mein bed V1 se ~12 dB zyada |
| Dome seam | shutter khulte waqt deewar par lakeer | asal wajah theek ki: blend ab sirf slit ke andar hota hai |
| B29 atmosphere | koi tasveer nahi | naya scene: "air" layer, jis mein asal pulse dheema hota hai jabke "no air" wala jora nahi hota, is liye "delay" aata hai. "atmosphere" ke baad tick wapas khisakta hai: "corrected". Koi number nahi, aur badge "SLOWDOWN HUGELY EXAGGERATED" |
| "A few photons" | histogram (lafz se match nahi) | teen dots ek ek karke roshan hote hain |
| P13 push | 45.2 s par pixel stair-steps, 44.8 s par zyada blur | offscreen layer ki resolution zoom ke saath badhti hai; blur kam; dissolve pehle |
| Astronaut se array cut | astronaut beech kaam mein ghayab | release poora hota hai, phir dissolve |
| Dots | phone par bohat chhote | 1.5–1.7× bade, final points par glow |
| Captions | card aur har lafz par sone ka dabba | Comic Neue Bold, poora phrase ek saath, koi card nahi, balanced lines, Earth ke station ke neeche |
| Badges | screen ke bilkul upar (phone UI ke neeche) | safe area mein; "SLOW-MOTION x1.1" ki jagah "SLIGHTLY SLOWED DOWN" |
| Look | photoreal aur vector scenes alag alag lagte the | poori film par ek grade, vignette aur halka grain; artwork nahi badla |
| Sound | 6 sounds, −21.8 LUFS | 23 original sounds, 115 cues, −17.4 LUFS, −1.9 dBTP; awaaz bed se 26 dB upar |

## Typography (xkcd What If)

- **Font ka saboot nahi mila.** What If? videos mein kaunsa font hai, iska koi pakka source nahi mila, is liye koi daawa nahi kar raha.
- **xkcd ka apna font istemal nahi ho sakta.** Uska licence CC BY-NC hai, jo commercial YouTube ke liye nahi chalta.
- **Comparison:** teen OFL fonts (Comic Neue, Patrick Hand, Kalam) teen scenes par compare kiye. Comic Neue Bold chuna, kyunke yeh phone par sab se saaf padha jata hai aur hand-lettered feel deta hai. Yeh xkcd font ki approximation hai, wahi font nahi.

## Sound aur licensing

- **Local SFX library:** iske 83 clips ka licence UNKNOWN hai, is liye inhein publication mix se bahar rakha. Private comparison mix nahi banaya.
- **Pixabay, Freesound, Mixkit:** inke licence check kiye. Koi file download nahi ki, kyunke zaroorat ki har awaaz original synthesis se ban gayi. Aage koi khaas file chahiye ho to file ka naam bata kar aap ki approval lunga.
- **Space mein awaaz:** space aur Moon par koi literal awaaz nahi, sirf illustrative musical accents. Har cue cue sheet mein "literal" ya "illustrative" likha hai.

## Jo abhi kamzor hai (V3 ke liye)

1. 38–39 s par imagined mirror ka dashed box generic hai.
2. 60–67 s par data plots ke charon taraf bohat khali jagah hai.
3. 88–96 s par aakhri orbit shot mein Earth aur Moon chhote hain.

## Verification: kya hua, kya nahi

**Hua:**
- 46 frames ke contact sheets aur close strips dekhe.
- Har frame ka frame-difference naapa: V1 ke 277 spikes ab 188 hain, aur max 30.1 se 25.8 hua.
- Splice ke kinare check kiye.
- ebur128 se loudness naapi.
- Code checks pass (P11 ke siwa, jo render ke baghair nahi chalta aur jiska code nahi badla).

Review ke dauran 4 nayi ghaltiyan mili aur theek ki gayin:
- G29 ke labels chhote the.
- "no air" label safed barf par chhup raha tha.
- Pulse ki trail finish line se aage chal rahi thi.
- 71 s par splice jump tha.

**Nahi hua:**
- Asal speed par poori film dekhna.
- Sunna (G1).
- Asli logon ke saath mute viewer test.
- Owner acceptance.

Main in mein se kisi ko done nahi likh raha.

## Aap ke liye agla qadam

1. Phone par captions wali file ek dafa awaaz ke saath aur ek dafa mute dekhein.
2. Headphones par pehle 16 seconds sunein.
3. Teen viewers ke saath mute test karein (protocol `SCIENTIFIC_COMPREHENSION_QA.md` mein hai).
4. Style ka faisla (D10) karein.
