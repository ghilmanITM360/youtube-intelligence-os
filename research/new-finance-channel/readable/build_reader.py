"""Build a readable HTML view of the new-finance-channel markdown files.
Run from repo root:  uv run --with markdown python research/new-finance-channel/readable/build_reader.py
Source .md files are never modified; output goes to research/new-finance-channel/readable/site/."""
import re, html, pathlib, shutil, markdown

ROOT = pathlib.Path(__file__).resolve().parents[3]
WS = ROOT / "research/new-finance-channel"
OUT = WS / "readable/site"
PRODS = ["productions/new-finance-channel-v1-rent-01/V1_RENT_SCRIPT.md",
         "productions/new-finance-channel-v2-airfares-01/V2_AIRFARES_SCRIPT.md",
         "productions/new-finance-channel-l3-jobs-01/L3_JOBS_SCRIPT.md"]

# plain-language box per document: (kya hai, nateeja, agla kadam)
S = {
"audit/01_INDEPENDENT_AUDIT_SUMMARY.md": ("Poore kaam ka sakht audit (jaanch).", "Score 55.5/100. Faisla: REJECTED, dobara kaam chahiye. Primary six channels 85% covered.", "Audit/18 (gap plan) padhein, phir batayein pehle kaunsa gap band karna hai."),
"audit/19_FINAL_ACCEPTANCE_REPORT.md": ("Audit ka aakhri faisla.", "REJECTED - REWORK REQUIRED. Calendar aur branch ke 2 critical gate fail.", "Gap plan (audit/18) dekhein."),
"audit/18_GAP_ANALYSIS_AND_CORRECTION_PLAN.md": ("Jo kuch kam hai uski list, priority ke saath (P0 sabse zaroori).", "12 gaps. P0 mein se ek band, ek aadha.", "Batayein kaunsa gap agla lein."),
"audit/17_NUMERICAL_QUALITY_SCORECARD.md": ("12 categories mein number.", "Kul 55.5 / 100. Sabse kamzor: calendar (2/5), knowledge documents (5/10), visual analysis (5/10).", "Sirf andaza hai, ek hi jaanchne wala."),
"audit/02_REQUIREMENT_TRACEABILITY_MATRIX.md": ("Aapki har hidayat ek-ek karke: hui ya nahi.", "36 hidayaat: 11 poori, 21 adhoori, 2 fail, 1 unverified, 1 blocked.", "PARTIAL wali rows dekhein, wahi baaki kaam hai."),
"audit/04_FINANCE_CHANNEL_COVERAGE_AUDIT.md": ("Kitne channels aur videos ka data hamare paas hai.", "72 channels, 3,832 videos. Primary six 85%. MonkeyExplains sirf 49%.", "MonkeyExplains ka baaki data paid refresh se aayega (pehle aapki approval)."),
"audit/14_CONTENT_CALENDAR_ACCEPTANCE_TEST.md": ("Calendar publish karne layak hai ya nahi.", "Nahi. 13 slots mein se sirf kuch ke paas topic hai.", "Topics validate karein, phir launch date decide karein."),
"02_FINANCE_CHANNEL_MASTER_INVENTORY/MASTER_INVENTORY.md": ("Saare 72 finance channels ki list.", "Har channel ke videos, transcripts, latest upload.", "Reference ke liye."),
"03_PRIMARY_REFERENCE_CHANNELS/STRENGTH_MATRIX_AND_LEARNINGS.md": ("Chhe bade competitor channels ne kya achha kiya.", "Monkey Economics, Casual Finance, Crayon Capital waghera ki taqat aur kamzori ek jagah.", "Naye channel ki identity yahin se bani."),
"09_TOPIC_DISCOVERY/PRIMARY_DATA_PULL_2026-11-18.md": ("Asli sarkari sources se numbers (BLS, IATA, Zillow).", "Rent ka +2.8%, airfares +22.4%, IATA ka $4.50 per passenger forecast. 'Rent gir raha hai' galat nikla.", "Publish se pehle numbers dobara check hone chahiye."),
"17_TOPIC_VALIDATION/L3_L4_VALIDATION_2026-11-19.md": ("Jobs report aur gas-price topic ki jaanch.", "Gas topic REJECT (bohot copies). Jobs report aur CPI-weights topic CONDITIONAL.", "Ye topics abhi 'proven' nahi, sirf aage badhne layak."),
"17_TOPIC_VALIDATION/PHASE_TEN_FINAL_TOPIC_VALIDATION_2026-11-18.md": ("Pehle teen topics (rent, airfares, ports) ka faisla.", "Rent aur airfares CONDITIONAL, ports REJECT.", "Scripts in do par bani hain."),
"18_CONTENT_PACKAGING/PHASE_NINE_TOPIC_TITLE_THUMBNAIL_PACKAGING_2026-11-18.md": ("Video ke title aur thumbnail ke idea.", "V1 rent aur V2 airfares ka packaging aap ne approve kiya (conditional).", "Thumbnail ki asli images abhi nahi bani."),
"19_30_DAY_CONTENT_CALENDAR/PHASE_ELEVEN_30_DAY_CALENDAR_2026-11-18.md": ("30 din ka plan (13 slots).", "Sabse jaldi launch 14 Dec 2026. 23 Nov nahi.", "Addendum bhi padhein, usme update hai."),
"19_30_DAY_CONTENT_CALENDAR/P0_FIX_CALENDAR_ADDENDUM_2026-11-19.md": ("Calendar mein nayi cheezein aur ek date ki ghalti ka fix.", "13 mein 8 slots ke paas topic ka shuruaati idea. Koi validated nahi.", "Launch date aur capacity aap decide karein."),
"16_CHANNEL_POSITIONING/PHASE_F_POSITIONING_2026-11-18.md": ("Channel ki pehchaan: kis cheez ke liye jana jayega.", "'Keemat ke peeche ka number' + 'industry kaise kaam karti hai'.", "Aap ki mansoori chahiye."),
"20_CHANNEL_BRANDING/PHASE_TWELVE_BRANDING_DIRECTIONS_2026-11-18.md": ("Channel ke naam aur look ke 3 raaste.", "Direction A (Ledger) recommended. Naam ki availability abhi check nahi hui.", "Aap naam chunein, phir handle/domain/trademark check."),
"21_PRODUCTION_WORKFLOW/PHASE_THIRTEEN_PRODUCTION_WORKFLOW_2026-11-18.md": ("Video banane ke 20 qadam.", "Research se publish tak, har gate ke saath.", "Abhi tak asli video par test nahi hua."),
"23_FINAL_STRATEGY/FINAL_STRATEGIC_RECOMMENDATION_2026-11-18.md": ("Poori strategy ek jagah.", "Search-first, hafte mein 1 long + 2 Shorts (capacity maloom nahi).", "Owner ke faislon ka intezar."),
"productions/new-finance-channel-v1-rent-01/V1_RENT_SCRIPT.md": ("Video 1 ki draft script: rent number kya naapta hai.", "~9 minute. Gate WARN (sirf images nahi).", "[CHECK] wali lines insaan ko source se confirm karni hain."),
"productions/new-finance-channel-v2-airfares-01/V2_AIRFARES_SCRIPT.md": ("Video 2 ki draft script: airfares +22% par airlines ka profit.", "~7 minute. Gate WARN (sirf images nahi).", "Nov CPI (10 Dec) ke baad numbers refresh karein."),
"productions/new-finance-channel-l3-jobs-01/L3_JOBS_SCRIPT.md": ("Video 3 ki draft script: jobs report ka margin ~122,000.", "~8 minute. Gate WARN (sirf images nahi).", "8 Jan 2027 ki release ke baad publish."),
}
GROUPS = [("audit","Audit (jaanch)"),("01_","1 Project overview"),("02_","2 Channel inventory"),("03_","3 Primary six channels"),("04_","4 Additional channels"),("05_","5 Fresh data"),("06_","6 Transcripts"),("07_","7 Thumbnails"),("08_","8 Visual (NOT DONE)"),("09_","9 Topics"),("10_","10 Sub-niches"),("11_","11 Trends/News"),("12_","12 YouTube search"),("13_","13 Titles/Hooks"),("14_","14 Thumbnail models"),("15_","15 Script models"),("16_","16 Positioning"),("17_","17 Validation"),("18_","18 Packaging"),("19_","19 Calendar"),("20_","20 Branding"),("21_","21 Workflow"),("22_","22 Originality"),("23_","23 Final strategy"),("24_","24 Sources"),("productions","Scripts (drafts)")]

def key_of(p):  # path relative to repo root -> key
    s = str(p.relative_to(ROOT))
    return s[len("research/new-finance-channel/"):] if s.startswith("research/new-finance-channel/") else s

def out_name(k): return re.sub(r"[^A-Za-z0-9._-]", "_", k.replace("/", "__")).replace(".md", ".html")

def group_of(k):
    for pre, label in GROUPS:
        if k.startswith(pre): return label
    return "Logs"

files = sorted([p for p in WS.rglob("*.md") if "readable" not in p.parts] ) + [ROOT/x for x in PRODS]
files = [p for p in files if p.exists()]
docs = [(key_of(p), p) for p in files]

CHIP = {"PASS":"ok","VERIFIED":"ok","DONE":"ok","FAIL":"bad","REJECTED":"bad","BLOCKED":"bad","PARTIAL":"mid","CONDITIONAL":"mid","WARN":"mid","CANDIDATE":"mid","UNVERIFIED":"gray","UNKNOWN":"gray","STALE":"gray","SECONDARY":"gray","INFERRED":"gray","HYPOTHESIS":"gray"}
def chipify(h):
    def f(m):
        w = m.group(2)
        return f'{m.group(1)}<span class="chip {CHIP[w]}">{w}</span>{m.group(3)}'
    return re.sub(r"(<td[^>]*>)\s*(" + "|".join(CHIP) + r")\s*(</td>)", f, h)

CSS = """
:root{--bg:#fafaf7;--fg:#1d1d1b;--mut:#5f5f58;--card:#fff;--line:#dcdcd2;--acc:#0b5cad;--ok:#1f7a3d;--bad:#b3261e;--mid:#9a6700;--gray:#6b6b63}
@media(prefers-color-scheme:dark){:root{--bg:#141412;--fg:#ecece6;--mut:#a5a59c;--card:#1d1d1a;--line:#34342f;--acc:#7db4ee;--ok:#5ec27d;--bad:#f2837c;--mid:#e0b04a;--gray:#a0a098}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 system-ui,-apple-system,Segoe UI,sans-serif}
.wrap{display:flex;min-height:100vh}nav{width:290px;flex:none;border-right:1px solid var(--line);padding:18px 14px;position:sticky;top:0;height:100vh;overflow:auto;font-size:14.5px;background:var(--card)}
nav h4{margin:16px 0 4px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}nav a{display:block;padding:3px 6px;border-radius:6px;color:var(--fg);text-decoration:none}nav a:hover,nav a.cur{background:var(--line)}
main{flex:1;min-width:0;padding:28px clamp(16px,4vw,56px) 80px;max-width:1100px}
h1{font-size:1.9rem;line-height:1.25}h2{margin-top:2.2em;padding-top:.4em;border-top:1px solid var(--line);font-size:1.35rem}h3{font-size:1.1rem;margin-top:1.6em}
a{color:var(--acc)}code{background:var(--line);padding:1px 5px;border-radius:4px;font-size:.88em;word-break:break-word}pre{background:var(--card);border:1px solid var(--line);padding:12px;overflow:auto;border-radius:8px}pre code{background:none}
.tw{overflow-x:auto;margin:1em 0;border:1px solid var(--line);border-radius:10px;background:var(--card)}table{border-collapse:collapse;width:100%;font-size:15px}
th,td{padding:9px 12px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line);min-width:90px}th{position:sticky;top:0;background:var(--card);font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}tr:nth-child(even) td{background:color-mix(in srgb,var(--line) 25%,transparent)}
.chip{display:inline-block;padding:1px 9px;border-radius:99px;font-size:12.5px;font-weight:700;color:#fff}.chip.ok{background:var(--ok)}.chip.bad{background:var(--bad)}.chip.mid{background:var(--mid)}.chip.gray{background:var(--gray)}
.box{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--acc);border-radius:10px;padding:14px 18px;margin:0 0 26px}.box b{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);margin-top:8px}.box b:first-child{margin-top:0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin:14px 0}.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px}.card .n{font-size:1.9rem;font-weight:700}.card .l{color:var(--mut);font-size:14px}
.src{color:var(--mut);font-size:13px;margin-bottom:6px}.menu{display:none}
@media(max-width:820px){.wrap{display:block}nav{position:static;width:auto;height:auto;border:0;border-bottom:1px solid var(--line)}}
"""

def nav_html(cur):
    groups = {}
    for k, _ in docs: groups.setdefault(group_of(k), []).append(k)
    order = [l for _, l in GROUPS] + ["Logs"]
    h = ['<a href="index.html" class="%s"><b>START HERE</b></a>' % ("cur" if cur == "index" else "")]
    for g in order:
        if g not in groups: continue
        h.append(f"<h4>{html.escape(g)}</h4>")
        for k in groups[g]:
            t = title_of[k]
            h.append(f'<a href="{out_name(k)}" class="{"cur" if k == cur else ""}">{html.escape(t[:60])}</a>')
    return "\n".join(h)

def page(title, body, cur, srcnote=""):
    return f"""<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head><body><div class="wrap"><nav>{nav_html(cur)}</nav><main>{srcnote}{body}</main></div></body></html>"""

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
def render(text):
    md.reset(); h = md.convert(text)
    h = re.sub(r'<table>', '<div class="tw"><table>', h); h = h.replace("</table>", "</table></div>")
    h = re.sub(r'href="([^":]+?)\.md(#[^"]*)?"', lambda m: f'href="{out_name(m.group(1).split("/")[-1]+".md") }{m.group(2) or ""}"', h)
    return chipify(h)

title_of = {}
for k, p in docs:
    t = p.read_text(errors="replace")
    m = re.search(r"^#\s+(.+)$", t, re.M)
    title_of[k] = (m.group(1).strip() if m else p.stem).replace("`", "")

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
for k, p in docs:
    text = p.read_text(errors="replace")
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)  # drop front matter
    box = ""
    if k in S:
        a, b, c = S[k]
        box = f'<div class="box"><b>Seedhi baat</b>{html.escape(a)}<b>Nateeja</b>{html.escape(b)}<b>Agla kadam</b>{html.escape(c)}</div>'
    src = f'<div class="src">Source file: <code>{html.escape(str(p.relative_to(ROOT)))}</code> (original badla nahi gaya)</div>'
    (OUT / out_name(k)).write_text(page(title_of[k], src + box + render(text), k))

START = open(WS / "readable/start_here.html", encoding="utf-8").read()
(OUT / "index.html").write_text(page("Start here: New Finance Channel", START, "index"))
print("pages:", len(docs) + 1, "->", OUT)
