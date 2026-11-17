"""Approved pose library for Remy (remy-2). Targets are wrist positions in the rest frame.

Each pose lists the expressions it was QA'd with ("compatible") and its story use.
"""
import props as P

SIT_SLOTS = {k: "mid" for k in ("shin_f", "thigh_f", "shoe_f", "shin_n", "thigh_n", "shoe_n")}
SIT_LEGS = {"body_dy": 206, "leg_n": (-90, 90, 0), "leg_f": (-88, 92, -4), "slots": SIT_SLOTS}

POSES = {
    "stand_neutral": dict(
        pose={"expr": {"preset": "neutral"}},
        compatible=["neutral", "curious", "concerned", "content", "skeptical", "deadpan"],
        use="Default stance, entrances, reaction holds"),
    "point_forward": dict(
        pose={"lean": 3, "arm_f": {"ik": (668, 386), "hand_dir": -4}, "hand_f": "point", "flip_f": False,
              "expr": {"preset": "curious", "gaze": (4, 0)}},
        compatible=["curious", "determined", "concerned", "neutral"],
        use="B3 point at IF; B7/B10 indicate a label to screen-right"),
    "point_up": dict(
        pose={"arm_f": {"ik": (560, 176), "hand_dir": -48}, "hand_f": "point", "flip_f": False,
              "neck": -4, "expr": {"preset": "curious", "gaze": (4, -4)}},
        compatible=["curious", "determined", "intrigued"],
        use="Point at headline / sign above and to the right"),
    "point_across": dict(
        pose={"lean": 4, "arm_n": {"ik": (452, 470), "hand_dir": -6}, "hand_n": "point", "flip_n": False,
              "expr": {"preset": "determined", "gaze": (4, 2)}},
        compatible=["determined", "curious", "concerned"],
        use="Near-arm point across the body at a close object (switch, ledger)"),
    "hold_sheet": dict(
        pose={"arm_n": {"ik": (214, 486), "hand_dir": -12}, "hand_n": "grip_back", "flip_n": False,
              "arm_f": {"ik": (448, 492), "hand_dir": 192}, "hand_f": "grip_back", "flip_f": True,
              "props": [{"id": "held_offer_sheet", "svg": P.offer_sheet(), "at": (330, 440, -2, 0.6)}],
              "expr": {"preset": "intrigued", "gaze": (2, 4)}},
        compatible=["intrigued", "curious", "concerned", "skeptical", "neutral"],
        use="B2 reading the store-card offer"),
    "hold_bill": dict(
        pose={"lean": -3, "arm_n": {"ik": (214, 496), "hand_dir": -12}, "hand_n": "grip_back", "flip_n": False,
              "arm_f": {"ik": (448, 502), "hand_dir": 192}, "hand_f": "grip_back", "flip_f": True,
              "props": [{"id": "held_statement", "svg": P.statement("charged"), "at": (330, 440, 3, 0.66)}],
              "expr": {"preset": "concerned", "gaze": (0, 4)}},
        compatible=["concerned", "shocked", "confused", "alarmed"],
        use="B1 'Then why the interest bill?'; B6 bill lands"),
    "hold_card_up": dict(
        pose={"arm_n": {"ik": (368, 430), "hand_dir": -78}, "hand_n": "grip_back", "flip_n": False,
              "props": [{"id": "held_store_card", "svg": P.store_card(), "at": (418, 352, -10, 0.85)}],
              "neck": 4, "expr": {"preset": "curious", "gaze": (5, 2)}},
        compatible=["curious", "intrigued", "content", "skeptical"],
        use="B2 store card in hand; B9 holding the 0% card"),
    "open_hands": dict(
        pose={"arm_n": {"ik": (150, 470), "hand_dir": -118}, "hand_n": "open", "flip_n": False,
              "arm_f": {"ik": (494, 470), "hand_dir": -62}, "hand_f": "open", "flip_f": True,
              "expr": {"preset": "content"}},
        compatible=["content", "neutral", "determined", "curious"],
        use="B9 separating two offer types (two different things)"),
    "shrug": dict(
        pose={"arm_n": {"ik": (178, 520), "hand_dir": 168}, "hand_n": "palm_up", "flip_n": True,
              "arm_f": {"ik": (470, 520), "hand_dir": 12}, "hand_f": "palm_up", "flip_f": False,
              "neck": -5, "expr": {"preset": "confused"}},
        compatible=["confused", "skeptical", "deadpan"],
        use="Hook: 'No interest?' quizzical shrug"),
    "shocked": dict(
        pose={"lean": -5, "arm_n": {"ik": (186, 330), "hand_dir": -104}, "hand_n": "open", "flip_n": False,
              "arm_f": {"ik": (452, 318), "hand_dir": -76}, "hand_f": "open", "flip_f": True,
              "expr": {"preset": "shocked"}},
        compatible=["shocked", "alarmed"],
        use="B6 accumulated interest lands on the bill"),
    "think_chin": dict(
        pose={"arm_n": {"ik": (292, 352), "hand_dir": -62}, "hand_n": "fist", "flip_n": False,
              "neck": -3, "expr": {"preset": "skeptical", "gaze": (4, -3)}},
        compatible=["skeptical", "intrigued", "concerned", "focused"],
        use="B7 'Not just interest on what's left' – working it out"),
    "drop_coin": dict(
        pose={"lean": 6, "arm_f": {"ik": (592, 520), "hand_dir": 34}, "hand_f": "release", "flip_f": False,
              "expr": {"preset": "determined", "gaze": (4, 5)}},
        compatible=["determined", "focused", "content"],
        use="B5 dropping payment tokens onto the promotional balance"),
    "relieved": dict(
        pose={"lean": -3, "neck": -7, "arm_n": (10, -6, 0), "arm_f": (-10, 6, 0), "expr": {"preset": "relieved"}},
        compatible=["relieved", "happy", "content"],
        use="B5 interest waived – exhale"),
    "walk_a": dict(
        pose={"lean": 3, "leg_n": (-22, 14, -6), "leg_f": (20, 24, 4), "arm_n": (-16, -10, 0),
              "arm_f": (16, -14, 0), "expr": {"preset": "curious", "gaze": (4, 0)}},
        compatible=["curious", "neutral", "content", "determined"],
        use="Walk cycle contact pose (B2 entering store, B7 walking the timeline)"),
    "walk_b": dict(
        pose={"lean": 3, "body_dy": -6, "leg_n": (-4, 6, 0), "leg_f": (-14, 52, 10), "arm_n": (2, -6, 0),
              "arm_f": (-2, -6, 0), "expr": {"preset": "curious", "gaze": (4, 0)}},
        compatible=["curious", "neutral", "content", "determined"],
        use="Walk cycle passing pose"),
    "tick_pen": dict(
        pose={"lean": 5, "arm_f": {"ik": (590, 430), "hand_dir": 24}, "hand_f": "pen_back", "flip_f": False,
              "props": [{"id": "held_pen", "hand": "f", "svg": P.pen(), "at": (24, -4, 70, 0.8), "slot": "prop"}],
              "expr": {"preset": "focused", "gaze": (5, 3)}},
        compatible=["focused", "determined", "concerned"],
        use="B8 ticking minimum-payment boxes"),
    "circle_marker": dict(
        pose={"arm_f": {"ik": (600, 290), "hand_dir": -34}, "hand_f": "pen_back", "flip_f": False,
              "props": [{"id": "held_marker", "hand": "f", "svg": P.marker(), "at": (26, -6, 70, 0.8), "slot": "prop"}],
              "neck": -3, "expr": {"preset": "determined", "gaze": (5, -2)}},
        compatible=["determined", "focused", "content"],
        use="B10 circling the promotion-expiry date"),
    "sit_relaxed": dict(
        pose={**SIT_LEGS, "lean": -4, "arm_n": {"ik": (402, 590), "hand_dir": 12}, "hand_n": "relaxed",
              "flip_n": False, "arm_f": {"ik": (452, 584), "hand_dir": 18}, "expr": {"preset": "content"}},
        compatible=["content", "relieved", "happy", "neutral"],
        use="B11 sofa came home on day one"),
    "sit_notice": dict(
        pose={**SIT_LEGS, "lean": 2, "neck": 7, "arm_n": {"ik": (402, 590), "hand_dir": 12}, "hand_n": "relaxed",
              "flip_n": False, "arm_f": {"ik": (452, 584), "hand_dir": 18},
              "expr": {"preset": "concerned", "gaze": (5, 5)}},
        compatible=["concerned", "skeptical", "deadpan", "intrigued"],
        use="B12 notices the waiting interest receipt beside him"),
}
