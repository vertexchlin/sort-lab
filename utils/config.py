"""
Configuration settings for the application
"""

class Config:
    # Window settings
    WINDOW_WIDTH = 1400  # Increased width for algorithm panel
    WINDOW_HEIGHT = 700
    FPS = 60

    # Visualization area (left side - for bars)
    VIS_AREA_X = 50
    VIS_AREA_Y = 150
    VIS_AREA_WIDTH = 800  # Reduced to make room for algorithm panel
    VIS_AREA_HEIGHT = 400

    # Algorithm panel (right side)
    ALGO_PANEL_X = 900  # Start after visualization area
    ALGO_PANEL_Y = 150
    ALGO_PANEL_WIDTH = 450
    ALGO_PANEL_HEIGHT = 400

    # Array settings
    DEFAULT_ARRAY_SIZE = 50
    MIN_ARRAY_SIZE = 10
    MAX_ARRAY_SIZE = 200
    MIN_VALUE = 10
    MAX_VALUE = 500

    # Animation settings
    DEFAULT_SPEED = 50  # milliseconds
    MIN_SPEED = 1
    MAX_SPEED = 500

    # UI settings
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 40
    BUTTON_MARGIN = 10

    # Font settings
    FONT_SIZE_TITLE = 36
    FONT_SIZE_NORMAL = 20
    FONT_SIZE_SMALL = 16
