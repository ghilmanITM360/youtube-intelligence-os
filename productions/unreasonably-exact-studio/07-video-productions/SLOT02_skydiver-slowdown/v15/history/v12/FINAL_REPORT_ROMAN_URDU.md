# V12 — Final Report (Roman Urdu)

## Mukhtasar nateeja

V12 ban gayi hai, aur yeh V11 ka motion-design re-edit hai:
- `SKYDIVER_SLOWDOWN_V12.mp4`: saaf version, screen par captions nahi.
- `SKYDIVER_SLOWDOWN_V12_captions.mp4`: captions wala version.
- `SKYDIVER_SLOWDOWN_V12.srt`: alag subtitle file.

Video 78.2 s ki hai, 1080×1920, aur narration aap ki asal recording hai.

**Yeh ab bhi review cut hai, publish ke liye tayyar nahi.**

## Kya badla (aap ke V11 screenshots ke mutabiq)

1. **Text bohat kam kiya:**
   - har shot par "UNREASONABLY EXACT" khatam
   - bara MODEL banner khatam (ab sirf chhota "MODEL" tab)
   - "SPEED (your wrist)" wala floating dial khatam
   - "CLOSE-UP OF THE ARROW TIPS" jaise headers aur footnotes khatam
   - captions ab alag export aur SRT mein hain

   V11 ke 39 text items ki list aur faisla `TEXT_REDUCTION_AUDIT.csv` mein hai.
2. **Opening (2.5D):** camera door se aeroplane ke neeche chhoti si figure ki taraf barhta hai. Ek qareeb ka badal lens ke saamne se guzarta hai, phir hum faller ke peeche hote hain, pack band hai, aur "10 km down" ki lakeer zameen tak jaati hai.
3. **Character ki harkat:** Codex V12 ke parts se naya rig banaya:
   - Bazu uthta hai aur nazar kalai par jaati hai (0:08 aur 0:54).
   - "Wait, what?" par sar jhatke se upar aata hai, palak jhapakti hai aur bazu wapas jaata hai.
   - Baqi shots mein halki nod aur blink hai.
4. **Hawa ka bahao:** "air, relative to you". Lakeerein jism ke gird ek ek kar ke banti hain, un par chalte nishaan hain, aur lakeerein jism ke peeche (aur kinaron par aage) se guzarti hain. "Schematic" likha hai, yeh simulation nahi.
5. **Forces:** ek hi scale par weight aur drag. Bara white card hata diya, ab scene ke andar ek **×30 lens** hai. Lens mein drag ki nok model ke mutabiq weight ki lakeer se upar nikalti hai, aur tab violet "net force" teer aata hai.
6. **Equal-time positions:** do columns (4 s aur 15 s) ki jagah ab **ek hi neeche jaati lakeer** hai: har 10 s par ek nishaan, sab ek hi scale par. Faasle pehle barhte hain, phir ghatte hain, aur har nishaan pichhle se neeche hai.
7. **Hawa ki ghanatwa (density):** altitude ruler par "air sample" lens hain, neeche zyada nuqte. **Speed ×2 → drag ×4:** ek hi jism par jude hue teer.
8. **Graph:** white card nahi. Axes bante hain, curve zero se uthta hai, "top speed" aata hai, phir girta hai magar zero tak nahi ("not zero"). Doosre curves sirf tab aate hain jab narration "conditions" kehta hai.
9. **Speedometer:** sirf kalai par dikhta hai (0:10, 0:55, 0:57), har jagah corner mein nahi.
10. **Awaaz:**
    - V11 ka sound design naye cuts par retime kiya.
    - Bazu uthne par kapre ki sarsarahat.
    - Lens, trail aur graph ke neeche hawa kam hoti hai.

    Rights-clear mix bhi maujood hai.

## Codex V12 package

Codex ne khud likha tha ke motion tests fail hain aur pivots maloom nahi. Is liye maine us partition ko azaadana ghumaya nahi:
- **Rest:** parts jod kar master jaisa nikla (fark 8/255).
- **Kohni:** pehla pivot (kohni ke beech) aazmaya to khala bana, is liye rad kar diya. Kohni ke **neeche wale hisse** par pivot rakha, to fold band rehta hai.
- **Bazu ka uthna:** 22° tak ghoom kar Codex ka "raised" pose (2 frames dissolve).
- **Sar:** ±4° par collar par seam aayi, is liye sirf ±1° rakha.
- **Pivots:** maine visual test se chune hain. Yeh Codex ke certified nahi.

Tafseel: `RIG_AND_ATTACHMENT_QA.md`. Har file ka istemal: `CODEX_ASSET_INTEGRATION_MANIFEST.csv`.

**Istemal nahi hue:**
- bare-hands candidates (seams verify nahi)
- wrist ke layers (hard cuts)
- torso underlay aur sleeve overlap (registered nahi, haze)

## Libraries

16 repos ke README parhe (`research/LIBRARY_REVIEW.md`). **Koi repo install ya run nahi kiya.** Renderer wohi Cairo wala hai, jaisa brief mein kaha tha. Unke ideas code mein dobara banaye:
- trim-path teer
- har held shot par halka push
- ek world-to-screen function
- accumulate karne wale diagrams

MotionClone ka repo 404 hai. Whisper install nahi kiya; purani phrase timing istemal hui.

## Kya check kiya

- **Physics self-check pass:** velocity hamesha neeche, height kabhi nahi barhti, 47.7 s ke baad needle nahi uthti, zameen se takkar nahi.
- **Asal file:** 1877 frames, decode saaf, **0 freeze**, −16.4 LUFS.
- **Motion strips dekhi:** opening, bazu uthna, reaction, lens, trail, slowdown. Masle mile aur theek kiye:
  - opening mein figure nazar nahi aati thi
  - lens screen se bahar ja raha tha
  - labels aapas mein takra rahe the
  - reaction mein chehra kat raha tha
  - 21.9 s par freeze tha
- **Storyboard:** 75 full-size panels. Phone size par bhi check kiya.
- **Before/after:** aap ke 8 screenshots ke saath V12 usi waqt par (`qa/before_after/`).

## Abhi kya baqi hai (publish se pehle)

- **Approval:** saari art candidate hai. Mera rig bhi approval chahta hai.
- **Kohni:** 22° par upar ek chhota halka notch hai, jo sirf ~0.3 s ki harkat mein dikhta hai. Codex se 10°/15°/22° ke painted elbow folds maange hain.
- **Sar:** ±1° se zyada nahi ghoom sakta. Iske liye neck/collar overlap art chahiye.
- **Dastanay:** three-quarter aur back mein ab bhi grey dastanay hain.
- **Chhote labels:** "schematic", ruler aur "×30" (8–9.5 units) phone par chhote hain.
- **Neechi uncha'i par zameen** ab bhi saada hai.
- **Sunna:** main audio sun nahi sakta. Headphones par kisi insaan ka sunna zaroori hai.
- **SFX licence:** 15 library cues clear nahi. Rights-clear mix maujood hai.
- **Narration ka faisla aap ka hai.** Kuch dobara record ya rewrite nahi hua.
- **Real-time playback:** player mein real-time playback nahi kiya; decode, strips aur stills se check kiya.

V1–V11 bilkul mehfooz hain. Kuch upload ya publish nahi hua.
