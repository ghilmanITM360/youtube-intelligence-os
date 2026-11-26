# V13: Final Report (Roman Urdu)

## Mukhtasar nateeja

V13 ban gayi hai:
- `SKYDIVER_SLOWDOWN_V13.mp4`: saaf version
- `SKYDIVER_SLOWDOWN_V13_captions.mp4`: captions wala version
- `SKYDIVER_SLOWDOWN_V13.srt`: subtitle file

Video 78.2 s ki hai, 1080×1920, aur narration aap ki wohi recording hai.

**Yeh abhi review cut hai, publish ke liye tayyar nahi.**

## 1. Opening theek ki (sab se pehli tarjeeh)

Aap ke 0:00 / 0:01 / 0:03 wale screenshots mein V12 ke yeh masle the:
- jahaz aur insaan bohat chhote the
- dono neeche daayein kone mein the
- zameen zyada jagah le rahi thi
- 0:03 par ek bara badal poori screen dhak raha tha

Maine V10, V11, V12 aur V13 ki opening ek hi sheet par rakh kar dekhi (`qa/OPENING_V10_V11_V12_V13.png`). Sab se achhi composition V11 ki thi, is liye wohi wapas laya aur us mein asal parallax shamil kiya:
- **A. Establish (0–1.2 s):** jahaz upar beech mein, girta hua insaan us ke neeche, saaf aasman par. Ufaq (horizon) neeche hai aur us par halki dhund hai.
- **B. Follow (1.1–2.4 s):** camera girte hue insaan ke saath neeche jhukta hai. Jahaz jaan boojh kar upar se frame se nikalta hai.
- **C. Approach (2.2–3.3 s):** camera insaan ki taraf barhta hai. Door ki pahariyan, khet, darmiyani badal aur insaan, sab alag raftaar se hilte hain.
- **D. Reveal (3.3–5.2 s):** seedha cut peeche se: band parachute, ek ring aur "parachute: closed".

Badal ka wipe bilkul khatam kar diya.

Mawazna: `qa/before_after/V12_vs_V13_*.png` aur `OPENING_V10_V11_V12_V13_COMPARISON.md`.

## 2. Science aasaan ki

- **Hawa ki mukhalfat (16.8–20.9 s):**
  - Pehle aap saakin hawa ke beech se neeche jaate hain ("you: down", "still air").
  - Phir camera aap ko pakar leta hai, aur wohi hawa aap ke gird upar ki taraf behti nazar aati hai ("air, relative to you").
  - Uske baad drag ka teer upar ki taraf banta hai ("drag: the air pushes back").

  Hawa nuqton se dikhai gayi hai aur force teer se; dono ka style alag hai.
- **Patli aur ghani hawa (28.6–31.4 s):**
  - Do barabar dabbe hain: upar patli hawa, neeche ghani hawa. Nuqte model ki density ke mutabiq hain, takreeban 2.8 guna.
  - Phir dono ke neeche **ek hi raftaar** par ek hi jism hai, aur ghani hawa mein drag ka teer lamba hai.

  Is screen par aur kuch nahi hai.
- **Sirf raftaar ka asar (33.7–38.7 s):** "same air · same posture" wala dabba saamne hai, aur raftaar ×2 hone par drag ×4 hota hai.
- **Forces (38.7–46.6 s):**
  - ×30 lens hata diya, kyunke pehli baar dekhne wale ke liye mushkil tha.
  - Ab pehle teer barabar hote hain aur "balanced: still falling" aata hai (raftaar ka teer wohi rehta hai).
  - Phir weight aur drag ke bars ek hi base se, ek hi scale par saath saath dikhte hain. Drag ka bar weight ki lakeer se aage nikalta hai aur wo hissa violet ho jaata hai ("net force: up").
  - Camera bars ke upar ki taraf qareeb jaata hai. Dono bars ek saath barhte hain, is liye farq ko bara chara kar nahi dikhaya; yeh model ka asal farq hai (takreeban 3%).
- **Neeche jaate hue dheema hona:** "still moving down", aur har 10 s par ek nishaan wali lakeer (faasle pehle barhte hain, phir ghatte hain, har nishaan pichhle se neeche). Needle girti hai.

Physics model bilkul nahi badla (V12 wali file byte-identical hai). Saare checks pass hain.

## 3. Codex V13 ka saman

- **Bare hands (back pose):** maine dekh kar check kiya. Sirf haath, cuff aur munh ke hisse badle hain. Istemal kiye. Ab peeche wale pose mein bhi dastanay nahi, side pose jaisa.
- **Three-quarter bare hands:** check kiye aur asset mein daale, magar V13 mein three-quarter pose screen par nahi aata.
- **Kohni ke folds (10/15/22°):** 2× crop mein notch aur double lakeerein theen, is liye **rad kiye**. V12 wala tareeqa rakha.
- **Gardan/collar:** ±4° par seams theen, is liye **rad kiye**. Sar ±1° tak hi hai.

Tafseel: `CODEX_V13_INTEGRATION_MANIFEST.csv`. Sab art ab bhi "candidate" hai.

## 4. Captions

V12 mein yeh masle the:
- caption 4 aur 5 aapas mein 0.25 s overlap kar rahe the
- ek caption 131 huroof ka tha

Ab Whisper (whisper.cpp, small.en model) se har lafz ka waqt nikala aur awaaz ke asal shuru aur khatam par set kiya:
- **48 chhote captions**, har ek 40 huroof se kam
- **0 overlap**

Narration ka ek lafz bhi nahi badla. ("breaks" ko script ke mutabiq "brakes" likha.)

Tafseel: `CAPTION_SYNC_QA.md`.

## 5. Awaaz

- Hawa ki awaaz ab girne ke saath chalti hai, graphics ke saath achanak kam nahi hoti. Sirf "starting from rest" par jaan boojh kar khamoshi aati hai.
- Naye cues: hawa ke ulat jaane par, drag ke teer par, ghani hawa par, bars aur net force par.
- Rights-clear mix maujood hai.

**Main audio sun nahi sakta; kisi insaan ko headphones par sunna hoga.**

## Kya check kiya

- **Files:** 1877 frames, decode mein 0 errors, 0 freeze. Awaaz −16.4 LUFS, peak −1.1 dBFS.
- **Real-time rate:** file real-time raftaar par 78 s mein bina error ke decode hui.
- **Frames:** lagataar frames (opening ka cut, hawa ka ulatna, forces ka barabar hona), proofs A–F ki strips, aur 75 storyboard panels.
- **Phone size:** check kiya.

**Chrome mein real-time playback nahi ho saka.** Claude in Chrome extension connect nahi tha, aur andar wala browser local file nahi khol sakta. Is liye maine film player mein chala kar nahi dekhi. Baraye meharbani aap khud dekh lein.

## Publish se pehle baqi

- Art aur rig ki approval
- Kohni ka chhota notch (~0.3 s) aur dissolve ki halki double outline
- Opening se peeche wale shot par zameen ka style badalta hai
- Hawa wale shot mein nuqte zyada hain
- Headphones par sunna
- 18 library SFX ka licence clear nahi
- Narration ka aakhri faisla aap ka hai

V1–V12 mehfooz hain. Kuch upload ya publish nahi hua.
