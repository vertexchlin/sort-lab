"""
Insertion Sort Algorithm Implementation
Time Complexity: O(n²) - Worst case when array is reverse sorted, O(n) for nearly sorted
Space Complexity: O(1) - Only uses a constant amount of extra space

How it works:
- Builds sorted array one element at a time (like sorting playing cards)
- Takes each element and inserts it into correct position in sorted portion
- Shifts larger elements to the right to make room
- Very efficient for small or nearly sorted arrays
"""

import pygame
from utils.colors import Colors

def insertion_sort(visualizer):
    """
    Insertion Sort: Build the sorted array one element at a time
    by inserting each element into its correct position.

    Args:
        visualizer: The Visualizer object containing the array and display methods
    """
    # Get reference to the array we're sorting
    arr = visualizer.array
    n = len(arr)

    # Start from index 1 (assume first element is already sorted)
    # Each iteration inserts arr[i] into the correct position in sorted portion
    for i in range(1, n):
        # Step 0: Outer loop iteration
        visualizer.current_step = 0

        # Step 1: Store key value
        visualizer.current_step = 1

        # Store the current element to be inserted (the "key")
        key = arr[i]

        # Step 2: Initialize j
        visualizer.current_step = 2

        # Start comparing with element to the left
        j = i - 1

        # Check for pygame quit events to allow user to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # CORE LOGIC: Shift elements greater than key to the right
        # Continue moving left while we find elements larger than key
        while j >= 0 and arr[j] > key:
            # Step 3: While loop condition check
            visualizer.current_step = 3
            # Track number of comparisons for statistics
            visualizer.comparisons += 1

            # VISUALIZATION: Reset all bars to default color
            visualizer.color_array = [Colors.DEFAULT] * len(arr)

            # Highlight element being compared in yellow
            visualizer.color_array[j] = Colors.COMPARING

            # Highlight position where key will be inserted in dark blue
            visualizer.color_array[j + 1] = Colors.SWAPPING

            # Mark sorted portion in green (except current comparison)
            for k in range(i):
                if k != j and k != j + 1:
                    visualizer.color_array[k] = Colors.SORTED

            # Update the display to show current shift
            visualizer.update_display()

            # Step 4: Shift element
            visualizer.current_step = 4

            # Shift the larger element one position to the right
            arr[j + 1] = arr[j]

            # Track statistics (treating shifts as swaps)
            visualizer.swaps += 1

            # Step 5: Decrement j
            visualizer.current_step = 5

            # Move to next element on the left
            j -= 1

        # Step 6: Insert key at correct position
        visualizer.current_step = 6

        # Insert the key into its correct position
        # j+1 is the correct position (j went one position too far left)
        arr[j + 1] = key

        # VISUALIZATION: Show the newly expanded sorted portion
        visualizer.color_array = [Colors.DEFAULT] * len(arr)

        # All elements from 0 to i are now sorted
        for k in range(i + 1):
            visualizer.color_array[k] = Colors.SORTED

        visualizer.update_display()

    # Final visualization: Mark all elements as sorted (green)
    visualizer.current_step = -1  # Reset step
    visualizer.color_array = [Colors.SORTED] * len(arr)
    visualizer.update_display()
