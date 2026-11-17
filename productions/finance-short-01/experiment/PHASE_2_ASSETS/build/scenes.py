"""Hero-frame compositions (1080x1920) built only from library instances.

Each scene = world layers (inside the camera group) + ui layers (screen-fixed). Every instance
records asset_id + transform so Remotion can rebuild the layout and animate between states.
Timings live in SCENE_ASSET_MAP.csv (provisional until the corrected MP3).
"""
import diagrams as D
import env as E
import poses_remy as PR
import props as P
import rig_associate as A
import rig_remy as R
import typography as TY
from geom import apply
from style import C

RCS_FOOT = (314, 1030)  # Remy/associate ground contact point in rig space


def char_tf(fx, fy, s, flip=False):
    """Transform placing the rig's ground point at scene (fx, fy) with scale s."""
    if flip:
        return f"translate({fx + RCS_FOOT[0] * s:.1f} {fy - RCS_FOOT[1] * s:.1f}) scale({-s} {s})"
    return f"translate({fx - RCS_FOOT[0] * s:.1f} {fy - RCS_FOOT[1] * s:.1f}) scale({s})"


def char_point(pose, part, local, fx, fy, s, flip=False, design=None):
    x, y = R.world_point(pose, part, local, design)
    x, y = (x - RCS_FOOT[0]) * s, (y - RCS_FOOT[1]) * s
    return (fx - x if flip else fx + x, fy + y)


def at(x, y, s=1.0, rot=0):
    return f"translate({x} {y})" + (f" rotate({rot})" if rot else "") + (f" scale({s})" if s != 1 else "")


def remy(pose_name, fx, fy, s, flip=False, expr=None, **over):
    pose = {**PR.POSES[pose_name]["pose"], **over}
    if expr:
        pose["expr"] = expr
    return (f"CHR_REMY_POSE_{pose_name.upper()}", R.render(pose), char_tf(fx, fy, s, flip),
            {"pose": pose_name, "expr": pose["expr"], "feet": (fx, fy), "scale": s, "flip": flip})


def assoc(pose_name, fx, fy, s, flip=True):
    pose = A.POSES[pose_name]["pose"]
    return (f"CHR_ASSOC_POSE_{pose_name.upper()}", A.render(pose), char_tf(fx, fy, s, flip),
            {"pose": pose_name, "feet": (fx, fy), "scale": s, "flip": flip})


def env_layers(kit):
    return [(f"{kit}__{k}", f"{kit.upper()}_L_{k.upper()}", v, "", {}) for k, v in E.KITS[kit]().items()]


def dgm_layers(name, only=None):
    out = []
    for k, v in D.DIAGRAMS[name]().items():
        if only is None or k in only:
            out.append((f"{name}__{k}", f"{name.upper()}_L_{k.upper()}", v, "", {}))
    return out


def inst(iid, asset_id, svg, tf="", **notes):
    return (iid, asset_id, svg, tf, notes)


def ch(iid, spec, **notes):
    aid, svg, tf, meta = spec
    return (iid, aid, svg, tf, {**meta, **notes})


def sofa_split(x, y, s, front_only=False):
    L = P.sofa_layers()
    back = [inst(f"sofa__{k}", f"PRP_SOFA_L_{k.upper()}", L[k], at(x, y, s)) for k in ("shadow", "legs", "back", "seat")]
    front = [inst(f"sofa__{k}", f"PRP_SOFA_L_{k.upper()}", L[k], at(x, y, s)) for k in ("arm_left", "arm_right", "pillow")]
    return back, front


def scenes():
    S = {}
    # ---- C01 hook -------------------------------------------------------------------------
    sign = inst("promo_sign", "PRP_PROMO_SIGN", P.promo_sign("NO", "INTEREST?"), at(540, 170, 1.4))
    S["C01A_HOOK_SIGN"] = dict(
        shots=["S01A"], world=env_layers("env_stage") + [
            sign, ch("remy", remy("shrug", 540, 2040, 1.2))], ui=[],
        note="Open on the promise. Sign swings in (pivot = string tops), Remy shrugs on 'No interest?'.")
    S["C01B_HOOK_BILL"] = dict(
        shots=["S01B"], world=env_layers("env_stage") + [
            sign, ch("remy", remy("hold_bill", 520, 2090, 1.38, expr={"preset": "concerned", "gaze": (0, 5)}))],
        ui=[], camera="",
        note="Statement slides up into Remy's grip on 'bill'; camera pushes in from C01A framing.")
    # ---- C02 store wide -------------------------------------------------------------------
    sb, sf = sofa_split(650, 1590, 0.82)
    S["C02_STORE_WIDE"] = dict(
        shots=["S02A"], world=env_layers("env_store") + sb + sf + [
            inst("price_tag", "PRP_PRICE_TAG", P.price_tag(), at(890, 1430, 0.9)),
            inst("store_sign", "PRP_PROMO_SIGN_STORE", P.promo_sign("NO", "INTEREST"), at(650, 900, 0.9)),
            ch("associate", assoc("assoc_present", 930, 1760, 0.6, flip=True)),
            ch("remy", remy("walk_a", 250, 1800, 0.62))],
        ui=[inst("qualifier", "TYP_QUALIFIER_STRIP", TY.qualifier("Illustrative offer • U.S. store card", cy=240))],
        note="'Imagine' - walk-in to the showroom; associate presents the sofa. Fictional store, no brand.")
    # ---- C03 checkout --------------------------------------------------------------------
    S["C03_CHECKOUT_OFFER"] = dict(
        shots=["S02B"], world=env_layers("env_checkout")[:2] + [
            ch("associate", assoc("assoc_present", 860, 1560, 1.0, flip=True)),
            *env_layers("env_checkout")[2:],
            inst("card_terminal", "PRP_CARD_TERMINAL", P.card_terminal(), at(930, 1090, 0.55)),
            inst("store_card", "PRP_STORE_CARD", P.store_card(), at(700, 1150, 0.6, -6)),
            ch("remy", remy("hold_sheet", 300, 1790, 1.3, expr={"preset": "intrigued", "gaze": (2, 5)}))],
        ui=[inst("qualifier", "TYP_QUALIFIER_STRIP", TY.qualifier("Illustrative offer • U.S. store card", cy=240))],
        note="Offer read in full; counter occludes the associate below the waist.")
    # ---- C04 IF switch macro --------------------------------------------------------------
    hand_pose = {**PR.POSES["point_forward"]["pose"], "expr": {"preset": "determined"}}
    tip = R.world_point(hand_pose, "hand_f", (88, -13))
    s4 = 2.4
    fx = 610 - (tip[0] - RCS_FOOT[0]) * s4
    fy = 1010 - (tip[1] - RCS_FOOT[1]) * s4
    S["C04_IF_SWITCH"] = dict(
        shots=["S03"], world=[
            inst("paper_bg", "ENV_PAPER_MACRO", f'<rect width="1080" height="1920" fill="{C["paper"]}"/>'
                 + "".join(f'<path d="M0 {y} H1080" stroke="{C["paper_dk"]}" stroke-width="4"/>'
                           for y in range(140, 1920, 64)), ""),
            inst("if_switch", "PRP_IF_SWITCH_UP", P.if_switch("up"), at(760, 820, 1.35)),
            ch("remy_arm", (f"CHR_REMY_POSE_POINT_FORWARD", R.render(hand_pose), char_tf(fx, fy, s4), {
                "pose": "point_forward", "crop": "arm/hand only; body off-frame left", "scale": s4}))],
        ui=[inst("qualifier", "TYP_LABEL_IF_PAID_IN_FULL", P.label_pill("IF PAID IN FULL", fill=C["coral"],
                                                                         color=C["ink"], size=40), at(540, 300))],
        note="Macro push from the offer's IF; fingertip lands on the switch lever.")
    # ---- C05 ledger ------------------------------------------------------------------------
    S["C05_LEDGER"] = dict(
        shots=["S04A", "S04B", "S04C"], world=env_layers("env_stage") + dgm_layers("diagram_ledger") + [
            ch("remy", remy("think_chin", 190, 1930, 0.62))], ui=[],
        note="Rows of the receipt print month by month; 'NOT YET CHARGED' label on S04C.")
    # ---- C06 path A ------------------------------------------------------------------------
    coin_from = char_point(PR.POSES["drop_coin"]["pose"], "hand_f", (60, 10), 200, 1960, 0.72)
    S["C06A_PAID_IN_FULL"] = dict(
        shots=["S05A"], world=env_layers("env_stage") + [
            inst("title", "TYP_LABEL_PAID_IN_FULL_TERMS_MET", P.label_pill("PAID IN FULL + TERMS MET", fill=C["teal"],
                                                                          size=38), at(540, 300)),
            inst("balance_card", "PRP_BALANCE_CARD_045", P.balance_card(0.45), at(560, 1010, 1.25)),
            inst("coin_1", "PRP_COIN", P.coin(), at(coin_from[0] + 20, coin_from[1] + 80, 0.8)),
            inst("coin_2", "PRP_COIN", P.coin(), at(560, 880, 0.8)),
            inst("receipt", "PRP_RECEIPT_ROWS_06", P.interest_receipt(6), at(820, 420, 0.95)),
            inst("month_strip", "PRP_MONTH_STRIP", P.month_strip(), at(156, 1180, 1.0)),
            inst("deadline_flag", "PRP_DEADLINE_FLAG", P.deadline_flag(), at(890, 1150, 0.75)),
            ch("remy", remy("drop_coin", 200, 1960, 0.72))], ui=[],
        note="Coins drop from the release hand into the balance card; fill shrinks to zero before month 12.")
    S["C06B_WAIVED"] = dict(
        shots=["S05B"], world=env_layers("env_stage") + [
            inst("title", "TYP_LABEL_INTEREST_WAIVED", P.label_pill("INTEREST WAIVED", fill=C["teal"], size=44),
                 at(540, 300)),
            inst("balance_card", "PRP_BALANCE_CARD_000", P.balance_card(0.0), at(560, 1010, 1.25)),
            inst("receipt", "PRP_RECEIPT_ROWS_06", P.interest_receipt(6), at(820, 420, 0.95)),
            inst("stamp", "PRP_STAMP_WAIVED", P.waived_stamp(), at(800, 620, 0.95)),
            inst("month_strip", "PRP_MONTH_STRIP", P.month_strip(), at(156, 1180, 1.0)),
            ch("remy", remy("relieved", 200, 1960, 0.72))], ui=[],
        note="Stamp slams on 'waived'; receipt can then fade/curl away. Remy exhales.")
    # ---- C07 path B ------------------------------------------------------------------------
    S["C07A_BALANCE_LEFT"] = dict(
        shots=["S06A"], world=env_layers("env_stage") + [
            inst("title", "TYP_LABEL_ALTERNATIVE", P.label_pill("ALTERNATIVE: BALANCE LEFT", fill=C["coral"],
                                                               color=C["ink"], size=38), at(540, 300)),
            inst("calendar", "PRP_CALENDAR_PAGE_PROMO_ENDS",
                 P.calendar_page("PROMO ENDS", mark="circle", header=C["coral"]), at(250, 620, 1.2, -4)),
            inst("balance_card", "PRP_BALANCE_CARD_030_REMAINDER", P.balance_card(0.3, remainder=True),
                 at(560, 1010, 1.25)),
            inst("receipt", "PRP_RECEIPT_ROWS_12", P.interest_receipt(12), at(800, 410, 0.8)),
            ch("remy", remy("stand_neutral", 870, 1990, 0.74, flip=True, expr={"preset": "concerned", "gaze": (3, 2)}))],
        ui=[], note="Calendar page turns to PROMO ENDS; remaining balance highlighted coral.")
    S["C07B_INTEREST_LANDS"] = dict(
        shots=["S06B"], world=env_layers("env_stage") + [
            inst("statement", "PRP_STATEMENT_CHARGED", P.statement("charged"), at(470, 900, 1.45)),
            inst("receipt", "PRP_RECEIPT_ROWS_12", P.interest_receipt(12), at(470, 300, 0.8, -6)),
            inst("stamp", "PRP_STAMP_CHARGED", P.charged_stamp(), at(470, 1250, 0.8)),
            ch("remy", remy("shocked", 870, 1990, 0.74, flip=True))],
        ui=[], note="Receipt drops onto the statement; interest row fills coral. No dollar amounts.")
    # ---- C08 not just what's left ---------------------------------------------------------
    S["C08_NOT_JUST_LEFTOVER"] = dict(
        shots=["S07A"], world=env_layers("env_stage") + [
            inst("balance_card", "PRP_BALANCE_CARD_030_REMAINDER", P.balance_card(0.3, remainder=True),
                 at(560, 760, 1.6)),
            inst("magnifier", "PRP_MAGNIFIER", P.magnifier(), at(470, 860, 1.25)),
            inst("label", "TYP_LABEL_NOT_JUST_WHATS_LEFT", P.label_pill("NOT JUST WHAT'S LEFT", fill=C["paper"],
                                                                       color=C["ink"], size=40), at(540, 300)),
            ch("remy", remy("think_chin", 220, 1930, 0.62))], ui=[],
        note="Magnifier finds the small remainder, then the label rejects 'just this'.")
    # ---- C09 balance history ----------------------------------------------------------------
    S["C09_BALANCE_HISTORY"] = dict(
        shots=["S07B"], world=env_layers("env_stage") + dgm_layers("diagram_balance_history") + [
            ch("remy", remy("walk_a", 900, 1930, 0.5, flip=True))], ui=[],
        note="Bars build left->right, chips follow, bracket collects into the receipt; gold arrow traces back to the sofa.")
    # ---- C10 minimum payments ---------------------------------------------------------------
    S["C10_MIN_PAYMENTS"] = dict(
        shots=["S08"], world=env_layers("env_stage") + dgm_layers("diagram_min_payments") + [
            ch("remy", remy("tick_pen", 150, 1960, 0.62))], ui=[],
        note="Twelve MIN ticks pop in sequence; balance card still shows a coral remainder at PROMO ENDS.")
    # ---- C11 compare --------------------------------------------------------------------------
    S["C11_COMPARE"] = dict(
        shots=["S09A", "S09B"], world=env_layers("env_stage") + dgm_layers("diagram_compare") + [
            ch("remy", remy("open_hands", 540, 1960, 0.55))], ui=[],
        note="Build left panel, then right; S09B highlights the right column. APR line awaits corrected audio.")
    # ---- C12 two dates ----------------------------------------------------------------------
    S["C12_TWO_DATES"] = dict(
        shots=["S10A", "S10B"], world=env_layers("env_living_room") + [
            inst("cal_due", "PRP_CALENDAR_PAGE_PAYMENT_DUE",
                 P.calendar_page("PAYMENT DUE", header=C["slate"], text=C["paper"]), at(720, 450, 0.95)),
            inst("cal_promo", "PRP_CALENDAR_PAGE_PROMO_ENDS",
                 P.calendar_page("PROMO ENDS", mark="circle", header=C["coral"]), at(800, 940, 1.45)),
            ch("remy", remy("circle_marker", 330, 1760, 0.85))],
        ui=[inst("label_due", "TYP_LABEL_EVERY_MONTH", P.label_pill("EVERY MONTH", fill=C["slate"], size=28),
                 at(720, 630)),
            inst("label_promo", "TYP_LABEL_ONE_DEADLINE", P.label_pill("ONE DEADLINE", fill=C["coral"], color=C["ink"],
                                                                      size=30), at(800, 1170))],
        note="Due-date card first, then Remy circles the single promotion-expiry card.")
    # ---- C13/C14 home callback ------------------------------------------------------------
    sb, sf = sofa_split(560, 1650, 1.0)
    sit = remy("sit_relaxed", 420, 1650, 0.78)
    S["C13_SOFA_HOME"] = dict(
        shots=["S11"], world=env_layers("env_living_room") + sb + [ch("remy", sit)] + sf + [
            inst("day1_tag", "TYP_LABEL_DAY_1", P.label_pill("DAY 1", fill=C["teal"], size=34), at(860, 1330))],
        ui=[], note="Sofa settles, Remy sinks in. DAY 1 tag recalls purchase day.")
    S["C14_INTEREST_WAITING"] = dict(
        shots=["S12"], world=env_layers("env_living_room") + sb + [
            ch("remy", remy("sit_notice", 420, 1650, 0.78)),
            *sf,
            inst("receipt", "PRP_RECEIPT_ROWS_06", P.interest_receipt(6), at(690, 1352, 0.44, 8)),
            inst("clock", "PRP_CLOCK_FACE", P.clock_face() + P.clock_hand("minute")
                 + f'<g transform="rotate(-90)">{P.clock_hand("hour")}</g>', at(742, 1352, 0.2))],
        ui=[inst("qualifier", "TYP_QUALIFIER_STRIP",
                 TY.qualifier("Deferred interest • waived only if paid in full on time", cy=240, size=26))],
        camera="translate(-210 -560) scale(1.35)",
        note="Push-in; the coral receipt sits on the cushion beside Remy. Clock may tick backward (original metaphor).")
    return S


def render_scene(sc):
    world = "".join(f'<g id="{iid}" data-asset="{aid}"' + (f' transform="{tf}"' if tf else "") + f">{svg}</g>"
                    for iid, aid, svg, tf, _ in sc["world"])
    ui = "".join(f'<g id="ui__{iid}" data-asset="{aid}"' + (f' transform="{tf}"' if tf else "") + f">{svg}</g>"
                 for iid, aid, svg, tf, _ in sc.get("ui", []))
    cam = sc.get("camera") or ""
    return (f'<g id="camera"' + (f' transform="{cam}"' if cam else "") + f">{world}</g><g id=\"ui\">{ui}</g>")


def layout(name, sc):
    return {"scene_id": f"SCN_{name}", "shots": sc["shots"], "camera": sc.get("camera") or "none",
            "note": sc["note"],
            "world": [{"z": i, "instance": iid, "asset_id": aid, "transform": tf or "none",
                       **{k: (list(v) if isinstance(v, tuple) else v) for k, v in meta.items()}}
                      for i, (iid, aid, _, tf, meta) in enumerate(sc["world"])],
            "ui": [{"instance": iid, "asset_id": aid, "transform": tf or "none"}
                   for iid, aid, _, tf, _ in sc.get("ui", [])]}
