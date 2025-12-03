"""
Sort Lab - Sorting Algorithm Visualization
Main entry point for the application

This module initializes the Pygame environment and starts the visualization application.
It creates the main window and runs the event loop for interactive sorting demonstrations.
"""

import pygame
import sys
from visualization.visualizer import Visualizer
from utils.config import Config

def main():
    """
    Main function that initializes and runs the Sort Lab application.

    Steps:
    1. Initialize Pygame library
    2. Create configuration object with window and array settings
    3. Create visualizer with the configuration
    4. Run the main visualization loop
    5. Clean up and exit when window is closed
    """
    # Initialize Pygame library (required before using any Pygame functions)
    pygame.init()

    # Create configuration object with all settings
    config = Config()

    # Create the main visualizer object that manages display and sorting
    visualizer = Visualizer(config)

    # Run the main application loop (handles events and updates display)
    visualizer.run()

    # Clean up Pygame resources when application closes
    pygame.quit()
    sys.exit()

# Entry point: Run main() when script is executed directly
if __name__ == "__main__":
    main()
