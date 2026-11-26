# V9 — Final Report (Roman Urdu)

## Mukhtasar nateeja
V9 video ban gayi hai: `SKYDIVER_SLOWDOWN_V9.mp4`. Yeh 78.2 second, 1080×1920 aur 24 fps ki hai. Is mein aap ki asal 78.2 s narration hai, aur pehli dafa sound effects bhi mix hue hain.
Lekin yeh **abhi review cut hai, publish ke liye tayyar nahi.** Wajah neeche likhi hai.

## Sab se aham daryaft
- **Character art kabhi image-generated tha hi nahi.** V1 se V8 tak har character part code se bana tha: pehle Pillow se, phir V7/V8 mein SVG Bézier se. Aap ki requirement poori nahi hui thi. V9 mein bhi yehi art placeholder ke tor par hai. Codex ke liye exact request `CODEX_MISSING_ASSET_REQUEST_V9.md` mein hai (P0: side character, rear view, wrist close-up, side-view aircraft).
- **V8 mein sound effects zero thay.** Manifest mein do whoosh likhe thay, magar mix mein sirf narration thi.
- **V8 ki physics mein drag weight se 1.5 guna dikhaya gaya tha.** Asal model (NASA Glenn atmosphere, fixed posture) mein drag weight se sirf ~3% zyada hota hai. V9 mein dono arrows ek hi scale par hain, aur net force (drag − weight) ek labelled inset mein 10× bara kar ke dikhaya gaya hai.

## V9 mein kya theek hua
1. **Opening:** 10 km ki height se wide shot. Upar khula aasman, neeche haze ke saath zameen aur clouds ki tah, plane, aur choti si "you" figure. Phir motivated push-in hota hai.
2. **Environment:** har altitude par alag. Zameen perspective ke saath banti hai aur jaise height kam hoti hai, khet bare hote jaate hain. Har shot mein ek hi static pahar wala background ab nahi.
3. **Forces:** gravity (rust), drag (teal), velocity (dashed blue, alag lane), net force (violet, double line) aur airflow (patli moving lines). Paanchon ka style alag hai, aur sab body ke centre of mass se jure hue hain.
4. **Physics timing:**
   - Model "rest" se shuru hota hai: needle zero, duniya ruki hui, hawa ki awaaz taqreeban khamosh.
   - Drag theek "stronger than your weight" par weight se aage nikalta hai.
   - Speed kam hoti hai, lekin character kabhi upar nahi jata aur needle kabhi wapas nahi uthti.
5. **Speedometer:** ek hi design hai. Model section mein ek fixed card hai, aur character ke glance ke baad wrist close-up aata hai. Koi number nahi dikhaya gaya.
6. **Density:** barabar size ke boxes mein dots (10 km, abhi, zameen ke qareeb).
7. **Character motion:** haathon, pairon aur kapron mein flutter hai, sar ghuma kar wrist dekhna hai, aur close-up mein eye/brow/blink reaction hai. Model section mein posture fixed rehta hai.
8. **Sound:**
   - Synthesized wind bed (rights-clear) jo picture ke saath chalta hai, aur aircraft ki halki awaaz.
   - Library se 10 cues: 3 whoosh, 2 gust, fabric flutter, instrument tick aur paper.
   - Paanch stems alag hain.
   - Loudness −16.4 LUFS. Narration ki timing aur level nahi badla.

## Kya baqi hai (publish se pehle zaroori)
- **Codex assets:** illustrated character, wrist aur aircraft chahiye.
- **SFX licence:** library ke clips ka licence established nahi hai. Publish ke liye `audio/V9_mix_rights_clear.wav` (sirf narration aur generated ambience) maujood hai.
- **Narration ka faisla:** 78.2 s recording istemal hui hai. Slot 02 ka chhota script record hi nahi hua, is liye use nahi kiya gaya. Aap confirm karein ke kaun sa chahiye.
- **Sunna:** main audio sun nahi sakta. Mix spectrogram aur loudness measurement se kiya gaya hai. Kisi insaan ko ek dafa headphones par sun-na zaroori hai.
- **Kamzor jagah:** POV ground shot thora mosaic jaisa lagta hai, aur kuch chhote footnotes phone par mushkil se parhe jaate hain.

## Check kaise kiya
- Teen full renders hue, aur har dafa poori video ka contact sheet dekha gaya.
- 68 full-size storyboard frames banaye gaye.
- Browser mein asal playback hua (audio decode confirm kiya).
- Freeze detection chalaya gaya: sirf intentional "rest" wala 0.8 s ka hissa ruka hua hai.
- Physics self-check pass hua.
- V1–V8 bilkul mehfooz hain. Kuch upload ya publish nahi hua.
