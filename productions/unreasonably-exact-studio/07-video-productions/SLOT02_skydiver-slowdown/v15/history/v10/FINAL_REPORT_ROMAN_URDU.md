# V10 — Final Report (Roman Urdu)

## Mukhtasar nateeja
V10 video ban gayi hai: `SKYDIVER_SLOWDOWN_V10.mp4`. Yeh 78.2 s, 1080×1920 aur 24 fps ki hai, aur is mein aap ki asal narration hai. Yeh V9 se kaafi behtar hai, lekin **abhi bhi review cut hai, publish ke liye tayyar nahi.**

## Codex assets kitne istemal hue
- **V9 ke 73 assets mein se 65 integrate hue:**
  - side, three-quarter aur back ke 15-15 layers
  - closeup ke 7
  - POV gloves ke 2
  - aircraft ke 2
  - clouds ke 9
- **8 istemal nahi hue:**
  - Purana semicircular instrument (4 layers). Yeh dashboard jaisa lagta tha, is liye retire kar diya.
  - Wrist ke 4 layers. Unka strap usi purane gauge ke liye bana tha.
- **Pehle wale procedural placeholders ab mukammal taur par khatam ho gaye hain:** character, aircraft, clouds, close-up chehra, POV gloves aur wrist instrument.
- **V10 supplement ke 10 candidate files istemal hue:**
  - circular instrument: housing, dial, needle, cap aur do straps
  - unmounted forearm
  - neeche dekhta hua glance head (Claude ne isay side rig par register kiya)
  - do painted landscapes: opening ka horizon aur neeche dekhne wala POV

  Codex ne inhein khud "candidate" kaha hai, final approved nahi.

## Kya naya bana
1. **Opening:** painted horizon, chhota sa jahaz aur chhoti si "you" figure. Phir motivated push-in hota hai.
2. **Wrist sequence:** pehle side view, phir sar ghuma kar wrist dekhna (naya head). Uske baad forearm detail, jis par wahi circular device usi right wrist par bandha hai. Phir instrument close-up, jis mein sirf needle hilti hai. Device har shot mein usi kalai par rehta hai.
3. **Density:** poori screen par bare, barabar size ke boxes. 10 km par kam dots hain, beech mein zyada, aur zameen ke qareeb sab se zyada. Dots ko "marks, not molecules" likha gaya hai.
4. **Same air, same body, do speeds:** do guna speed par taqreeban 4 guna drag. Yeh main descent se alag, ek controlled comparison ke taur par dikhaya gaya hai.
5. **Force diagram:**
   - STATE 1: weight > drag.
   - STATE 2: top speed par dono barabar, lekin neeche harkat jaari.
   - STATE 3: drag > weight.

   Sab ek hi scale par hai. Farq bohat chhota (~3%) hai, is liye arrow ki tips par ek 10× "zoom lens" lagaya gaya hai, jo saaf likha hua hai.
6. **Equal-time positions:** model ki positions har 15 second baad dikhayi gayi hain. Faasle chhote hote jaate hain, lekin har position pichhli se neeche hai. Saath mein "MOVING: DOWN" aur "NET FORCE: UP" alag alag dikhaye gaye hain.
7. **Speed graph:** axes parhne ke qabil hain aur ek tracking point hai. Sirf aakhir mein do aur curves aate hain, label ke saath: "smaller / larger drag area".
8. **Overload khatam kiya:** V9 ka altitude ruler, chhota net-force box aur ek hi frame mein sab cheezein ab nahi hain. Har beat mein ek main idea hai.
9. **Sound:** V9 ka sound design rakha gaya aur naye picture ke mutabiq retime kiya gaya.
   - Diagram cards ke neeche hawa ki awaaz kam hoti hai.
   - 11 library cues hain.
   - Rights-clear mix bhi maujood hai.

## Kya check kiya gaya
- **Physics model dobara chalaya:** peak ~81 m/s, zameen ke qareeb ~51 m/s, aur drag weight se zyada se zyada ~3.5% aage. Yeh model ke values hain, universal facts nahi, aur video mein koi number nahi dikhaya gaya.
- **Self-check pass hua:** speed kabhi negative nahi, height kabhi nahi barhti, needle 47.7 s ke baad sirf neeche jaati hai, aur koi zameen se takrana nahi.
- **Visual review:** poori video ka contact sheet aur motion strips dekhe gaye, aur 82 full-size storyboard panels banaye gaye.
- **Playback:** browser mein asal playback hua (audio decode active tha, 0 dropped frames). Loudness −16.4 LUFS hai.
- **Research:** NASA Glenn ke 5 pages, Physics Classroom ke 2 pages, aur Red Bull Stratos ka record (Wikipedia aur PLOS ONE) dekhe gaye. Tafseel `SCIENTIFIC_ILLUSTRATION_RESEARCH.md` mein hai.

## Abhi kya baqi hai (publish se pehle)
- **Narration ka faisla aap ka hai.** Sirf 78.2 s recording maujood hai. Slot 02 record nahi hua, aur kuch bhi dobara record ya rewrite nahi kiya gaya.
- **Sunna:** main audio sun nahi sakta. Kisi insaan ko headphones par sunna zaroori hai.
- **SFX licence:** library clips clear nahi hain. Is liye `audio/V10_mix_rights_clear.wav` maujood hai.
- **Codex art ke masle:**
  - joints par gol caps nazar aate hain
  - three-quarter view ka chehra muskurata hua hai (identity farq)
  - instrument ka side/oblique view nahi hai
  - candidate layers ab tak approved nahi
  - painted landscapes character ke flat style se zyada detailed hain

  Tafseel `CODEX_REMAINING_ASSET_REQUEST_V10.md` mein hai.
- **Chhoti cheezein:**
  - wrist ke do shots sirf 0.9 s ke hain
  - kuch footnotes phone par chhote hain
  - phrase timing ±0.3 s hai

V1–V9 bilkul mehfooz hain. Kuch upload ya publish nahi hua.
