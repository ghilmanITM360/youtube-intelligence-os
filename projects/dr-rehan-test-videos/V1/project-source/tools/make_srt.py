# Caption text = supplied script wording; timing = faster-whisper word starts on the MP3 (tools/words.json).
import sys
CHUNKS = [
    (0.00, "Calf pain that starts with walking"), (1.52, "and eases with rest"),
    (2.50, "is a pattern doctors don't ignore."), (4.30, "Let's see what Dr. Rahim says."),
    (5.94, "Calf pain or cramping while walking,"), (7.50, "this is called claudication"),
    (8.48, "or intermittent claudication."), (9.74, "It happens when narrowing arteries"),
    (11.26, "reduce blood flow to the leg muscles"), (12.80, "during activity."),
    (13.68, "The muscles essentially run low on oxygen."), (15.72, "The pain usually eases with rest"),
    (17.16, "and then returns with walking again."), (19.04, "This pattern is a known early signal"),
    (21.16, "of peripheral arterial disease,"), (22.94, "which is directly connected\nto the cardiovascular risk."),
    (25.60, "The signal doctors watch the most"), (27.60, "is claudication,"),
    (28.62, "that is, calf pain"), (29.70, "that appears during activity or walking"),
    (31.68, "and disappears with rest."), (32.96, "It is considered one of the most"),
    (34.28, "clinically significant early signals."), (35.96, "But if this intermittent claudication"),
    (37.30, "converts into continuous pain,\neven at rest,"), (39.98, "this occurs in patients who have got"),
    (41.50, "critical [limb] ischemia,"), (42.60, "which is a serious state of affairs"),
    (44.34, "for peripheral vascular disease."), (45.94, "It suggests that arterial blood flow"),
    (47.90, "is already reduced enough"), (49.40, "to affect muscle function,"),
    (50.64, "and research consistently shows"), (52.36, "that people with claudication"),
    (53.72, "have elevated cardiovascular risk."), (55.34, "That is why doctors"),
    (56.76, "don't dismiss leg pain during walking."), (58.88, "They always,"),
    (59.70, "always investigate."),
]
END = 60.58
ts = lambda s: f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d},{int(round(s * 1000)) % 1000:03d}"
out = []
for i, (start, text) in enumerate(CHUNKS):
    end = CHUNKS[i + 1][0] if i + 1 < len(CHUNKS) else END
    assert end > start
    out.append(f"{i + 1}\n{ts(start)} --> {ts(end)}\n{text}\n")
open(sys.argv[1], "w").write("\n".join(out))
print(len(CHUNKS), "cues")
