"""
Main Visualization Engine

This module contains the Visualizer class that manages:
- Pygame window and display
- Array generation and visualization as bars
- UI elements (buttons, statistics, info panels)
- User interaction handling
- Sorting algorithm execution with visual feedback
"""

import pygame
import random
from utils.colors import Colors
from utils.config import Config
from utils.algorithm_info import ALGORITHM_INFO

class Visualizer:
    def __init__(self, config):
        """
        Initialize the Visualizer with all necessary components.

        Args:
            config: Configuration object containing window size, array settings, etc.
        """
        # Store configuration reference
        self.config = config

        # Create Pygame window with specified dimensions
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption("Sort Lab - Sorting Algorithm Visualizer")

        # Clock for controlling frame rate
        self.clock = pygame.time.Clock()

        # Initialize fonts for different text sizes
        self.font_title = pygame.font.Font(None, config.FONT_SIZE_TITLE)
        self.font_normal = pygame.font.Font(None, config.FONT_SIZE_NORMAL)
        self.font_small = pygame.font.Font(None, config.FONT_SIZE_SMALL)

        # ===== ARRAY DATA =====
        self.array = []  # The array of values to be sorted
        self.array_size = config.DEFAULT_ARRAY_SIZE  # Current size of array
        self.generate_array()  # Generate initial random array

        # ===== STATE TRACKING =====
        self.color_array = []  # Colors for each bar (for visualization states)
        self.comparisons = 0  # Count of element comparisons
        self.swaps = 0  # Count of element swaps
        self.is_sorting = False  # Whether sorting is currently in progress
        self.is_sorted = False  # Whether array is fully sorted
        self.current_algorithm = None  # Name of currently running algorithm
        self.speed = config.DEFAULT_SPEED  # Animation delay in milliseconds
        self.current_step = -1  # Current step being executed in algorithm (-1 = none)

        # ===== UI ELEMENTS =====
        self.buttons = self._create_buttons()  # Dictionary of button objects

    def generate_array(self):
        """
        Generate a new random array and reset all statistics.

        Creates an array of random integers between MIN_VALUE and MAX_VALUE.
        Resets visualization colors and statistics counters.
        """
        # Generate random array with values in configured range
        self.array = [random.randint(self.config.MIN_VALUE, self.config.MAX_VALUE)
                      for _ in range(self.array_size)]

        # Initialize all bars with default color (light cyan)
        self.color_array = [Colors.DEFAULT] * len(self.array)

        # Reset statistics
        self.comparisons = 0
        self.swaps = 0
        self.is_sorted = False

    def _create_buttons(self):
        """Create UI buttons"""
        buttons = {}
        y_pos = 20
        x_start = 50

        button_configs = [
            ('bubble', 'Bubble Sort'),
            ('selection', 'Selection'),
            ('insertion', 'Insertion'),
            ('merge', 'Merge Sort'),
            ('quick', 'Quick Sort'),
            ('heap', 'Heap Sort'),
            ('reset', 'Reset'),
            ('slower', 'Slower'),
            ('faster', 'Faster'),
            ('size_up', 'Size +'),
            ('size_down', 'Size -'),
        ]

        for i, (key, label) in enumerate(button_configs):
            x_pos = x_start + (i * (self.config.BUTTON_WIDTH + self.config.BUTTON_MARGIN))
            buttons[key] = {
                'rect': pygame.Rect(x_pos, y_pos, self.config.BUTTON_WIDTH, self.config.BUTTON_HEIGHT),
                'label': label,
                'color': Colors.BUTTON_BG
            }

        return buttons

    def draw_array(self):
        """
        Draw the array as vertical bars on the screen.

        Each array element is represented as a bar:
        - Bar height is proportional to element value
        - Bar color indicates its current state (comparing, swapping, sorted, etc.)
        - Bars are drawn side by side across the visualization area
        """
        # Calculate width of each bar based on array size
        bar_width = self.config.VIS_AREA_WIDTH / len(self.array)

        # Maximum height available for bars
        max_height = self.config.VIS_AREA_HEIGHT

        # Find maximum value in array for height scaling
        max_value = max(self.array) if self.array else 1

        # Draw each element as a vertical bar
        for i, value in enumerate(self.array):
            # Calculate bar height proportional to value
            # Larger values -> taller bars
            bar_height = (value / max_value) * max_height

            # Calculate bar position
            x = self.config.VIS_AREA_X + i * bar_width  # Horizontal position
            y = self.config.VIS_AREA_Y + max_height - bar_height  # Vertical position (from top)

            # Get color for this bar (reflects current state)
            color = self.color_array[i] if i < len(self.color_array) else Colors.DEFAULT

            # Draw the bar (rectangle)
            # -2 on width creates small gap between bars for visibility
            pygame.draw.rect(self.screen, color,
                           (x, y, bar_width - 2, bar_height))

    def draw_algorithm_panel(self):
        """
        Draw the algorithm panel on the right side showing:
        - Algorithm name
        - Pseudocode steps
        - Current step highlighted with synchronized color
        """
        if not self.current_algorithm or self.current_algorithm not in ALGORITHM_INFO:
            return

        info = ALGORITHM_INFO[self.current_algorithm]
        steps = info.get('steps', [])

        # Panel background
        panel_rect = pygame.Rect(
            self.config.ALGO_PANEL_X,
            self.config.ALGO_PANEL_Y,
            self.config.ALGO_PANEL_WIDTH,
            self.config.ALGO_PANEL_HEIGHT
        )
        pygame.draw.rect(self.screen, Colors.PANEL_BG, panel_rect, border_radius=5)
        pygame.draw.rect(self.screen, Colors.BLACK, panel_rect, 2, border_radius=5)

        # Algorithm title
        title_y = self.config.ALGO_PANEL_Y + 15
        title = self.font_normal.render(f"Algorithm: {self.current_algorithm}", True, Colors.TEXT_COLOR)
        self.screen.blit(title, (self.config.ALGO_PANEL_X + 15, title_y))

        # Draw separator line
        line_y = title_y + 35
        pygame.draw.line(
            self.screen,
            Colors.LIGHT_GRAY,
            (self.config.ALGO_PANEL_X + 10, line_y),
            (self.config.ALGO_PANEL_X + self.config.ALGO_PANEL_WIDTH - 10, line_y),
            2
        )

        # Draw pseudocode steps
        step_y = line_y + 20
        line_height = 30

        for i, step in enumerate(steps):
            # Determine background color for current step
            if i == self.current_step and self.is_sorting:
                # Get current bar color state for synchronization
                if self.color_array:
                    # Find the most common non-default color in array
                    comparing_count = self.color_array.count(Colors.COMPARING)
                    swapping_count = self.color_array.count(Colors.SWAPPING)
                    pivot_count = self.color_array.count(Colors.PIVOT)

                    # Choose highlight color based on current operation
                    if swapping_count > 0:
                        bg_color = Colors.SWAPPING
                        text_color = Colors.WHITE
                    elif pivot_count > 0:
                        bg_color = Colors.PIVOT
                        text_color = Colors.WHITE
                    elif comparing_count > 0:
                        bg_color = Colors.COMPARING
                        text_color = Colors.BLACK
                    else:
                        bg_color = Colors.DEFAULT
                        text_color = Colors.BLACK
                else:
                    bg_color = Colors.DEFAULT
                    text_color = Colors.BLACK

                # Draw highlighted background for current step
                highlight_rect = pygame.Rect(
                    self.config.ALGO_PANEL_X + 10,
                    step_y + i * line_height - 5,
                    self.config.ALGO_PANEL_WIDTH - 20,
                    line_height - 2
                )
                pygame.draw.rect(self.screen, bg_color, highlight_rect, border_radius=3)

                # Render step text with appropriate color
                step_text = self.font_small.render(step, True, text_color)
            else:
                # Normal step (not current)
                step_text = self.font_small.render(step, True, Colors.TEXT_COLOR)

            self.screen.blit(step_text, (self.config.ALGO_PANEL_X + 20, step_y + i * line_height))

    def draw_ui(self):
        """Draw user interface elements"""
        # Title
        title = self.font_title.render("Sort Lab", True, Colors.TEXT_COLOR)
        self.screen.blit(title, (self.config.WINDOW_WIDTH // 2 - title.get_width() // 2, 70))

        # Buttons
        mouse_pos = pygame.mouse.get_pos()
        for key, button in self.buttons.items():
            color = Colors.BUTTON_HOVER if button['rect'].collidepoint(mouse_pos) else Colors.BUTTON_BG
            pygame.draw.rect(self.screen, color, button['rect'], border_radius=5)
            pygame.draw.rect(self.screen, Colors.BLACK, button['rect'], 2, border_radius=5)

            label = self.font_small.render(button['label'], True, Colors.BUTTON_TEXT)
            label_rect = label.get_rect(center=button['rect'].center)
            self.screen.blit(label, label_rect)

        # Stats
        stats_y = self.config.VIS_AREA_Y + self.config.VIS_AREA_HEIGHT + 30
        stats = [
            f"Array Size: {len(self.array)}",
            f"Comparisons: {self.comparisons}",
            f"Swaps: {self.swaps}",
            f"Speed: {self.speed}ms",
        ]

        if self.current_algorithm:
            stats.insert(0, f"Algorithm: {self.current_algorithm}")

        for i, stat in enumerate(stats):
            stat_text = self.font_normal.render(stat, True, Colors.TEXT_COLOR)
            self.screen.blit(stat_text, (50 + i * 220, stats_y))

        # Algorithm information panel
        if self.current_algorithm and self.current_algorithm in ALGORITHM_INFO:
            info = ALGORITHM_INFO[self.current_algorithm]
            panel_y = stats_y + 40
            panel_x = 50

            # Draw panel background
            panel_rect = pygame.Rect(panel_x, panel_y, 1100, 100)
            pygame.draw.rect(self.screen, Colors.PANEL_BG, panel_rect, border_radius=5)
            pygame.draw.rect(self.screen, Colors.BLACK, panel_rect, 2, border_radius=5)

            # Draw algorithm info
            info_y = panel_y + 10
            desc_text = self.font_small.render(f"Description: {info['description']}", True, Colors.TEXT_COLOR)
            self.screen.blit(desc_text, (panel_x + 10, info_y))

            complexity_y = info_y + 25
            complexity_lines = [
                f"Time Complexity - Best: {info['time_best']}, Average: {info['time_avg']}, Worst: {info['time_worst']}",
                f"Space Complexity: {info['space']}"
            ]

            for i, line in enumerate(complexity_lines):
                text = self.font_small.render(line, True, Colors.TEXT_COLOR)
                self.screen.blit(text, (panel_x + 10, complexity_y + i * 25))

    def handle_button_click(self, pos):
        """Handle button clicks"""
        for key, button in self.buttons.items():
            if button['rect'].collidepoint(pos):
                if key == 'reset':
                    self.generate_array()
                    self.is_sorting = False
                    self.current_algorithm = None
                elif key == 'faster':
                    self.speed = max(self.config.MIN_SPEED, self.speed - 10)
                elif key == 'slower':
                    self.speed = min(self.config.MAX_SPEED, self.speed + 10)
                elif key == 'size_up':
                    if not self.is_sorting:
                        self.array_size = min(self.config.MAX_ARRAY_SIZE, self.array_size + 10)
                        self.generate_array()
                elif key == 'size_down':
                    if not self.is_sorting:
                        self.array_size = max(self.config.MIN_ARRAY_SIZE, self.array_size - 10)
                        self.generate_array()
                else:
                    # Algorithm button clicked
                    if not self.is_sorting:
                        self.current_algorithm = button['label']
                        self.start_sorting(key)

    def start_sorting(self, algorithm_key):
        """
        Start the sorting process with the selected algorithm.

        Args:
            algorithm_key: String key identifying which algorithm to run
                          ('bubble', 'selection', 'insertion', 'merge', 'quick', 'heap')

        This method:
        1. Sets sorting flag to prevent concurrent sorts
        2. Resets statistics counters
        3. Imports and runs the selected sorting algorithm
        4. Algorithm function will update display during execution
        5. Marks sorting as complete when done
        """
        # Set flag to prevent starting another sort while one is running
        self.is_sorting = True

        # Reset statistics for new sort
        self.comparisons = 0
        self.swaps = 0

        # Dynamically import and run the selected algorithm
        # Each algorithm is in its own module for organization
        if algorithm_key == 'bubble':
            from algorithms.bubble_sort import bubble_sort
            bubble_sort(self)  # Pass visualizer to algorithm
        elif algorithm_key == 'selection':
            from algorithms.selection_sort import selection_sort
            selection_sort(self)
        elif algorithm_key == 'insertion':
            from algorithms.insertion_sort import insertion_sort
            insertion_sort(self)
        elif algorithm_key == 'merge':
            from algorithms.merge_sort import merge_sort
            merge_sort(self)
        elif algorithm_key == 'quick':
            from algorithms.quick_sort import quick_sort
            quick_sort(self)
        elif algorithm_key == 'heap':
            from algorithms.heap_sort import heap_sort
            heap_sort(self)

        # Clear sorting flag - algorithm has completed
        self.is_sorting = False
        self.is_sorted = True

    def update_display(self):
        """
        Update the display with current visualization state.

        This method is called frequently during sorting to show:
        - Current array state as bars
        - UI elements (buttons, statistics, info)
        - Animation with controlled speed

        The delay at the end controls animation speed.
        """
        # Clear screen with white background
        self.screen.fill(Colors.WHITE)

        # Draw all UI elements (buttons, stats, info panels)
        self.draw_ui()

        # Draw the array as colored bars
        self.draw_array()

        # Draw the algorithm panel on the right side
        self.draw_algorithm_panel()

        # Update the display (swap buffers)
        pygame.display.flip()

        # Add delay to control animation speed (milliseconds)
        # Lower speed value = faster animation
        pygame.time.delay(self.speed)

    def run(self):
        """
        Main application loop - runs until user closes window.

        This is the heart of the application that:
        1. Processes user events (mouse clicks, window close)
        2. Updates the display every frame
        3. Maintains target frame rate
        """
        # Main loop control flag
        running = True

        while running:
            # Limit frame rate to FPS setting (e.g., 60 FPS)
            # Prevents excessive CPU usage
            self.clock.tick(self.config.FPS)

            # Process all pending events
            for event in pygame.event.get():
                # User clicked X button to close window
                if event.type == pygame.QUIT:
                    running = False

                # User clicked mouse button
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if click was on any button
                    self.handle_button_click(event.pos)

            # Redraw everything (UI and array bars)
            self.update_display()
