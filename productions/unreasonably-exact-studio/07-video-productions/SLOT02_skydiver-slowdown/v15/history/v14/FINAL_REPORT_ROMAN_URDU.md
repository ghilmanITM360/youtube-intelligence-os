# V14: Hamza ki awaaz ke saath (Final Report, Roman Urdu)

## Mukhtasar nateeja

V14 ban gayi hai:
- `SKYDIVER_SLOWDOWN_V14_HUMAN_VOICE.mp4`: saaf version
- `SKYDIVER_SLOWDOWN_V14_CAPTIONS.mp4`: captions wala version
- `SKYDIVER_SLOWDOWN_V14.srt`: subtitle file

Video 110.04 s ki hai, 1080×1920. Ab is mein sirf Hamza ki awaaz hai.

**Main ne film ko player mein chala kar dekha ya suna nahi**: Chrome extension connect nahi tha, aur main audio sun nahi sakta. Baraye meharbani aik dafa headphones ke saath khud dekh lein. V13 bilkul waisi hi hai (6/6 hash OK).

## 1. Hamza ki recording

- **Script ka aaghaz:** asal file mein script **10.24 s** par shuru hoti hai.
  - 0–8 s mein setup ki baat thi ("I will do a video recording here… Start the video"). Yeh nikal di.
  - Main ne andaze se 9 s nahi kaate. Yeh jagah transcription aur waveform se pakki ki.
- **False start ya dohri take:** koi nahi mili. Hamza ne script aik hi dafa, tarteeb se parhi hai.
- **Lambe waqfe:** jo waqfe 1.5 s se lambe the (8 jagah), unhein 1.5 s kar diya. Kul 3.56 s ki khamoshi nikli.
  - Is ke ilawa har saans, waqfa aur andaaz wahi hai.
  - Raftaar, pitch aur koi lafz nahi badla. AI awaaz bilkul nahi.
- **Processing:** halka high-pass, halka de-esser, naram compression, aur aawaz −18.5 LUFS tak barhai.
  - Noise reduction ki zaroorat nahi thi, kyunke waqfon mein bilkul khamoshi (digital silence) hai.
- **Saaf narration:** 108.70 s (`HAMZA_VOICEOVER_CLEAN.wav`). Asal file `HAMZA_VOICEOVER_RAW.mp3` mehfooz hai.

## 2. Transcript aur script mein farq

Captions wohi likhti hain jo Hamza ne bola. Do alag Whisper decode ne har lafz par ittefaq kiya. Script se yeh farq hain:

| Script | Hamza ne kaha |
|---|---|
| so **your** downward **speed starts** | so **the** downward **speeds start** |
| you**'ve** stopped | you **have** stopped |
| And your parachute? Still closed. | And your parachute **is** still closed. |
| the **result** can change | the **results** can change |

"speeds start" aur "speed starts" ki awaaz taqreeban aik jaisi hai, **is liye sun kar tasdeeq kar lein**. Baqi script poori hai; koi lafz kata ya chhoota nahi.

## 3. Animation awaaz ke mutabiq

- **Timing ka tareeqa:**
  - V13 ki har cheez (shot, camera, teer, graph) ab Hamza ke usi lafz par aati hai jis par woh bani thi.
  - Is ke liye Hamza ke har phrase ko V13 ke usi phrase se milaya. Yeh aik global speed nahi hai; har phrase ki apni raftaar hai (0.26× se 1.4×).
  - Jahan Hamza aahista bolta hai, wahan bhi jism ka halka hilna, hawa ki lakeerein aur badal asal raftaar par chalte rehte hain, is liye koi scene jama hua nahi lagta (0 frozen frames).
- **Brief ki table ki 33 lines check kin** (`NARRATION_VISUAL_SYNC_MAP.csv`). Koi cheez lafz se pehle nahi aati.
- **Kuch cheezein jo pehle aa rahi thin, theek kin:**
  - "starts at rest" ab "starting from rest" par aata hai (pehle 1.9 s pehle aata tha).
  - Speed ×2 wala hissa ab "the faster you fall" par shuru hota hai.
  - Drag ka bar weight ki lakeer se **"stronger"** lafz par aage nikalta hai.
  - "Think about that" ke dauraan camera net force par ruka rehta hai.
- **Naye chhote beats:**
  - "this is a model" par MODEL frame ke andar speed ka graph aata hai, aur "change the posture or the conditions" par doosre nataij ki lakeerein banti hain.
  - "body position stays fixed" par "posture: fixed" likha aata hai.
- **Opening wahi V13 wali hai:** jahaz upar beech mein, girta hua insaan us ke neeche, koi bara badal screen nahi dhakta. Pehla lafz 0.40 s par aata hai.
- **Physics model bilkul nahi badla.** Har frame par altitude, hawa ki ghanapan, raftaar, drag, net force, needle aur zameen aik hi model se aate hain. Self-check pass hai.

## 4. Captions

- 47 chhote captions, har aik 40 huroof se kam aur zyada se zyada do lines.
- **0 overlap.** Har caption apne lafz se 0.05 s pehle aata hai aur 0.25 s baad jaata hai.
- Captions neeche hain aur character, ghari ya teeron ko nahi dhakte.
- Sirf aik caption ("Slowing down doesn't mean") 0.66 s ke liye hai, kyunke Hamza is hisse ko tez bolta hai.

## 5. Awaaz (sound design)

- **Naya mix:** sound design naye sire se banaya. Har effect usi frame par hai jahan us ka kaam screen par hota hai (`SOUND_DESIGN_CUE_SHEET.csv`, 35 cues). Masalan:
  - ghari par cut hone par tick
  - needle girne par halki ticks
  - har diagram ke aane par naram tone
  - camera ke tilt aur pull-back par whoosh
  - "brakes" par hawa ka jhonka
  - model reset se pehle uthti awaaz
- **Sab effects is project mein khud banaye gaye hain** (noise aur sine se). Koi library clip istemal nahi hua, is liye **poora mix rights-clear hai**. V13 wala SFX licence ka masla V14 mein nahi hai.
- **Hamza ki awaaz sab se oopar hai.** Hawa ki awaaz −27 LUFS par hai, aur bolte waqt hawa aur effects khud dheeme ho jaate hain.
- **Final level:** −16 LUFS, peak −1.5 dB.

## 6. Kya check kiya

- **Files:** dono MP4 mein 2641 frames hain, 0 decode errors, 0 frozen hisse. Audio aur video dono 110.04 s par saath khatam hote hain. Awaaz aur tasveer mein sirf 3 ms ka farq hai.
- **Frames:** 12 ahem lamhon par lagataar frames, captions ke saath (`qa/consecutive_frames_critical.png`), aur poori film ke stills.
- **Real-time decode:** ffmpeg se dono files normal raftaar par decode kin.
- **V14 khud-mukhtar hai:**
  - alag folder mein dobara banane par narration, captions, word timings aur mix bilkul wohi bane
  - koi path V14 se bahar nahi jaata

## Aap ke karne ke kaam

1. Dono videos **QuickTime ya Chrome mein headphones ke saath** dekhein. Main ne inhein dekha ya suna nahi.
2. "the downward speeds start" wala hissa sun kar caption ki tasdeeq karein.
3. Effects ka level aur hawa ki awaaz pasand aaye ya nahi, bata dein.
4. Art aur rig ab bhi V13 wale "candidate" hain; un ki approval aap ki taraf se baqi hai.

Kuch upload ya publish nahi hua.
