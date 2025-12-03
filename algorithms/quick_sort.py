"""
Quick Sort Algorithm Implementation
Time Complexity: O(n log n) average case, O(n²) worst case (rare with good pivot selection)
Space Complexity: O(log n) - For the recursion call stack

How it works:
- Divide and Conquer approach
- Selects a 'pivot' element
- Partitions array so elements < pivot are on left, elements > pivot are on right
- Recursively sorts the partitions
- Very efficient in practice, often faster than merge sort
"""

import pygame
from utils.colors import Colors

def quick_sort(visualizer):
    """
    Quick Sort: Pick a pivot element, partition the array around the pivot,
    then recursively sort the partitions.

    Args:
        visualizer: The Visualizer object containing the array and display methods
    """

    def partition(arr, low, high):
        """
        Partition the array around a pivot element.
        Places pivot in correct position and ensures:
        - All elements < pivot are to its left
        - All elements > pivot are to its right

        Args:
            arr: The array to partition
            low: Starting index of partition range
            high: Ending index of partition range

        Returns:
            Final position of pivot element
        """
        # Step 0: Choose pivot
        visualizer.current_step = 0

        # Choose the last element as pivot (other strategies: first, middle, random)
        pivot = arr[high]

        # Step 1: Initialize i
        visualizer.current_step = 1

        # i tracks the position where next smaller element should go
        # Start at low - 1 (before the partition)
        i = low - 1

        # VISUALIZATION: Highlight the pivot in purple
        visualizer.color_array = [Colors.DEFAULT] * len(arr)
        visualizer.color_array[high] = Colors.PIVOT
        visualizer.update_display()

        # CORE LOGIC: Partition elements around pivot
        # Scan through array from low to high-1
        for j in range(low, high):
            # Step 2: Loop through array
            visualizer.current_step = 2
            # Check for pygame quit events to allow user to close window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return i + 1

            # Track number of comparisons for statistics
            visualizer.comparisons += 1

            # VISUALIZATION: Highlight current element being compared with pivot
            visualizer.color_array = [Colors.DEFAULT] * len(arr)
            visualizer.color_array[high] = Colors.PIVOT  # Keep pivot highlighted
            visualizer.color_array[j] = Colors.COMPARING

            visualizer.update_display()

            # If current element is smaller than pivot
            if arr[j] < pivot:
                # Step 3: Check if element < pivot
                visualizer.current_step = 3

                # Step 4: Increment i
                visualizer.current_step = 4

                # Move boundary of smaller elements forward
                i += 1

                # Step 5: Swap elements
                visualizer.current_step = 5

                # Swap current element with element at boundary
                arr[i], arr[j] = arr[j], arr[i]
                visualizer.swaps += 1

                # VISUALIZATION: Highlight the swap in dark blue
                visualizer.color_array[i] = Colors.SWAPPING
                visualizer.color_array[j] = Colors.SWAPPING
                visualizer.update_display()

        # Step 6: Swap pivot to correct position
        visualizer.current_step = 6

        # Place pivot in its correct position
        # Swap pivot with element at i+1 (first element larger than pivot)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        visualizer.swaps += 1

        # VISUALIZATION: Mark pivot as sorted (it's now in correct final position)
        visualizer.color_array = [Colors.DEFAULT] * len(arr)
        visualizer.color_array[i + 1] = Colors.SORTED
        visualizer.update_display()

        # Return the partition index (pivot's final position)
        return i + 1

    def quick_sort_helper(arr, low, high):
        """
        Recursive helper function for quick sort.

        Args:
            arr: The array to sort
            low: Starting index of range to sort
            high: Ending index of range to sort
        """
        # Base case: If low >= high, subarray has 0 or 1 element (already sorted)
        if low < high:
            # PARTITION: Find pivot position such that:
            # - Elements < pivot are before it
            # - Elements > pivot are after it
            pi = partition(arr, low, high)

            # DIVIDE: Recursively sort elements before pivot
            quick_sort_helper(arr, low, pi - 1)

            # DIVIDE: Recursively sort elements after pivot
            quick_sort_helper(arr, pi + 1, high)

    # Get reference to the array we're sorting
    arr = visualizer.array

    # Start the recursive quick sort process
    quick_sort_helper(arr, 0, len(arr) - 1)

    # Final visualization: Mark all elements as sorted (green)
    visualizer.current_step = -1  # Reset step
    visualizer.color_array = [Colors.SORTED] * len(arr)
    visualizer.update_display()
