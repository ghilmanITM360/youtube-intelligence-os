"""Shared style tokens for Finance Short 01 artwork (palette, strokes, type)."""

C = {
    # Phase 1 approved roles
    "ink": "#142A38",      # outlines, structure, text
    "teal": "#147D83",     # offer / repayment path / Remy sweater
    "coral": "#F16850",    # conditional charge / deferred interest
    "paper": "#FFF5DF",    # paper, cuffs, collar
    "gold": "#E8BC62",     # time
    "skin": "#BB7557",     # Remy skin
    "hair": "#342A39",     # Remy plum-black curls
    # Phase 2 extensions (shades of the same roles)
    "teal_dk": "#0E646A", "teal_lt": "#4FA9A6", "teal_pale": "#CFE7E2",
    "coral_dk": "#C94B37", "coral_pale": "#FBD3C9",
    "paper_dk": "#E9D9BA", "paper_dkr": "#D3C09C",
    "gold_dk": "#C99A3E", "gold_pale": "#F6E3B4",
    "skin_dk": "#9A5940", "skin_lt": "#CC8B6A", "blush": "#C96A57",
    "hair_lt": "#5B4656", "hair_dk": "#221A26",
    "slate": "#34505F", "slate_dk": "#263D4A",
    "shoe": "#3B2D35", "sole": "#E9DCC2",
    "mouth": "#5E2627", "tongue": "#D9705F", "teeth": "#FFF9EE",
    "navy_bg": "#142A38", "navy_mid": "#1B3744", "navy_dk": "#091D29",
    "white": "#FFFFFF",
    # environment neutrals
    "wall": "#F3E6CF", "wall_dk": "#E4D2B4", "floor": "#C98F5E", "floor_dk": "#AD7449",
    "floor_lt": "#DDA673", "wood": "#9C6440", "wood_dk": "#7A4B30", "plant": "#3E8E6E",
    "plant_dk": "#2C6B53", "sage": "#9DBFAE", "sky": "#BFE0E3",
}

SW = 8          # character outline width at scale 1 (1080x1920 frame)
SW_PROP = 7     # prop outline width
SW_FINE = 4     # interior detail lines
FONT = "Avenir Next, 'Avenir Next', Avenir, 'Nunito Sans', Arial, sans-serif"
