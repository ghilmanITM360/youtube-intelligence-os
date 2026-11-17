# Dr. Rehan Video Kit: istemal ka tareeqa (step by step)

Ye kit Claude Code (Opus 5.5) ko batata hai ke poora kaam kaise karna hai: script, hooks, Dr. Rehan ka intro, image prompts aur editing. Aap ko sirf 4 jagah kaam karna hai. Claude har marhale ke baad **ruk kar aap se poochega**.

---

## Step 0: Folder tayyar karein (ek dafa, 10 minute)

Apne computer par ek naya folder banayein, maslan `rehan-project`, aur andar ye rakhein:

```
rehan-project/
  CLAUDE.md                ← is kit wali file (root par hi rakhein)
  kit/                     ← is kit ka "kit" folder (01 se 05 tak files)
  input/
    video/                 ← Dr. Rehan ki original video (MP4)
    script/                ← un ki script (docx/pdf)
    references/            ← aap ki style images, sound design notes, sounds
    knowledge/             ← zip (extract kar ke), Script Writing Engine.docx,
                             Topic Repackage.docx, Character Sheet PDF, links ki list
```

Zaroori software (Claude khud check karega, phir bhi): **Node 22+, Python 3.11+, ffmpeg, Chrome, Claude Code.**

---

## Step 1: Claude Code shuru karein

Terminal mein `rehan-project` folder ke andar:
```
claude
```
Model **Opus 5.5** chunein, aur ye pehla message bhejein:

> CLAUDE.md parho aur Phase 0 shuru karo. Pehle tools install aur check karo (kit/04_TOOLS_AND_SETUP.md), phir video, script, knowledge aur references sab analyze karo, aur Gate 0 par ruk kar mujh se poocho.

Claude khud `CLAUDE.md` parhta hai. Wahan poora plan likha hai.

---

## Step 2: Gate 0, direction chunein (aap ka kaam: 5 minute)

Claude 3 visual directions dikhayega aur kuch sawal poochega:
- kaun si look pasand hai (default: "Clinical Calm", minimal, safaid aur navy rang, sirf ek laal accent);
- captions Urdu script mein hon, Roman mein ya English mein;
- narrator ki awaaz kaisi ho (mard ya aurat, kaisa tone);
- vertical (9:16) shorts kitne aur kitne lambe;
- logo, channel ka naam, aur Dr. Rehan ka hospital ya city (sirf agar screen par dikhana ho).

Jawab de dein, Claude script likhna shuru kar dega.

---

## Step 3: Gate 1, script approve karein aur MP3 record karein (aap ka asal kaam)

Claude ye files dega (`work/01_script/` mein):
- `narration_script.md`: poori script. Dr. Rehan ke hisse ka khulasa, narrator ki har line, aur 3 hook options.
- `vo_lines.md`: **recording sheet**. Har line ka ID (H01, I01, B01…), Urdu, Roman, lehja aur andaza waqt.
- `edl.md`: kaun si line kahan aayegi.
- `title_thumbnail.md`: title, thumbnail aur SEO ke ideas (bonus).

Aap ko ye karna hai:
1. Script parhein, aur ⚠️ **DOCTOR CHECK** wali lines **Dr. Rehan se approve** karwayein. Ye medical video hai, is liye un ki manzoori zaroori hai.
2. Har line **alag MP3** mein record karein (ya TTS se banayein). File ka naam bilkul ID ke mutabiq hona chahiye: `H01.mp3`, `I01.mp3`, `B01.mp3`…
3. Sab MP3 `work/03_narration_audio/` mein rakhein.

Recording tips: ek hi mic, ek hi kamra, shuru aur aakhir mein aadha second khamoshi, ghalti ho to poori line dobara record karein.

---

## Step 4: Gate 2, images Codex se banwayein

Claude `work/02_assets/asset_prompts.md` dega, jis mein 20 se 100 tak prompts hongi. Codex ko ye file dein aur ye likhein:

> Is file ki instructions follow karo: har prompt se image banao, exact file name ke saath `generated/` folder mein save karo, aur aakhir mein `generated/_index.md` banao.

Bana hua `generated/` folder `work/02_assets/generated/` mein rakh dein, aur Claude ko batayein:

> MP3 aur images aa gayi hain. Gate 2 clear, Phase 3 editing shuru karo.

---

## Step 5: Gate 3, draft dekhein

Claude pehle ek **animatic** (kachha timeline) aur phir **draft videos** dega: 16:9 wali poori video aur 9:16 wale shorts. Wo 2–3 khaas sawal poochega. Seconds ke saath bata dein kya badalna hai (maslan "1:42 par text jaldi chala jata hai"). Ek fix round ke baad final files `work/05_delivery/` mein aa jayengi:
- `RehanExplainer_16x9.mp4` aur `RehanShort_01_9x16.mp4`…
- `.srt` captions, thumbnail ke liye frames, `CREDITS.md` (music, SFX aur fonts ke licence)

---

## Ahem baatein

- **Dr. Rehan ki baat nahi badli jayegi.** Narrator sirf aasaan karta aur jorta hai. Koi nayi medical baat apni taraf se nahi daalta.
- **Koi AI video nahi.** Sab motion keyframes, masks, typography, code se bane diagrams aur halki 3D se banta hai. AI images sirf kachhe maal ke taur par aati hain, aur un mein chehre saaf nahi hote.
- **Waqt aur kharcha:** ye bhaari kaam hai. Har phase mein kaafi tokens lagenge, aur render mein waqt lagta hai. Pehli video mein 2–4 ghante ka kaam samjhein, gates ke beech aap ke waqt ke ilawa.
- Kahin atak jayein to Claude se seedha Roman Urdu mein baat karein. Wo `CLAUDE.md` ke usoolon par hi chalega.

Kit mein kya kya hai:
| File | Kaam |
|---|---|
| `CLAUDE.md` | master plan: 5 phases, 4 gates, aur sakht usool |
| `kit/01_SCRIPT_AND_HOOKS.md` | hooks ka 4-hissa formula, line ki types, aasaan zubaan ke usool, retention |
| `kit/02_ASSET_PROMPTS_SPEC.md` | Codex ke liye image prompts ka format aur style lock |
| `kit/03_EDIT_SPEC.md` | editing ki poori hidayat: layouts, masks, motion, sound, 10/10 checklist |
| `kit/04_TOOLS_AND_SETUP.md` | repos ka audit (kya istemal hoga aur kyun), install commands |
| `kit/05_DR_REHAN_INTRO.md` | **Dr. Rehan ke intro, tayyar** (4 versions, Urdu + Roman), lower third, aur hook ki misaalein |
