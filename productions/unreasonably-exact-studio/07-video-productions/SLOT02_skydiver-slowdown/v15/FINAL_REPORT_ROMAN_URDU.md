# Skydiver Slowdown · V15 — Final Report (Roman Urdu)

## Status: OWNER_APPROVED_FINAL (25 Nov 2026)

Owner ne V15 ko final production master manzoor kar diya hai. V15 ab is film ka canonical master hai.

- **Publish ke liye:** sirf rights-clear audio master wala version istemal karein: `SKYDIVER_SLOWDOWN_FINAL_V15.mp4` ya `_CAPTIONS` wala. Library-review mix publish nahi hoga.
- **Dobara check kiya:**
  - 8 ki 8 checksums match.
  - Doosra isolated rebuild bhi byte-for-byte wohi bana: 8 files, 6 stems aur review mix sab.
  - Har project file ka SHA-256 `qa/FINAL_MANIFEST_SHA256.txt` mein hai.
- **V13 aur V14:** 25 Nov 18:22 ko Finder se macOS Trash mein bhej diye (2.1 GB). Trash khali nahi kiya. Wapas chahiye ho to Trash mein folder chun kar **Put Back** dabayein.
- **Trash ke baad:** V15 ke self-checks pass, checksums match, aur video 0 errors ke saath decode hui.
- **YouTube:** abhi upload nahi kiya. Alag hukam ka intezar hai.

## Khulasa

V15 ban gaya hai aur `v15/` folder mein mukammal, self-contained hai.

- **Files:** `SKYDIVER_SLOWDOWN_FINAL_V15.mp4` (clean) aur `SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4` (captions ke saath)
- **Format:** 1080×1920, 24 fps, 110.04 second, 2,641 frames, −16 LUFS
- **Checks:** har automatic check pass hua. Poori film browser mein normal speed par shuru se aakhir tak chali: 0 dropped frames, 0 stall.

**Aik baat saaf saaf:** main awaaz sun nahi sakta. Audio ke baare mein jo kuch likha hai woh **measurement** hai, sunne ka faisla nahi. Aap headphones aur phone speaker dono par aik dafa sun lein. Yahi aakhri acceptance step hai.

## Sab se bara masla: background awaaz (aap ki shikayat)

**V14 mein kya ghalat tha:**
- Hawa ka bed bohat ooncha tha.
- Hamza ki awaaz ke neeche sirf 7 dB ducking thi.
- Hawa consonants wali frequency (1–4 kHz) par bhi chhai hui thi.

**V15 mein kya kiya:**
- Hawa ka bed ~10 dB neeche.
- Bolte waqt hawa 12 dB aur effects 9 dB aur neeche jaate hain.
- Bolte waqt background ki 1–4.5 kHz band alag se 6 dB aur kaati jaati hai, taake alfaaz ke aakhri hisse saaf rahein.
- Hamza ki awaaz par sirf halki levelling (2:1). Unki natural awaaz waisi hi hai.
- "Ding" jaisi awaazein 11 se kam kar ke 5. Ab har arrow par awaaz nahi aati.

**Natija (jab Hamza bol rahe hon):**

| | V14 | V15 |
|---|---|---|
| Awaaz aur background ka farq (median) | 10.5 dB | **20.7 dB** |
| Kamzor tareen 10 % lamhon mein farq | 5.2 dB | **17.1 dB** |
| Speech band mein farq (median) | 14.1 dB | **24.8 dB** |

Poori film ki loudness pehle bhi −16 LUFS thi aur ab bhi hai. Isi liye sirf LUFS ko saboot nahi maana; asal farq upar wale numbers mein hai.

**SFX Library:** library ki README khud kehti hai ke licence tay nahi hua. Is liye publication master mein koi library clip nahi; master ki har awaaz code se generate hui hai (rights-clear). Chaar library clips ke saath alag review mix bhi banaya hai, sirf muqable ke liye: `qa/review/review_library_mix.mp4`. Tafseel `SFX_LICENCE_MANIFEST.csv` mein hai.

## Captions

- **126 pixel ooper kiye.** Caption box ab neeche ke kinare se 294 px door hai.
- **Do barabar lines,** har line 27 huroof tak.
- **65 second wala overlap khatam.** Bars par zoom hi hata diya.
- **Aik khatarnaak split theek kiya:** pehle "you have stopped falling." akela screen par aa sakta tha, jo baat ka ulta matlab deta hai. Ab poora jumla aik saath aata hai.
- **Automatic check:** har caption ke start, middle aur end par dekha ke neeche koi arrow, bar ya graph to nahi. 46 cues, 138 samples, **0 takraao**.

## Character animation

V14 mein skydiver aik jami hui tasveer thi.

V15 mein **mesh deformation** hai: aik hi tasveer ko narmi se moda jata hai, kaata nahi jata. Is liye joint mein disc, darar ya alag hota haath-joota mumkin hi nahi.

- **Ghutne aur joote:** dono taangein alag alag, apne ghutne ke gird halka harkat karti hain.
- **Kalaiyan:** dono haath hawa mein halka trim karte hain.
- **Kapre:** pant, aasteen aur shirt mein lehrein. Inki taqat model ke **drag/weight** se chalti hai: aaram ki halat mein 0, raftaar aur ghani hawa ke saath barhti hai.
- **Parachute pack:** bilkul sakht aur juda hua. Test kiya: zyada se zyada load par 0.35 px se kam hilta hai.

**Hadein:** ungliyan alag alag nahi hiltin aur chehre ke naye expressions nahi hain, kyun ke Codex art mein yeh hisse alag nahi bane. Peeche se dikhne wale shots par mesh nahi lagaya.

## Science ki wazahat

| Rang | Matlab |
|---|---|
| Garam narangi | Wazan (neeche) |
| Teal | Drag (ooper) |
| Neela dashed | Raftaar |
| Violet | Net force |

Har rang ka aik hi matlab hai; raftaar kabhi force jaisi nahi dikhti.

**Net force:**
- Bars ke ooper ek **×8 lens** khulta hai. Is mein wazan ki line ke ooper drag ka zaid hissa violet hai.
- Jism par bhi **violet "net force ×8" arrow** hai.
- Dono par ×8 likha hai. Asal scale par yeh farq sirf 1–4 % hai, is liye bara dikhana zaroori tha, aur bata bhi diya.

**Hawa ka kirdaar:**
- Oonchai par hawa ke nishan kam aur neeche zyada. Ginti model ki density se.
- Raftaar barhne ke saath airflow ki lakeerein banti hain, aur wohi load drag arrow banata hai.
- Ghani hawa wale muqable mein, aik hi raftaar par, ghani hawa wala skydiver zyada lehrata hai.

**Raftaar ka kam hona:** har 10 second ka nishan, aik hi scale par. Faasle pehle barhte hain, phir chhote hote hain, magar har nishan neeche hi hai. Yani skydiver ab bhi neeche ja raha hai.

**Bina awaaz ke check:** captions aur awaaz ke baghair contact sheet dekhi. Kahani tasveer se samajh aati hai.

## Mahol aur parallax

- Sarkon ke saath farmhouse aur gaon.
- Darakhton ke saaye wale tops. Zameen qareeb aane par jhund alag alag darakhton mein badal jaate hain.
- Skydiver ke saamne halke hawa ke zarre (foreground depth).
- Opening mein jahaz ki Codex tasveer ke neeche aik alag tukra tair raha tha (V14 mein bhi tha). Sirf woh tukra hataya gaya.

## Saboot (files)

| Kya | Kahan |
|---|---|
| Defect audit (19 masail: waqt, wajah, hal, saboot) | `FINAL_PRODUCTION_QA.md` |
| Audio numbers | `AUDIO_MIX_QA.md`, `qa/audio_qa.json` |
| Science | `SCIENTIFIC_VISUAL_QA.md` |
| Character | `CHARACTER_ANIMATION_QA.md`, `qa/rig_v15/warp_states.png` |
| Har cut aur ahem lamhe ke 6 lagatar frames | `qa/frames_critical/` (35 strips) |
| Caption check | `qa/caption_qa.csv` |
| Decode, freeze aur sync | `qa/decode_check.txt` (0 errors, 0 freeze), A/V farq 3 ms, sync map 34/34 |
| Research aur tools ka jaiza | `research/V15_RESEARCH_NOTES.md` |

## Rebuild aur V13/V14

- **Rebuild:** `zsh tools/build_v15.sh` se poori film ~3 minute mein dobara banti hai.
- **Isolated rebuild:** V15 ki copy aisi jagah chalayi jahan V13, V14 aur SFX Library maujood hi nahi the. 8 ki 8 files **byte-for-byte** wohi bani.
- **Hamza ki recordings:** asli aur saaf, dono mehfooz aur V14 jaisi hi (SHA-256 match).

**V13 (1.0 GB) aur V14 (1.1 GB) approval ke baad Trash mein bhej diye gaye.** Trash khali nahi kiya; Finder ke "Put Back" se wapas aa sakte hain.

## Aap ke karne ka kaam

Review page kholne ke liye `unreasonably-exact/` se yeh chalayein, phir http://127.0.0.1:8615/qa/review/ kholein:

```bash
python3 -m http.server 8615 --bind 127.0.0.1 --directory skydiver-slowdown/v15
```

1. Headphones par aik dafa sunein: har lafz saaf hona chahiye.
2. Phone speaker par "Low volume (20%)" button ke saath sunein.
3. "Library-SFX mix" se muqabla karein (agar pasand aaye aur licence mil jaye to master badla ja sakta hai).
4. (Ho gaya: owner ne manzoor kiya, V13/V14 Trash mein.)

Kuch upload ya publish nahi hua.
