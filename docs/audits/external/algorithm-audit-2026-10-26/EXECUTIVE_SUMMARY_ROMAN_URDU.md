# Executive Summary (Roman Urdu) — YouTube Algorithm aur Hamara Data, 2026-10-26

## 1. YouTube algorithm asal mein kya karta hai?
- YouTube ka official maqsad do cheezein hain: har viewer ko woh video dikhana jo woh dekhna chahe, aur **lambe arsay ki satisfaction** barhana. (Source: YouTube Help 16533387)
- Koi ek formula ya ek "score" nahi hai. YouTube khud kehta hai: "doesn't follow a set formula". Signals har viewer aur har surface ke liye alag weight paate hain.
- YouTube teen qisam ke signals dekhta hai:
  - **Appeal**: dikhne ke baad log click karte hain ya ignore karte hain.
  - **Engagement**: dekhna shuru karke rukte hain ya nahi.
  - **Satisfaction**: video pasand aayi ya nahi (surveys, likes, "not interested").
- Har nayi video ko **apne fresh data** par parkha jata hai. Purani videos ki kamyabi khud-ba-khud nayi video ko nahi milti.
- 2016 ka Google research paper (candidate generation → ranking, watch-time prediction) **tareekhi** maloomat hai. Yeh saboot nahi ke 2026 mein bilkul wahi system hai.

## 2. Home, Search, Suggested aur Shorts mein farq
- **Home/Browse:** zyada tar viewer ki watch history par chalta hai. Har viewer ka feed alag hota hai.
- **Suggested/Up Next:** jo video abhi dekhi ja rahi hai, wohi "main signal" hai.
- **Search:** relevance (title, description, content query se match), us query par engagement, aur quality (expertise/authority/trust). Search results "sab se zyada views wali list" nahi hain.
- **Shorts feed:** personalized hai. "Stayed to watch" ka matlab hai pehle chand seconds ke baad rukna. Shorts aur long-form ke views ek jaisi ikai (unit) nahi hain.
- **Upload ka waqt** lambi muddat ke views par asar nahi daalta (sirf live/premiere ke liye ahem hai). **Break lene** par penalty nahi hoti.

## 3. Hamare data ne kya dikhaya?
- **Data census:**
  - 2 SQLite DBs (75 channels, 2,303 videos) mukammal scan hue.
  - Do `.db` files khali (0 bytes) hain.
  - Finance: 1,612 videos registered hain. Inmein 449 ka deep audit mukammal hai (brief mein 448 likha tha; NICK_173 ab ho chuka hai).
- **Sab se bara factor channel hai:** views ke farq ka 38% (Finance) se 58% (sab niches) sirf is baat se samjha jata hai ke video kis channel ki hai.
- **Hit-driven duniya:** har channel ke top 10% videos aam taur par channel ke ~67% views laate hain.
- **Title tricks portable nahi:**
  - Original data mein "curiosity" titles 1.35× aur "opportunity/wealth" 1.28× behtar the.
  - "Fear/threat" titles 0.75× (kamzor) the.
  - Lekin 7 naye channels (418 videos) par yeh asar **dobara nazar nahi aaye**. Yaani title ka andaz har channel ke audience ke saath fit hota hai; universal formula nahi.
- **Ek hi title, ulta nateeja:**
  - "Your Life If You Start Building Wealth in Your 30s" ek channel par 14.8× aur doosre par 0.14×.
  - "How Banks Treat You at Every Level of Wealth" ek par 159× aur doosre par 0.07×.
- **Prediction fail hui:** title aur duration se hum yeh nahi bata sakte ke kaunsi video chalegi. Hamara model "sab normal hoga" wale andaze se behtar nahi tha.
- **Likes ka ulta rishta:** jo videos zyada phailti hain, unka like-rate kam hota hai (9/9 channels). Isliye like-rate satisfaction ka acha paimana nahi.
- **Do channels par kamyab concepts:** "Renting vs Buying — The Real Math" (350× aur 297×), "compounding number" (51× aur 67×). Yeh concrete, numbers wale faisla-sawalat hain. Yeh sirf hypothesis hai.

## 4. Kya sirf assumptions hain?
- Search traffic ne "Rent vs Buy" jaisi videos chalayin: **unknown** (traffic source data nahi hai).
- Visual density (ziyada visual states) ne Casually Finance ki video ko breakout banaya: **sabit nahi** (sirf 2 videos).
- Opening mein sawal (question) se nuqsaan hota hai: **ishara hai (0.74×) magar dobara test nahi ho saka**.
- Thumbnail ka asar: hamare paas **upload ke waqt ki thumbnails nahi hain**, aur analyst notes outcome jaan kar likhe gaye the.

## 5. Kaunsi strategies test karni chahiye?
1. Apne channel par **Studio data export** pehle din se (impressions, CTR, retention, traffic source).
2. Har long-form par **YouTube "Test & compare"** (title/thumbnail A/B). Winner watch-time se tay hota hai, CTR se nahi.
3. **Opening test:** sawal se shuru karna vs seedha stake/jawab se shuru karna; 30-second retention compare karein.
4. **"X vs Y — asal hisaab"** format, poore source aur durust calculation ke saath. Competitors ki ghaltiyan hamari credibility ka faida ban sakti hain.
5. Har idea ko production se pehle audience-fit par check karein (viewer, masla, payoff ek line mein).

## 6. Kaunsi mashhoor theories ghalat ya unsupported hain?
- "CTR X% se upar ho to algorithm push karta hai": koi official threshold nahi hai.
- "Fear titles hamesha chalte hain": hamare data mein ulta (0.75×) aur naye channels par koi asar nahi.
- "Paise ki raqam ($) title mein daalo": koi asar nahi mila (1.07×, p=0.55).
- "Perfect upload time": official taur par long-term views par asar nahi.
- "Tags bohat zaroori hain": official — sirf spelling ki ghaltiyon mein madad.
- "Kisi kamyab creator ka format copy karo to chal jayega": hamara data ulta dikhata hai.

## 7. Hamare project ki taqat aur kamzori
- **Taqat:**
  - Saaf provenance aur mukammal census.
  - 1,141 videos par age-matched peer ratio.
  - 449 deep audits mein claim/calculation receipts.
  - Replication ke liye alag channels mojood hain.
- **Kamzori:**
  - Koi private metric nahi (CTR, retention, traffic).
  - Snapshots purane aur frozen hain.
  - Nick Invests data par haavi hai.
  - Forensic sample sirf hits ka hai.
  - Visual 003 yahan dastiyab nahi.

## 8. Agla qadam
- **Research:** expansion videos ke transcripts, blind packaging coding, aur competitor views ke dobara snapshots (har ek ke liye alag ijazat aur cost approval).
- **Production:** apna channel instrument karein, A/B tests aur opening tests chalayein, aur faisle medians aur STRONG videos ki frequency par karein, ek video par nahi.
