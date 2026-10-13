"""Layered explanatory diagrams placed in 1080x1920 frame coordinates (navy stage).

Every diagram is schematic: no dollar values, rates, dates or chart units. Layer order in
each dict is the intended reveal order. Fact IDs refer to ../FACT_CHECK.md.
"""
import props as P
from props import g, p, t
from style import C


def place(svg, x, y, s=1.0, rot=0):
    r = f" rotate({rot})" if rot else ""
    return f'<g transform="translate({x} {y}){r} scale({s})">{svg}</g>'


def panel(x, y, w, h, fill=None, stroke=None):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="{fill or C["paper"]}" '
            f'stroke="{stroke or C["ink"]}" stroke-width="7"/>')


def ledger():
    """B4 (F3): promotional balance vs deferred interest accruing, not yet charged."""
    L = {}
    L["ledger_title"] = place(P.label_pill("DEFERRED INTEREST", fill=C["coral"], color=C["ink"], size=40), 540, 300)
    L["ledger_balance"] = place(P.balance_card(1.0), 290, 660, 1.25)
    L["ledger_receipt_clip"] = place(P.receipt_clip(), 790, 470, 1.15)
    for n in (1, 3, 6):
        L[f"ledger_receipt_rows_{n:02d}"] = place(P.interest_receipt(rows=n), 790, 500, 1.15)
    L["ledger_timeline"] = place(P.month_strip(12, highlight_last=False), 156, 1050)
    L["ledger_purchase_day"] = (place(P.label_pill("PURCHASE DAY", fill=C["teal"], size=26), 214, 962)
                                + p("M188 990 V1012", sw=6, color=C["paper"]))
    L["ledger_link"] = p("M300 760 C300 860 190 900 188 1012", sw=6, color=C["paper"],
                         extra=' stroke-dasharray="4 16"')
    L["ledger_not_charged"] = place(P.label_pill("ACCRUING • NOT YET CHARGED", fill=C["paper"],
                                                 color=C["ink"], size=30), 540, 1210)
    return L


def outcome_fork():
    """B5/B6 (F4, F5): the IF switch and its two outcomes."""
    L = {}
    L["fork_switch"] = place(P.if_switch("up"), 540, 560, 0.62)
    L["fork_branch_teal"] = p("M440 620 C300 650 270 760 270 880", sw=14, color=C["teal_lt"]) + \
        p("M244 852 L270 900 L296 852", sw=14, color=C["teal_lt"])
    L["fork_branch_coral"] = p("M640 620 C780 650 810 760 810 880", sw=14, color=C["coral"]) + \
        p("M784 852 L810 900 L836 852", sw=14, color=C["coral"])
    L["fork_box_teal"] = (panel(60, 920, 420, 300, stroke=C["teal"])
                          + t(270, 990, "PAID IN FULL", 34) + t(270, 1032, "+ TERMS MET", 34)
                          + place(P.waived_stamp(), 270, 1132, 0.7))
    L["fork_box_coral"] = (panel(600, 920, 420, 300, stroke=C["coral"])
                           + t(810, 990, "BALANCE LEFT", 34) + t(810, 1032, "AT PROMO END", 34)
                           + place(P.charged_stamp(), 810, 1132, 0.66))
    return L


def balance_history():
    """B7 (F6): balances carried month by month; interest scales with each balance (schematic)."""
    L = {}
    base, x0, step = 1180, 150, 66
    bars, chips = "", ""
    for i in range(12):
        h = 470 - i * 33  # declining balance as payments arrive; schematic, no units
        x = x0 + i * step
        bars += g(f'<rect x="{x}" y="{base - h}" width="48" height="{h}" rx="8" fill="{C["teal_lt"]}" '
                  f'stroke="{C["ink"]}" stroke-width="5"/>', id=f"history_bar_{i + 1:02d}")
        r = 9 + 15 * h / 470  # interest chip proportional to the balance carried that month
        chips += g(f'<circle cx="{x + 24}" cy="{base - h - 34}" r="{r:.1f}" fill="{C["coral"]}" '
                   f'stroke="{C["ink"]}" stroke-width="4"/>', id=f"history_chip_{i + 1:02d}")
    L["history_axis"] = (p(f"M{x0 - 24} {base} H{x0 + 12 * step + 6}", sw=7, color=C["paper"])
                         + t(540, base + 52, "BALANCE CARRIED EACH MONTH", 26, fill=C["paper"], ls=1))
    L["history_bars"] = bars
    L["history_chips"] = chips
    L["history_collect"] = (p(f"M{x0} 560 V520 H{x0 + 11 * step + 48} V560", sw=7, color=C["coral"])
                            + p(f"M{x0 + 6 * step} 520 C{x0 + 6 * step} 420 780 380 850 330", sw=8, color=C["coral"])
                            + p("M822 316 L860 324 L842 360", sw=8, color=C["coral"])
                            + place(P.interest_receipt(rows=6), 900, 150, 0.6)
                            + place(P.label_pill("INTEREST ON EACH MONTH'S BALANCE", fill=C["coral"], color=C["ink"],
                                                 size=24), 470, 470))
    L["history_trace_back"] = (p(f"M{x0 + 11 * step + 40} {base + 110} H{x0 + 70}", sw=10, color=C["gold"])
                               + p(f"M{x0 + 96} {base + 86} L{x0 + 60} {base + 110} L{x0 + 96} {base + 134}",
                                   sw=10, color=C["gold"])
                               + place(P.sofa_icon(), x0 + 10, base + 118, 0.75)
                               + place(P.label_pill("SINCE BUYING THE SOFA", fill=C["gold"], color=C["ink"], size=26),
                                       600, base + 180))
    L["history_note"] = place(P.label_pill("SCHEMATIC • NOT TO SCALE", fill=C["navy_mid"], size=20), 540, 1440)
    return L


def min_payments():
    """B8 (F7): every minimum paid, yet a promotional balance can remain at the deadline."""
    L = {}
    L["min_title"] = place(P.label_pill("MINIMUM PAID ≠ PROMO PAID OFF", fill=C["paper"], color=C["ink"],
                                        size=34), 540, 300)
    for i in range(12):
        c, r = i % 4, i // 4
        L[f"min_box_{i + 1:02d}"] = place(P.check_box(True, label=f"MIN {i + 1}", label_color=C["paper"]),
                                          210 + c * 220, 470 + r * 190)
    L["min_balance_left"] = place(P.balance_card(0.3, label="AT PROMO END", remainder=True), 470, 1130)
    L["min_deadline_flag"] = place(P.deadline_flag(), 720, 1240, 0.9)
    return L


def compare():
    """B9 (F8): deferred interest vs a true 0% intro APR; keep 'interest may start after' visible."""
    L = {}
    L["compare_panel_left"] = (panel(50, 330, 470, 900) + f'<rect x="57" y="337" width="456" height="120" rx="20" '
                               f'fill="{C["coral"]}"/>' + t(285, 386, "DEFERRED", 40) + t(285, 432, "INTEREST", 40))
    L["compare_panel_right"] = (panel(560, 330, 470, 900) + f'<rect x="567" y="337" width="456" height="120" rx="20" '
                                f'fill="{C["teal"]}"/>' + t(795, 386, "TRUE 0%", 40, fill=C["paper"])
                                + t(795, 432, "INTRO APR", 40, fill=C["paper"]))
    L["compare_row1_labels"] = (t(285, 520, "DURING PROMO", 24, fill=C["slate"], ls=1)
                                + t(795, 520, "DURING PROMO", 24, fill=C["slate"], ls=1))
    L["compare_row1_left"] = place(P.interest_receipt(rows=3), 285, 548, 0.62) + t(285, 760, "interest builds", 30, weight=700)
    L["compare_row1_right"] = (place(P.interest_receipt(rows=0, header="INTEREST"), 795, 560, 0.62)
                               + t(795, 690, "none", 44, fill=C["teal"]) + t(795, 760, "for the 0% period", 30, weight=700))
    L["compare_row2_labels"] = (t(285, 850, "BALANCE LEFT AT END", 24, fill=C["slate"], ls=1)
                                + t(795, 850, "BALANCE LEFT AT END", 24, fill=C["slate"], ls=1))
    L["compare_row2_left"] = (place(P.charged_stamp(), 285, 950, 0.56) + t(285, 1060, "back-interest", 30, weight=700)
                              + t(285, 1098, "can be charged", 30, weight=700))
    L["compare_row2_right"] = (place(P.rewind_arrow(), 760, 960, 0.6) + p("M700 900 L860 1020 M860 900 L700 1020",
                                                                       sw=14, color=C["teal"])
                               + t(795, 1080, "no back-interest", 30, weight=700))
    L["compare_after_note"] = (place(P.label_pill("Interest may start", fill=C["teal_pale"], color=C["ink"], size=24),
                                     795, 1150)
                               + place(P.label_pill("after the promo period", fill=C["teal_pale"], color=C["ink"],
                                                    size=24), 795, 1200))
    return L


def two_dates():
    """B10 (F9): monthly payment due date vs the one promotion expiry date."""
    L = {}
    L["dates_due"] = (place(P.calendar_page("PAYMENT DUE", header=C["slate"], text=C["paper"]), 270, 700, 1.35)
                      + place(P.label_pill("EVERY MONTH", fill=C["slate"], size=30), 270, 920))
    L["dates_promo"] = (place(P.calendar_page("PROMO ENDS", mark="circle", header=C["coral"]), 770, 680, 1.7)
                        + place(P.label_pill("ONE DEADLINE", fill=C["coral"], color=C["ink"], size=30), 770, 950))
    L["dates_vs"] = t(530, 720, "vs", 56, fill=C["paper"])
    return L


DIAGRAMS = {"diagram_ledger": ledger, "diagram_outcome_fork": outcome_fork,
            "diagram_balance_history": balance_history, "diagram_min_payments": min_payments,
            "diagram_compare": compare, "diagram_two_dates": two_dates}
