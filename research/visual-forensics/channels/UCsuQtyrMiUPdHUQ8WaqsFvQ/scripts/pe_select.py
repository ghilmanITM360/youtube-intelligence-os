"""Freeze selection v1 (before any visual review). Usage: python3 -I pe_select.py"""
import csv, json, pathlib, datetime
W = pathlib.Path.home()/"YIOS-local-audits/primitive-education"
C = {r["video_id"]: r for r in csv.DictReader(open(W/"census/source_census.csv"))}
S = [ # id, split, reason (queue order = list order)
 ("qB_EKkMyuUE","DEV","Landscape; highest public view snapshot among 16:9; 136.8 s; relationship topic"),
 ("IUur04eOd4A","DEV","Portrait; highest public view snapshot of channel; 40.8 s; earliest era; science/weapons topic"),
 ("3AsDdMQr_nQ","DEV","Landscape; shortest of main-era 16:9; 68.5 s; everyday topic; lowish view snapshot"),
 ("f1vIzsTFrp4","DEV","Portrait; short duration 17.1 s; multi-part series middle; relationship topic"),
 ("KyBWJPaF1KI","DEV","Landscape; long 206 s; science topic; early era"),
 ("uIG2U_1xynQ","DEV","Portrait; 53.9 s; high view snapshot; series opener; science topic"),
 ("RmTdnXHbI8s","DEV","Landscape; 163 s; finance topic; contrasts with Short W8AVd7RhTME"),
 ("W8AVd7RhTME","DEV","Portrait; 40.3 s; finance series late part"),
 ("DekaeZPzTAQ","DEV","Landscape; longest 211 s; biology topic; late main era"),
 ("Nv4xJ_NsFdo","DEV","Portrait; 60.2 s; culture topic with no long-form sibling in local set; longest portrait"),
 ("RM_KBLDLsnQ","DEV","Landscape; latest upload (2026-05) era outlier, lowest 16:9 view snapshot; 78.4 s"),
 ("xBJ6suQSt98","HELD_OUT","Landscape held-out; first 16:9 upload; 98.8 s; science"),
 ("6YHva7Me2ls","HELD_OUT","Landscape held-out; 128 s; economics topic"),
 ("C_jSOXP_XWY","HELD_OUT","Portrait held-out; latest Short series; lowest view snapshot of the channel's local set; 11.8 s"),
 ("5gSIU30yiVs","HELD_OUT","Portrait held-out; 25 s; everyday topic series end"),
]
rows = []
for i,(v,sp,why) in enumerate(S,1):
    c = C[v]; assert c["has_video"]=="True" and c["identity_class"]=="EXACT_ID_MATCH" and int(c["decode_errors"])==0
    rows.append(dict(queue=i, video_id=v, split=sp, displayed_format=c["displayed_format"], platform_type=c["reg_type"], title=c["reg_title"], published=c["reg_published"], views_snapshot=c["reg_views"], snapshot_date=c["reg_snapshot"], duration_s=float(c["duration"]), frames=int(c["decoded_frames"]), sha256=c["sha256"], bytes=int(c["bytes"]), reason=why))
assert len({r["video_id"] for r in rows})==15
m = dict(version="selection_v1", frozen_utc=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), channel=dict(name="Primitive Education", channel_id="UCsuQtyrMiUPdHUQ8WaqsFvQ", url="https://www.youtube.com/channel/UCsuQtyrMiUPdHUQ8WaqsFvQ", identity_evidence="seven-channel readiness 03_CHANNEL_AND_VIDEO_METADATA_RECONCILIATION.csv (metadata branch research/youtube-12-channel-metadata@967ea707): 45/45 EXACT_ID_MATCH; distinct from PrimateEconomics-MP4"),
  population=dict(local_files=45, unique_ids=45, video=44, audio_only_excluded=["cZYdi9aFv6I"], landscape_16_9=8, portrait_9_16=36, letterbox_or_pillarbox_detected=0, byte_duplicates=0),
  selected_format_split=dict(landscape=8, portrait=7), note_platform="Portrait files are all registry-type SHORT and landscape all REGULAR, from catalog snapshot 2026-10-20; display format measured independently. Views are a public snapshot, used for contrast only, never causal.",
  held_out_rule="HELD_OUT videos stay unopened until dev manual rules are frozen; then evaluated against rules without editing them first.", videos=rows)
(W/"selection/selection_v1.json").write_text(json.dumps(m,indent=1)); print(len(rows), sum(r["frames"] for r in rows), sum(r["frames"] for r in rows if r["split"]=="DEV"))
