# V11 — Final Report (Roman Urdu)

## Mukhtasar nateeja

V11 video ban gayi hai: `SKYDIVER_SLOWDOWN_V11.mp4` (78.2 s, 1080×1920, 24 fps, aap ki asal narration).

- Aap ke screenshots mein jo masle the, unmein se zyada tar theek ho gaye hain:
  - joints ke gol disc
  - boots
  - pack
  - clock jaisa dial
  - lamba strap
  - checkerboard zameen
  - airflow
  - 0:41 aur 1:08 ka hujoom
- **Lekin yeh abhi bhi review cut hai, publish ke liye tayyar nahi.**

## Aap ke screenshots ka audit

Sab 9 screenshots dekhe gaye aur har ek ko V10 ke shot se milaya gaya. Har masle ki wajah likhi gayi (artwork, rig, layer order, diagram design waghera).

- Tafseel: `V10_SCREENSHOT_DEFECT_AUDIT.md`
- Har time ke liye aap ka screenshot aur V11 ke frames saath saath: `qa/before_after/`

## Codex V11 package

Codex ne khud likha hai ke package **incomplete** hai:
- Character ke **jude hue (fused) poore poses** hain, alag hilne wale parts nahi.
- Sab "candidate, unregistered, not approved" hain.

**Maine kya kiya:**
- **Poore poses istemal kiye:** side, three-quarter aur back. Har pose ek drawing hai, is liye koi joint khul nahi sakta aur koi gol disc nazar nahi aata.
- **Side pose ke boots:** oval top code se theek kiye (`tools/fix_boots.py`).
- **Kapron ke rang ek jaise kiye:** side pose ki patloon grey, aur three-quarter ki door wali aasteen cream (`tools/recolour.py`).
- **Glance head:** side body par register kiya. Nazar kalai ki taraf jhukne wale shots mein yahi lagta hai.
- **Wrist art:** mounted aur POV istemal hue. In mein device ka chehra khaali tha, is liye maine code se scale banaya: SLOW → FAST, "↓ DOWN SPEED", 9 ticks aur ek needle.
- **Codex landscape:** opening mein laga. Baqi shots ki zameen ke rang bhi isi se liye gaye.
- **Istemal nahi hue:** akele (bina kalai ke) device ki tasveerein, kyunke aap ne kaha tha ke device kalai ke baghair nahi dikhna chahiye.
- **Retire kiye:** V9 ke limb rigs, V10 ka clock dial aur V10 ki painted zameen.

Poori list hash ke saath: `CODEX_REPAIR_INTEGRATION_MANIFEST.csv`.

## Kya naya bana

1. **Speedometer sequence (0:52–0:59):** side view → nazar kalai par → apni (first-person) kalai par device, zameen neeche → push-in, needle girti hai → kalai se zameen ki taraf tilt, zameen qareeb aati hai. Device hamesha kalai par hai.
2. **Shuru ka wrist shot:** 0.9 s ke do inserts ki jagah ab 2.1 s ka ek shot hai. Isme bazu, cuff aur haath dikhte hain, aur camera dial tak push-in karta hai.
3. **Forces (0:41 aur 1:08):** ek waqt mein ek cheez:
   - ek hi scale par weight aur drag
   - tips par ek ring ("tiny difference here")
   - poori screen ka card: "zoomed 30x, not the same scale"
   - NET FORCE: UP
   - phir body par sirf "still moving DOWN"
4. **Airflow:** pehle "you: moving down". Phir hawa ki lakeerein jism ke gird mudti hain aur upar jaate chevrons dikhte hain ("so the air rushes UP past you"). Yeh simulation nahi, saaf likha hai ke "simplified sketch" hai.
5. **Equal-time positions:** do column hain. Ek "speeding up" (faasle barhte hain), doosra "slowing down" (faasle ghatte hain). Har position pichhli se neeche hai.
6. **Zameen:** checkerboard khatam. Ab be-qaida khet, jangal ke jhund, ghoomti sarkein, aur neechi uncha'i par khet ki qataarein hain.
7. **Graph:** labels ki takkar theek ki gayi.
8. **Awaaz:** V10 ka sound design rakha aur naye picture ke mutabiq retime kiya.
   - Har card ke neeche hawa ~8 dB kam hoti hai (naapa gaya).
   - Zoom cards par halki reveal cues hain.
   - Rights-clear mix bhi maujood hai.

## Kya check kiya gaya

- **Physics model dobara chalaya:** peak ~81 m/s, aakhir mein ~51 m/s, D/W zyada se zyada 1.035. Screen par koi number nahi.
- **Self-check pass:**
  - speed kabhi negative nahi
  - height kabhi nahi barhti
  - 47.7 s ke baad needle nahi uthti
  - girne ke baad needle zero se upar rehti hai
- **Asal file ki jaanch:** 1877 frames, decode saaf, −16.4 LUFS, aur koi freeze nahi.
- **Motion review:** 5 sequences ki motion strips dekhi gayin. Unmein jo masle mile woh theek karke dobara render kiya.
- **Storyboard:** 90 full-size panels. Phone size (360×640) par bhi check kiya.

## Abhi kya baqi hai (publish se pehle)

- **Bazu aur haath alag se nahi hilte.** Poses poori drawings hain. Bazu uthane ya haath ki harkat ke liye Codex se layered side pose chahiye (`CODEX_REMAINING_ASSET_REQUEST_V11.md`).
- **Approval:** Saari V11 art candidate hai, approved nahi. Meri repairs ki bhi approval chahiye.
- **Dastanay:** three-quarter aur back mein grey dastanay hain, side aur kalai mein nange haath.
- **C1 reaction chehra:** ab bhi V9 ka close-up hai, kyunke V11 ka expressive chehra nahi hai.
- **Neechi uncha'i par zameen** kuch saada hai.
- **Chhote alfaaz:** "SPEED (your wrist)" inset ka text phone par chhota hai.
- **Sunna:** main audio sun nahi sakta. Kisi insaan ko headphones par sunna zaroori hai.
- **SFX licence:** library clips clear nahi hain (rights-clear mix maujood hai).
- **Narration ka faisla aap ka hai.** 78.2 s recording sirf review-cut ke taur par lagi hai. Kuch dobara record ya rewrite nahi kiya gaya.

V1–V10 bilkul mehfooz hain. Kuch upload ya publish nahi hua.
