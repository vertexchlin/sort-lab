"""
Color definitions for visualization states
Matching color scheme: #000000, #FFFFFF, #005087, #65dcf2, #ffe564, #b590dc, #8edb62
"""

class Colors:
    # Background
    WHITE = (255, 255, 255)      # #FFFFFF - Background
    BLACK = (0, 0, 0)            # #000000 - Text and borders
    LIGHT_GRAY = (200, 200, 200)

    # Bar states
    DEFAULT = (101, 220, 242)    # #65dcf2 - Light cyan - default unsorted
    COMPARING = (255, 229, 100)  # #ffe564 - Light yellow - elements being compared
    SWAPPING = (0, 80, 135)      # #005087 - Dark blue - elements being swapped
    SORTED = (142, 219, 98)      # #8edb62 - Light green - sorted elements
    PIVOT = (181, 144, 220)      # #b590dc - Light purple - pivot element (for quick sort)

    # UI elements
    BUTTON_BG = (0, 80, 135)     # #005087 - Dark blue
    BUTTON_HOVER = (101, 220, 242)  # #65dcf2 - Light cyan hover
    BUTTON_TEXT = (255, 255, 255)   # White text
    TEXT_COLOR = (0, 0, 0)       # #000000 - Black text

    # Panel
    PANEL_BG = (240, 240, 240)
