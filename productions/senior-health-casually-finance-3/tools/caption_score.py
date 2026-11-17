# Teacher-forced Whisper log-likelihood of candidate wordings on a clip (machine evidence only, not listening).
import sys, json, whisper, torch, numpy as np
R = "/Users/ghilmankhan/workprojects/youtube-intelligence-os/productions/senior-health-casually-finance-3/"
jobs = json.load(open(sys.argv[1] if len(sys.argv) > 1 else R + "tools/caption_score_jobs.json"))
models = {n: whisper.load_model(n) for n in ("base", "small.en")}
for pkg, a, b, cands in jobs:
    audio = whisper.load_audio(R + pkg + "/source_audio/narration_mix.wav")[int(a * 16000):int(b * 16000)]
    print(f"\n{pkg} {a}-{b}")
    for name, m in models.items():
        tok = whisper.tokenizer.get_tokenizer(m.is_multilingual, language="en", task="transcribe")
        mel = whisper.log_mel_spectrogram(whisper.pad_or_trim(audio), m.dims.n_mels).unsqueeze(0)
        with torch.no_grad():
            feat = m.encoder(mel)
            free = whisper.decode(m, mel[0], whisper.DecodingOptions(language="en", fp16=False, without_timestamps=True, beam_size=5)).text
            res = []
            for c in cands:
                pre = list(tok.sot_sequence_including_notimestamps)
                txt = tok.encode(" " + c)
                ids = torch.tensor([pre + txt + [tok.eot]])
                lp = torch.log_softmax(m.decoder(ids[:, :-1], feat)[0], -1)
                tgt = ids[0, 1:]
                s = lp[torch.arange(len(tgt)), tgt][len(pre) - 1:].sum().item()
                res.append((round(s, 2), c))
        print(f"  [{name}] free: {free.strip()}")
        for s, c in sorted(res, reverse=True):
            print(f"    {s:8.2f}  {c}")
