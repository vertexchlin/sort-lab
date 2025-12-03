"""
Merge Sort Algorithm Implementation
Time Complexity: O(n log n) - Consistent performance regardless of input
Space Complexity: O(n) - Requires additional space for temporary arrays

How it works:
- Divide and Conquer approach
- Recursively divides array into halves until single elements
- Merges sorted subarrays back together in sorted order
- Guarantees O(n log n) performance, stable sort
"""

import pygame
from utils.colors import Colors

def merge_sort(visualizer):
    """
    Merge Sort: Divide the array into halves, recursively sort them,
    then merge the sorted halves.

    Args:
        visualizer: The Visualizer object containing the array and display methods
    """

    def merge(arr, left, mid, right):
        """
        Merge two sorted subarrays into one sorted subarray.

        Args:
            arr: The main array
            left: Starting index of left subarray
            mid: Ending index of left subarray
            right: Ending index of right subarray
        """
        # Create temporary copies of the two subarrays
        # Left subarray: arr[left...mid]
        # Right subarray: arr[mid+1...right]
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]

        # Initialize pointers for left_arr, right_arr, and main array
        i = 0  # Pointer for left_arr
        j = 0  # Pointer for right_arr
        k = left  # Pointer for main array (starting at left index)

        # CORE LOGIC: Merge the two sorted arrays
        # Compare elements from both arrays and place smaller one in main array
        while i < len(left_arr) and j < len(right_arr):
            # Check for pygame quit events to allow user to close window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Track number of comparisons for statistics
            visualizer.comparisons += 1

            # VISUALIZATION: Highlight position where we're placing merged element
            visualizer.color_array = [Colors.DEFAULT] * len(arr)
            visualizer.color_array[k] = Colors.COMPARING

            visualizer.update_display()

            # Step 4: Merge comparison and placement
            visualizer.current_step = 4

            # Compare and select smaller element
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1

            # Track statistics (counting placements as swaps for visualization)
            visualizer.swaps += 1

            # VISUALIZATION: Highlight the placement in dark blue
            visualizer.color_array[k] = Colors.SWAPPING
            visualizer.update_display()
            k += 1

        # Copy any remaining elements from left subarray (if any)
        while i < len(left_arr):
            arr[k] = left_arr[i]
            visualizer.color_array[k] = Colors.SWAPPING
            visualizer.update_display()
            i += 1
            k += 1

        # Copy any remaining elements from right subarray (if any)
        while j < len(right_arr):
            arr[k] = right_arr[j]
            visualizer.color_array[k] = Colors.SWAPPING
            visualizer.update_display()
            j += 1
            k += 1

    def merge_sort_helper(arr, left, right):
        """
        Recursive helper function for merge sort.

        Args:
            arr: The array to sort
            left: Left boundary of current subarray
            right: Right boundary of current subarray
        """
        # Base case: If left >= right, subarray has 0 or 1 element (already sorted)
        if left < right:
            # Step 0: Check condition
            visualizer.current_step = 0

            # Step 1: Calculate mid point
            visualizer.current_step = 1

            # Find the middle point to divide array into two halves
            mid = (left + right) // 2

            # Step 2: Recursively sort left half
            visualizer.current_step = 2

            # DIVIDE: Recursively sort first half
            merge_sort_helper(arr, left, mid)

            # Step 3: Recursively sort right half
            visualizer.current_step = 3

            # DIVIDE: Recursively sort second half
            merge_sort_helper(arr, mid + 1, right)

            # CONQUER: Merge the two sorted halves
            merge(arr, left, mid, right)

    # Get reference to the array we're sorting
    arr = visualizer.array

    # Start the recursive merge sort process
    merge_sort_helper(arr, 0, len(arr) - 1)

    # Final visualization: Mark all elements as sorted (green)
    visualizer.current_step = -1  # Reset step
    visualizer.color_array = [Colors.SORTED] * len(arr)
    visualizer.update_display()
