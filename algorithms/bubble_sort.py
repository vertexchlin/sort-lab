"""
Bubble Sort Algorithm Implementation
Time Complexity: O(n²) - Quadratic time for average and worst case
Space Complexity: O(1) - Only uses a constant amount of extra space

How it works:
- Compares adjacent elements and swaps them if they're in wrong order
- Largest elements "bubble up" to the end in each pass
- Optimized with early termination if no swaps occur
"""

import pygame
from utils.colors import Colors

def bubble_sort(visualizer):
    """
    Bubble Sort: Repeatedly step through the list, compare adjacent elements
    and swap them if they are in the wrong order.

    Args:
        visualizer: The Visualizer object containing the array and display methods
    """
    # Get reference to the array we're sorting
    arr = visualizer.array
    n = len(arr)

    # Outer loop: Each pass bubbles one element to its correct position
    # After i passes, the last i elements are in their final sorted positions
    for i in range(n):
        # Step 0: Outer loop iteration
        visualizer.current_step = 0

        # Optimization: Track if any swaps occurred in this pass
        # If no swaps, the array is already sorted and we can exit early
        swapped = False

        # Inner loop: Compare adjacent elements up to the sorted portion
        # We stop at (n - i - 1) because last i elements are already sorted
        for j in range(0, n - i - 1):
            # Step 1: Inner loop iteration
            visualizer.current_step = 1
            # Check for pygame quit events to allow user to close window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Step 2: Comparison step
            visualizer.current_step = 2

            # Track number of comparisons for statistics
            visualizer.comparisons += 1

            # VISUALIZATION: Reset all bars to default color
            visualizer.color_array = [Colors.DEFAULT] * len(arr)

            # Highlight the two elements being compared in yellow
            visualizer.color_array[j] = Colors.COMPARING
            visualizer.color_array[j + 1] = Colors.COMPARING

            # Keep the already sorted elements (at the end) highlighted in green
            for k in range(n - i, n):
                visualizer.color_array[k] = Colors.SORTED

            # Update the display to show current comparison
            visualizer.update_display()

            # CORE LOGIC: Swap if current element is greater than next element
            if arr[j] > arr[j + 1]:
                # Step 3: Swap step
                visualizer.current_step = 3

                # Perform the swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Track statistics
                visualizer.swaps += 1
                swapped = True

                # VISUALIZATION: Highlight the swapping action in dark blue
                visualizer.color_array[j] = Colors.SWAPPING
                visualizer.color_array[j + 1] = Colors.SWAPPING
                visualizer.update_display()

        # Optimization: If no swaps occurred in this pass, array is sorted
        if not swapped:
            break

    # Final visualization: Mark all elements as sorted (green)
    visualizer.current_step = -1  # Reset step
    visualizer.color_array = [Colors.SORTED] * len(arr)
    visualizer.update_display()
