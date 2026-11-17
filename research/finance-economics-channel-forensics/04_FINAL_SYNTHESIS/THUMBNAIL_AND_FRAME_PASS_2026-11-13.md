# Thumbnails, frames aur endings: 2026-11-13 pass

Labels: VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Studio CTR UNKNOWN, isliye "thumbnail ne click diya" naapa nahi ja sakta.

## 1. Thumbnail review: 7 DB channels (Monkey, Casual Finance, Crayon, Economics Explained, Primate, Capital Case, Nutshell)
- Method: har channel ke andar views se top-5 aur bottom-5 long video, shuffle, sirf tile letter (title/views chhupe). Sheets aur key `~/YIOS-local-audits/finance-viral-forensics-2026-11-12/blind_2026-11-13/` (Mac-only, git mein nahi). Script: `_scripts/thumb_blind_sheets_2026-11-13.py`, scoring `thumb_blind_score_2026-11-13.py`, result `_analysis/thumb_blind_scored_2026-11-13.csv`. 1 thumbnail file disk par missing tha.
- **Blinding adhoori thi (VERIFIED limitation):** maine pichle opening test mein in videos ke titles/hooks parhe the, isliye S/W guess ka score (62/70) **leak hai aur saboot nahi** (Monkey, Crayon, Primate, Capital Case mein 10/10 titles yaad hone ki wajah se). Isse "thumbnail se strong pehchana ja sakta hai" **mat nikalna**.
- Features (tile par jo dikha, key kholne se pehle code kiye; 70 tiles): 

| feature | strong (35) | weak (35) |
|---|---|---|
| thumbnail par number/$/%/saal | 9 | 13 |
| asli naam (insaan/company/event/mulk) | 17 | 12 |
| sawal (?) | 4 | 8 |

  Ishara (INFERRED, MEDIUM-LOW, koi significance test nahi, n chhota): strong thumbnails mein asli naam/event zyada (17 vs 12), sawal kam (4 vs 8); number thumbnail par weak mein **zyada** hai (13 vs 9), yani "bara number thumbnail par" akela rule nahi.
- Visual style notes (VERIFIED, dekha): Nutshell ka sheet har tile par ek hi garam-rang/starburst template aur bold text, phir bhi views 190 se 1.04M tak; Primate ke 10 mein se 7 tiles ek hi baandar + ek object layout. Template same, views alag, jaise pehle video-level findings.

## 2. PENNY (13 long) aur Paper Billions (4): thumbnails Apify raw se
- Downloaded 17 maxresdefault.jpg (i.ytimg.com, public) `~/YIOS-local-audits/.../ext_thumbs_2026-11-13/`. Views-ordered sheets dekhe (**blind nahi**, views pata the). Source JSON SHA-256 pehle se saved hai.
- PENNY (VERIFIED dekha): #1 "$0 vs $40 TRILLION" (1.15M): do-taraf contrast + bara number. Wahi $40T concept #6 "$40 TRILLION PONZI?" (13.6k) alag framing (Capitol + muskurata chehra) aur number adha kata hua. Ye 1 jodi dikhati hai ke number wala thumbnail bhi 85x farq de sakta hai. Neeche ke (3-5k): "SECRET FAMILIES?" (Fed), "ASML" (sirf brand naam), "Google" (do chehre) mein koi number/contrast nahi. Jensen Huang wale 4 thumbnails 40k-148k ke beech.
- Paper Billions (VERIFIED, sirf 4): sab laal "-$" number + Nvidia ka Jensen Huang cartoon (3/4); sabse kam (144k) wala Jensen ke bina, "-$80 BILLION" aur ghanta bajata aadmi. n=4, kuch nahi nikalta.

## 3. Frames
- Chrome pilot (Capital Case "Rockefeller", strong): opening ~6 s ek cartoon shehar ka frame, end ~579 s ek ledger-book close-up (VERIFIED, ek video). Kharcha: ek video ke 2 frames ke liye ~5 tool calls + 30-60 s ke ads (do ads peechhe peechhe, mid-frame par ad aa gaya). Ek akela end-frame bina narration ke payoff nahi batata.
- Isliye baaqi videos par frames **nahi** liye (UNKNOWN: opening/payoff frames Capital Case, PENNY, Paper Billions, Crayon, Monkey, EE, Nutshell). Payoff ke liye neeche transcript ending use kiya.

## 4. Endings (transcript ke aakhri 80 words, 181 videos, 7 DB channels)
| tier | n | CTA (subscribe/like/comment) | "next/watch/click" |
|---|---|---|---|
| strong | 59 | 10 (17%) | 17 (29%) |
| mid | 63 | 19 (30%) | 23 (37%) |
| weak | 59 | 15 (25%) | 20 (34%) |
Koi saaf separation nahi (regex flags, INFERRED). Padhne mein: Capital Case ke strong 4 ke endings sab ek "quiet verdict" line par ("Order.", "They got a policy."), weak 4 mein "For now, anyway."/"Nobody has that answer." jaise adhoori ending; Nutshell har video "Subscribe so you won't miss..." se khatam, strong aur weak dono. Ye ek chhoti text observation hai, test nahi. File: `_analysis/endings_2026-11-13.csv`, script `_scripts/ending_test_2026-11-13.py`.

## 5. Launch model par asar
Koi naya rule nahi jodna. Thumbnail: asli naam/event + ek idea; sawal-wale ya sirf-brand thumbnails weak ki taraf (ishara). Number akela guarantee nahi. Ending/CTA ko lever mat maano. Dono HYPOTHESIS.

## 6. Abhi bhi NAHI hua
Opening/payoff frames (sirf 1 video pilot); sahi blind thumbnail review (kisi aur ko ya titles bhule hue session ko karna hoga); Studio CTR; 14/28-din re-pull.
