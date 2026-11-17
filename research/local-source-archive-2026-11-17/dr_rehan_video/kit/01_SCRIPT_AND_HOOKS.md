# 01: Script & Hooks (the narrator layer)

Goal: turn Dr. Rehan's technical recording into a story anyone can follow, **using only narrator lines placed around and between his segments**. His words stay. The narrator is the viewer's friend who says "ruko, isko aasaan karte hain" and then hands back to the expert.

This file condenses the user's knowledge files (Script Writing Engine stages 1–7, Topic Repackage, Hook guide, BUT/THEREFORE, Viral Checklist, Intro/Script Analyzer prompts) into one working method.

---

## 1. The narrator line types

| Code | Type | Where | Length | Job |
|---|---|---|---|---|
| **H** | Cold-open hook | 0:00 | 10–20 s | Stop the scroll and make the viewer think "ye video mujhe dekhni chahiye" within 15 s |
| **I** | Dr. Rehan introduction | right after H | 6–15 s | Who he is, in plain words, and why to trust him (see `05_DR_REHAN_INTRO.md`) |
| **B** | Bridge | before each doctor segment | 4–10 s | Ask the question his next segment answers ("Ab sawal ye hai…") |
| **J** | Jargon buster | right after he uses a hard term | 3–8 s | Explain one term with one everyday comparison |
| **R** | Re-hook | about every 60–90 s, before a likely drop-off | 4–8 s | Re-open curiosity and tease what's coming ("lekin asal hairani ki baat abhi baqi hai…") |
| **M** | Mini-recap | after a dense chapter | 5–10 s | "To ab tak humne 2 baatein samjhein: …" |
| **O** | Outro | end | 15–30 s | The one takeaway, when to see a doctor, a soft CTA, and a short medical disclaimer |

Name each line `H01, I01, B01, J01, R01, M01, O01…` in timeline order. The file name of the recording = the ID (`B03.mp3`).

**Density rule:** narrator time should be roughly **15–25% of total runtime**. Never put two narrator lines back-to-back for more than ~20 s; the doctor is the star.

---

## 2. The hook formula (every H and every R uses it)

The user's 4 requirements, merged with the Hook guide's 3-step formula:

| Step | User's requirement | Hook-guide name | What it sounds like |
|---|---|---|---|
| 1 | **Real-life situation** the viewer recognises | Context Lean | "Aap sirhiyan chadhte hain, saans phool jati hai, aur aap sochte hain umar ka asar hai." |
| 2 | **A genuine contradiction** | Scroll-Stop Interjection ("lekin…") | "**Lekin** kabhi kabhi ye umar nahi, dil ka ishara hota hai." |
| 3 | **A reason to keep watching** | Contrarian Snapback + promise | "Aur sab se khatarnak baat ye hai ke sugar ke mareezon ko aksar dard mehsoos hi nahi hota." |
| 4 | **Natural handover** to Dr. Rehan | (bridge) | "Ye kyun hota hai, ye samjhate hain Dr. Rehan Omer…" |

Hook rules:
- The first spoken words must be **concrete**: a person, an action, a place, a body feeling. No "Aaj hum baat karenge…", no "Assalam-o-Alaikum doston" as the opening line.
- **Show it in 3–5 on-screen words** at the same time (e.g. `SAANS PHOOLNA = UMAR?`).
- **Staccato** delivery for the snapback: short sentences, one idea each.
- The contradiction must be **true and supported by the doctor's own content**. No fear-mongering, no "doctor aap se ye chhupate hain".
- **Payoff fidelity:** whatever the hook promises must be delivered in his recording, ideally within the first third.
- Write **3 alternative cold-open hooks** with different angles (pick the angles from the Script Engine's psychology list: contradiction, hidden cost, unexpected consequence, power vs vulnerability, cause and effect, human behaviour). Mark your recommendation and say why.

---

## 3. Making it easy (simplification rules)

Test every narrator line against two listeners: a **10-year-old** and a **70-year-old dadi/nana**. Both must understand it on first hearing.

1. **One idea per sentence**, mostly 6–12 words. Spoken Urdu, not textbook Urdu: "dil", "naaliyan", "khoon", "sugar", not "qalb", "sharyanein", "ziabetus" (unless followed by the simple word).
2. **Every hard term gets one everyday picture**, then one simple sentence. Use these as a starting bank, and always check the doctor's meaning first:
   - artery blockage → "paani ke pipe mein jamne wala kachra"
   - heart → "ek pump jo din raat chalta hai"
   - stent → "naali ko khula rakhne wala chhota sa jaal / spring"
   - angioplasty → "bina bade operation ke, baazu ya taang ki naas se naali kholna"
   - insulin → "chaabi jo sugar ko khoon se nikal kar jism ke cells mein pohnchati hai"
   - insulin resistance → "taala zang kha gaya, chaabi kaam nahi kar rahi"
   - HbA1c → "pichle 3 mahine ki sugar ki report card"
3. **Numbers must mean something.** Turn "20%" into "har 5 mein se 1". Use only numbers the doctor said, or mark `⚠️ DOCTOR CHECK`.
4. **BUT / THEREFORE, never AND THEN.** Every narrator line connects the segments with "lekin…" (tension) or "is liye / to phir…" (consequence). Flag and rewrite any "aur phir…" chains.
5. **Speak to one person**: "aap", "aapke abba", "aapki ammi". Relatable family situations work best for this audience.
6. **No AI clichés.** Ban list (from the Script Audit engine): "kya aap jaante hain…?" as an opener, "chaliye shuru karte hain", "ye safar…", "hairat-angez", "sab kuch badal gaya", "aage jo hua…", "little did he know", "a testament to", "everything was about to change". Avoid fake suspense.
7. **Tone:** warm, calm, confident. Like a good older cousin who happens to know a doctor. Never preachy or scary.

---

## 4. Retention plan (from Script Engine stages 3–5)

Before writing lines, make `01_script/retention_map.md`:
- **Central argument** of the whole video in one sentence, and the **viewer promise** (what they will know by the end).
- **Act structure** (usually 3–5 acts) mapped onto the doctor's chapters, with the main question each act answers.
- **Open loops**: list every question opened (hook, re-hooks) and the exact timecode where it closes. Never leave a loop unclosed. Don't hold more than 2 open at once.
- **Drop-off points** from Phase 0. Each gets a J, R, M or a visual change.
- **Pace map**: alternate dense and light moments, with one breath (a pause or held visual) before the most important medical point.
- Narration speed: Urdu narration ~130–150 words/min. Estimate seconds for every line.

---

## 5. Output files (Phase 1)

### `01_script/narration_script.md` (for the user and Dr. Rehan to approve)
Write it in timeline order, like this:

```
[H01] COLD OPEN (recommended version A)        ~14 s
Urdu:   …
Roman:  …
On screen: "3–5 WORDS"
Visual idea: …
Why it works: situation → contradiction → reason → handover

[I01] DR. REHAN INTRO                           ~9 s
…

[DR 00:00.0 → 00:47.3] Dr. Rehan: (1-line plain summary of what he says)
   trims: 00:12.4–00:13.9 cough removed

[J01] after "angioplasty" at DR 00:31.2           ~5 s
…
```
Put alternatives (hook B and C) at the end in an "Options" section. Mark every `⚠️ DOCTOR CHECK` clearly.

### `01_script/vo_lines.md` (the recording sheet)
A table with columns `ID | Urdu script (with harakat where pronunciation is tricky) | Roman Urdu | Delivery note (tone, pace, emphasis word in CAPS) | Target sec | File`.
Add recording tips at the top: same mic, same room, 44.1/48 kHz, 0.5 s silence at start and end, one file per ID, re-record the whole line rather than patching.

### `01_script/edl.md` (edit decision list)
`# | Source (N-ID or DR) | In | Out | Duration | Notes (trim, overlap, J/L-cut)`. Total runtime estimate at the bottom.

### `01_script/title_thumbnail.md` (bonus)
Use Topic Repackage + the Title Analyzer: 10 title options from different psychological angles (not word swaps), 3 thumbnail concepts (3–4 words max, one strong visual, Dr. Rehan's expression frame suggestion), and SEO description, chapters and tags following the Video SEO checklist.

---

## 6. Self-audit before GATE 1

Run the Script Quality Audit (Script Writing Engine, prompt 7) on your narrator lines and write the scores at the top of `narration_script.md`:
- Naturalness, Clarity, Rhythm, Voice consistency, Voiceover readiness (each /10). **Rewrite anything under 8.**
- 10-year-old test / 70-year-old test: pass or fail per line.
- Every hook has all 4 parts? Every loop closed? Any new medical claim? (Must be zero, or marked.)
