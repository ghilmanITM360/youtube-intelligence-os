# Visual Forensics Standard — owner summary (Roman Urdu)

**Kya bana?**
- Aap ka poora visual-forensics kit ek permanent Claude skill `visual-ct-scan` ki shakal mein tayyar aur validate ho gaya hai. Ismein yeh sab hain:
  - SKILL.md;
  - 14 reference modules;
  - 7 templates;
  - chaaron original prompts, byte-for-byte same (hash match).
- Saath mein yeh files bhi hain:
  - mode-routing table;
  - YIOS bridge;
  - validator;
  - examples;
  - install report.

**Abhi repo mein kyun nahi gaya?**
- Finance handoff abhi `MACHINE_B_RELEASED_AWAITING_MACHINE_A_ACCEPTANCE` state mein hai.
- Machine B ka repo Finance branch par hai, aur nayi branch banana mana hai.
- Is waqt commit ya push karna Machine A ke handoff mein dakhal hota. Is liye sab kuch Git ke bahar is folder mein mehfooz hai.
- Repo, Finance JSONL aur Excel, MP4 aur ZIP: kisi ko haath nahi lagaya.

**Kaun se modes hain aur kab chalenge?**
- "inventory" → `INVENTORY`. Sirf file ki pehchaan aur hash.
- "1fps / overview" → `STRUCTURAL`.
- "visual forensics", "deep / deeper visual analysis" → `DEEP`.
- "CT scan", "frame by frame" → `CT_SCAN`.
- "recreate / reconstruct / motion reconstruction" → `RECONSTRUCTION` bhi saath judta hai.
- "channel visual DNA" → `CHANNEL_DNA`. Iske liye kai mukammal video reports chahiye; ek pilot kaafi nahi.

**Imaandari ke usool:**
- 1fps sheets sirf overview gate pass karti hain.
- 4 pilots ab bhi `VISUAL_ANALYSIS_PARTIAL` hain.
- 448 videos ka "complete review" nahi hua.
- Insaan ke sune bagair koi AV sign-off nahi hoga.
- Retention, CTR ya gaze ke numbers kabhi ghade nahi jayenge.

**Smoke test:** `uPQcyookL0Y` par dry run hua. Sirf purana evidence parha gaya, koi nayi decoding nahi hui. Status PARTIAL hi raha, jaisa hona chahiye tha.

**Aage kya?**
1. Machine A acceptance publish kare.
2. Phir handback ke baad, ya aap ki ijazat se, report mein likhi 5 commands se patch lagega, validator chalega, aur ek docs-only commit normal push hoga.
3. Tab jaa kar skill project mein khud-ba-khud trigger hogi.
