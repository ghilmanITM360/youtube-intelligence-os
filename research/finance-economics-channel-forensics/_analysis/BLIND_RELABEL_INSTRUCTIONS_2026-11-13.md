# Blind relabel: labeler ke liye (kisi taza session ya insaan ko do)
Sirf `blind_openings_PACKET_2026-11-13.csv` kholo. KEY file, views, titles, channel ke naam mat dekho.
Har `bid` ke `opening_60w` ke liye ek label likho (STAKE / PERSONA / OTHER):
- STAKE: pehle ~30 words mein asli tareekh/naam/waqia ya bara number jo viewer ke paise/zindagi se juda ho.
- PERSONA: invented/cartoon kirdaar ya "Meet X / This is X" / mazaq se shuru.
- OTHER: baaqi (sawal, general bayan).
Output: `bid,label` CSV. Phir: `python3 _scripts/blind_opening_packet_2026-11-13.py score <labels.csv>`.
Nota: packet mein 181 videos; sirf 7 DB channels (PENNY/PB shamil nahi).
