# ASR proper-noun check (2026-11-09)

Status: `ASR_UNCERTIFIED`. This note does not change any transcript in `transcripts_asr_base_20261109/`.

## Why this exists
The 199 transcripts in this hub come from Whisper `base` (CPU, fp16 off). Before deciding on a `small.en` rerun, a pilot compared four settings on three Shorts. Results are OBSERVED by reading the text. Reference spellings come from the video titles and standard names. No audio was listened to.

## Pilot (n = 3 Shorts, about 40 s each)
Videos: `EcA1oScUzoA` (OpenAI), `WbU0Z50PlWE` (SpaceX IPO), `8rf3Ql04hKA` (Goodhart's Law).
Prompt = a short list of names: OpenAI, SpaceX, Goodhart's Law, Wall Street, Warren Buffett, MicroStrategy, Bitcoin, private credit, petrodollar, Casual Finance.

| Setting | OpenAI | SpaceX | Goodhart's Law | Other observation |
|---|---|---|---|---|
| base | ok | ok | "Good Heart's Law" | baseline |
| base + prompt | ok | ok | ok | new slip: "managing the message metrics" |
| small.en | ok | ok | "Good Heart's Law" | cleaner punctuation |
| small.en + prompt | ok | ok | ok | small slips: "blindspots", stray "so" |

Speed on CPU (per 40 s Short): base about 3-6 s, small.en about 6-8 s.

## Reading of the result
- Common names (OpenAI, SpaceX) were already right in `base`.
- Only the rarer name (Goodhart) failed, and only the prompt fixed it.
- The prompt can add its own slips, so a prompted run is not strictly better.
- n = 3 is too small to claim an overall accuracy gain. No rerun was done.

## Names to check before reusing any transcript text
Goodhart's Law (heard as "Good Heart's"), MicroStrategy, Brett Johnson (SpaceX CFO, spelling not verified), petrodollar, Warren Buffett, and any figure or percentage. Check against the video or a primary source.

## If a rerun is wanted later
`small.en` is already cached at `~/.cache/whisper/small.en.pt` (no download needed). Use `tools/transcribe.py small.en <ids>` with an `initial_prompt` of names, and write to a new folder so the `base` record stays intact. Start with the 33 long videos, where a name error costs the most.
