"""
Selection Sort Algorithm Implementation
Time Complexity: O(n²) - Always performs n²/2 comparisons regardless of input
Space Complexity: O(1) - Only uses a constant amount of extra space

How it works:
- Divides array into sorted (left) and unsorted (right) portions
- Finds minimum element in unsorted portion
- Swaps it with first element of unsorted portion
- Grows sorted portion by one element each iteration
"""

import pygame
from utils.colors import Colors

def selection_sort(visualizer):
    """
    Selection Sort: Find the minimum element from the unsorted portion
    and swap it with the first unsorted element.

    Args:
        visualizer: The Visualizer object containing the array and display methods
    """
    # Get reference to the array we're sorting
    arr = visualizer.array
    n = len(arr)

    # Outer loop: Build sorted portion one element at a time
    # Position i is where we'll place the minimum element from unsorted portion
    for i in range(n):
        # Step 0: Outer loop, initialize min_idx
        visualizer.current_step = 0

        # Assume the first unsorted element is the minimum
        min_idx = i

        # Step 1: Set min_idx = i
        visualizer.current_step = 1

        # Inner loop: Find the actual minimum in the unsorted portion
        # Search from i+1 to end of array
        for j in range(i + 1, n):
            # Step 2: Inner loop iteration
            visualizer.current_step = 2
            # Check for pygame quit events to allow user to close window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Track number of comparisons for statistics
            visualizer.comparisons += 1

            # VISUALIZATION: Reset all bars to default color
            visualizer.color_array = [Colors.DEFAULT] * len(arr)

            # Highlight current minimum candidate in yellow
            visualizer.color_array[min_idx] = Colors.COMPARING

            # Highlight element being compared against minimum in yellow
            visualizer.color_array[j] = Colors.COMPARING

            # Keep sorted portion (elements before i) highlighted in green
            for k in range(i):
                visualizer.color_array[k] = Colors.SORTED

            # Update the display to show current comparison
            visualizer.update_display()

            # CORE LOGIC: Update minimum index if we found a smaller element
            if arr[j] < arr[min_idx]:
                # Step 3: Check condition
                visualizer.current_step = 3
                # Step 4: Update min_idx
                visualizer.current_step = 4
                min_idx = j

        # Swap the found minimum element with first unsorted element
        # Only swap if minimum is not already in correct position
        if min_idx != i:
            # Step 5: Swap elements
            visualizer.current_step = 5

            # Perform the swap
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

            # Track statistics
            visualizer.swaps += 1

            # VISUALIZATION: Highlight the swapping action in dark blue
            visualizer.color_array = [Colors.DEFAULT] * len(arr)
            visualizer.color_array[i] = Colors.SWAPPING
            visualizer.color_array[min_idx] = Colors.SWAPPING

            # Keep sorted portion highlighted
            for k in range(i):
                visualizer.color_array[k] = Colors.SORTED

            visualizer.update_display()

    # Final visualization: Mark all elements as sorted (green)
    visualizer.current_step = -1  # Reset step
    visualizer.color_array = [Colors.SORTED] * len(arr)
    visualizer.update_display()
