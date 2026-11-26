# V13 Cleanup aur Consolidation Report (Roman Urdu)

Project ka asal path: `/Users/ghilmanislam360/workprojects/unreasonably-exact/skydiver-slowdown/`

## Mukhtasar nateeja

- V13 ab **mukammal taur par khud-mukhtar (independent)** hai. Ek alag folder mein, jahan v8–v12 aur SFX Library maujood nahi the, V13 ko shuru se dobara banaya gaya. Har final file **bit-for-bit wohi** bani.
- `v8`, `v9`, `v10`, `v11`, `v12` **macOS Trash mein bhej diye** gaye hain. Wahan se wapas laaye ja sakte hain. Trash khaali nahi kiya.
- Final videos ke SHA-256 hash **badle nahi**.

## 1. Dependency audit: kya mila

| V13 kis cheez par bahar se depend karti thi | Kahan thi | Ab kahan hai |
|---|---|---|
| Python environment (cairocffi, CairoSVG, numpy, Pillow…) | `v8/.venv` | `v13/.venv` (wohi Python 3.14.7, wohi packages offline copy kiye) + `v13/requirements.txt` |
| Rig banane ka source art | `v12/CODEX_V12_ART_PACKAGE/` | `v13/CODEX_V12_ART_PACKAGE/` (zip copy nahi kiya, duplicate tha) |
| Rig ka master body (`side_body_v11_repaired.png`) | `v11/codex_request/` | `v13/codex_request/v11/` |
| Codex V13 kaam ki reference images (`side_master_v11.png` waghera) | `v12/codex_request/` | `v13/codex_request/v12/` |
| Opening comparison sheet ke liye V10/V11/V12 videos | `v10–v12/*.mp4` | Sirf zaroori 24 frames: `v13/qa/reference/opening_frames/` (poori videos copy nahi kin) |
| Mix mein istemal 8 SFX clips | `../SFX Library/` (project se bahar) | `v13/audio/sfx_library_used/` (asal SFX Library ko haath nahi lagaya) |
| Library review document | `v12/research/LIBRARY_REVIEW.md` | `v13/history/v12/research/` |
| Purane versions ke docs, manifests, prompts, provenance, timelines | v8–v12 ki .md/.csv/.json/.txt/.edl files | `v13/history/v8 … v12/` (255 files, 2.5 MB) |

Pehle se V13 ke andar the (kuch karna nahi para): narration (`audio/narration_preserved.m4a`), phrases, rigs (`assets/v12rig`, `rigs/`), character aur environment art (`assets/`), Codex V11/V13 packages, model (`tools/model.py`), Whisper model, owner screenshots, timeline (`timeline/V13_timeline.json`, `V13.edl`).

**Copy nahi kiya** (zaroorat nahi thi): purani renders, frames, motion tests, zips, caches, purane storyboards.

## 2. Badle gaye paths aur commands

- `tools/mix_v13.py`: `LIB` ab `audio/sfx_library_used` hai.
- `tools/build_rig.py`: master body ab `codex_request/v11/…` se. Run note ab `.venv/bin/python`.
- `tools/boards_v13.py`: opening sheet ab saved reference frames se banti hai, purani videos se nahi.
- `work/hands.py`, `finish.py`, `folds.py`, `neck.py`: v12 paths ki jagah v13 paths.
- `tools/fix_boots.py`, `tools/recolour.py`: yeh V11 ke purane one-off scripts the jo `v11/` mein likhte the. Inko `work/legacy_v11/` mein rakh diya; rebuild ka hissa nahi.
- `START_HERE.md`: har command mein `../v8/.venv/bin/python` ki jagah `.venv/bin/python`.
- `SCIENTIFIC_VISUAL_RESEARCH.md`: `../v12/research/…` ki jagah `history/v12/research/…`.
- `../.claude/launch.json` (project se bahar, local preview config): v9/v10 ki jagah v13. Purani copy: `qa/cleanup/launch.json.before`.

## 3. Delete se pehle verification

Final files ke hash (`qa/cleanup/hashes_before.txt`):

| File | SHA-256 |
|---|---|
| SKYDIVER_SLOWDOWN_V13.mp4 | a8d17b029af4e54de851078e3d7838c254895f91395b43645321fb016ec659aa |
| SKYDIVER_SLOWDOWN_V13_captions.mp4 | c2ac0d6e73dbed09464234cbf713719570cf21fa90a6db5e5fe524e584599c7c |
| SKYDIVER_SLOWDOWN_V13.srt | 22010476d634dce769ff13cf87c7c21652c55fe39baf2dddd303e6978a047e90 |
| SKYDIVER_SLOWDOWN_V13_picture.mp4 | 619c8ef364055a4d74f832f90aae8efd80c15ce0e2b8510630d508d5c33c544e |
| audio/V13_mix.wav | 8a0137d8b56937fa8b9b77549cfe2e874dd4b5ac03e00139732f998d89b1ba88 |
| audio/V13_mix_rights_clear.wav | 563b09572b5d3cacaa460808171c150530a1ec9175fe783ad532cac822b5827f |

**Alag folder mein mukammal rebuild.** V13 ko scratch folder mein copy kiya, jahan v8–v12 aur SFX Library nahi the. Final outputs copy nahi kiye. Phir `START_HERE.md` ke commands chalaye:

1. Narration se 16 kHz copy
2. whisper.cpp transcription
3. Captions aur SRT
4. Model self-check aur picture render
5. Caption overlay
6. Stems aur dono mixes
7. Dono MP4 mux
8. Storyboard, comparisons, proofs
9. Rig rebuild

Nateeja:
- SRT, captions JSON, picture MP4, dono mixes, final MP4, caption MP4: **sab hash bilkul same**.
- Self-check: "25 shots continuous, model time monotonic, v≥0, no rise, needle monotonic after 47.7 s, min alt 445 m".
- Rig rebuild: `assets/v12rig` ki 16 files **byte-identical**.

Yeh asal saboot tha. Is ke baad deletion ka faisla kiya.

## 4. Kya Trash mein gaya

`trash` (macOS ka apna command) se yeh paanch folders Trash mein bheje:

| Folder | Size |
|---|---|
| v8 | 269 MB (275,068 KB) |
| v9 | 395 MB (404,128 KB) |
| v10 | 888 MB (909,620 KB) |
| v11 | 1.0 GB (1,055,876 KB) |
| v12 | 481 MB (492,784 KB) |
| **Kul** | **≈ 3.0 GiB (3,137,476 KB)** |

Koi aur cheez delete nahi ki. Yeh sab mehfooz hain:
- SFX Library aur us ka zip
- scripts aur DOCX files
- `skydiver-slowdown.zip`
- baqi projects

## 5. Cleanup ke baad verification

- `skydiver-slowdown/` mein ab sirf `v13` hai.
- Hash check (`shasum -c`): 6/6 files **OK**, kuch nahi badla.
- Dono MP4: 1877 frames, decode mein 0 errors.
- Asal V13 folder se doosra alag rebuild (ab v8–v12 kahin nahi the): SRT, picture, mix, MP4, caption MP4, sab **SAME**. Self-check pass.
- Timeline (`timeline/V13_timeline.json`, `V13.edl`) aur asset references: sab V13 ke andar ki files ki taraf ishara karte hain. Rebuild mein boards ne inhe dobara likha bina error ke.

## 6. Storage

| | Pehle | Baad |
|---|---|---|
| `skydiver-slowdown/` | 4.81 GiB (5,044,632 KB) | 1.92 GiB (2,012,592 KB) |
| `v13/` | 1.82 GiB | 1.92 GiB (+103 MiB: venv 65 MB, V12 art 21 MB, request images 9 MB, SFX 4.6 MB, history 2.5 MB, frames 1.3 MB) |

- **Project se hata:** takreeban **2.9 GiB** (3,032,040 KB).
- **Disk par asal mein khaali hua:** **abhi 0**. Folders Trash mein hain, jo usi disk par jagah leta hai. Jab aap khud Trash se yeh paanch folders hatayenge, tab takreeban 3.0 GiB khaali hoga.

## 7. Kya V13 mukammal independent hai?

**Haan, project ki files ke lehaz se.** Do system tools bahar se chahiye, jo kisi purane version ka hissa nahi the:
- Homebrew ka `ffmpeg`
- Homebrew ka `whisper-cli`
- Homebrew Python 3.14 (`/opt/homebrew/opt/python@3.14`). `.venv` usi par bana hai. Agar Python update ho kar 3.14 hat jaye, to `requirements.txt` se naya venv banana hoga.

## Baqi masle

- **Update (owner ki ijazat ke baad):** `qa/_audio/` (865 MiB) aur `qa/_chunks_mov`, `qa/_chunks_mp4` (62 MiB) bhi Trash mein bhej diye. Yeh sirf build ke dauran banne wali temporary files theen. `mix_v13.py` aur `v13.py` har build par inhe khud dobara banate hain; koi aur script inhe nahi parhti. Is ke baad bhi 6/6 hash OK rahe. `v13/` ab **1.01 GiB** (1,062,380 KB) hai, aur `skydiver-slowdown/` bhi takreeban itna hi.
- Trash ko main khol kar list nahi kar saka (macOS ne "Operation not permitted" diya). `trash` command ne har folder ke liye kaamyabi di, aur folders project se gayab hain. Finder mein Trash khol kar dekh lein.
- V13 ke creative masle wohi hain jo `FINAL_VISUAL_AND_AUDIO_QA.md` mein hain:
  - art approval
  - headphones par sunna
  - SFX licence
  - narration ka faisla
- Kuch upload ya publish nahi hua.

## Update: Trash se hamesha ke liye delete (owner ki ijazat ke baad)

Owner ne sirf hamare 8 items delete karne ka kaha:
- v8, v9, v10, v11, v12
- V13 ke temp folders: `_audio`, `_chunks_mov`, `_chunks_mp4`

Yeh ab Trash se bhi hamesha ke liye hat gaye hain; wapas nahi aa sakte. Trash mein owner ki apni 1 cheez thi; usay chhera nahi, woh wahin hai.

Disk par khaali jagah 261,768,696 KB se barh kar 265,866,956 KB ho gayi, yani **takreeban 3.9 GiB (4,098,260 KB) asal mein reclaim hui**.
