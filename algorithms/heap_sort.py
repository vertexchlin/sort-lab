"""
Heap Sort Algorithm Implementation
Time Complexity: O(n log n) - Consistent performance regardless of input
Space Complexity: O(1) - Sorts in place, no extra array needed

How it works:
- Uses binary heap data structure (max heap)
- First builds a max heap from the array
- Repeatedly extracts maximum element (root) and rebuilds heap
- Guarantees O(n log n) performance, not stable
- Efficient memory usage (in-place sorting)
"""

import pygame
from utils.colors import Colors

def heap_sort(visualizer):
    """
    Heap Sort: Build a max heap, then repeatedly extract the maximum element
    and rebuild the heap.

    Args:
        visualizer: The Visualizer object containing the array and display methods
    """

    def heapify(arr, n, i):
        """
        Heapify subtree rooted at index i.
        Ensures the subtree satisfies max heap property:
        - Parent node is greater than or equal to its children

        Args:
            arr: The array representing the heap
            n: Size of heap (number of elements to consider)
            i: Index of root node of subtree to heapify
        """
        # Assume current node i is the largest
        largest = i

        # In a binary heap represented as array:
        # Left child of node i is at index 2*i + 1
        # Right child of node i is at index 2*i + 2
        left = 2 * i + 1
        right = 2 * i + 2

        # Check for pygame quit events to allow user to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # VISUALIZATION: Highlight current node and its children
        visualizer.color_array = [Colors.DEFAULT] * len(arr)
        visualizer.color_array[i] = Colors.COMPARING

        # Highlight left child if it exists
        if left < n:
            visualizer.color_array[left] = Colors.COMPARING

        # Highlight right child if it exists
        if right < n:
            visualizer.color_array[right] = Colors.COMPARING

        visualizer.update_display()

        # CORE LOGIC: Find largest among root, left child, and right child

        # Check if left child exists and is greater than root
        if left < n:
            visualizer.comparisons += 1
            if arr[left] > arr[largest]:
                largest = left

        # Check if right child exists and is greater than current largest
        if right < n:
            visualizer.comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        # If largest is not root, swap and recursively heapify affected subtree
        if largest != i:
            # Swap root with largest child
            arr[i], arr[largest] = arr[largest], arr[i]
            visualizer.swaps += 1

            # VISUALIZATION: Highlight the swap in dark blue
            visualizer.color_array[i] = Colors.SWAPPING
            visualizer.color_array[largest] = Colors.SWAPPING
            visualizer.update_display()

            # Recursively heapify the affected subtree
            # The subtree rooted at 'largest' may now violate heap property
            heapify(arr, n, largest)

    # Get reference to the array we're sorting
    arr = visualizer.array
    n = len(arr)

    # Step 0: Build max heap phase
    visualizer.current_step = 0

    # PHASE 1: BUILD MAX HEAP
    # Start from last non-leaf node and heapify each node
    # Last non-leaf node is at index (n//2 - 1)
    # Work backwards to root, ensuring heap property
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # PHASE 2: EXTRACT ELEMENTS FROM HEAP ONE BY ONE
    # After building heap, root (arr[0]) contains maximum element
    for i in range(n - 1, 0, -1):
        # Step 1: Extract phase - loop iteration
        visualizer.current_step = 1

        # Step 2: Swap root with last element
        visualizer.current_step = 2

        # Move current maximum (root) to end of array
        # This places largest unsorted element in its final position
        arr[0], arr[i] = arr[i], arr[0]
        visualizer.swaps += 1

        # VISUALIZATION: Show swap and mark element as sorted
        visualizer.color_array = [Colors.DEFAULT] * len(arr)
        visualizer.color_array[0] = Colors.SWAPPING  # Root being moved
        visualizer.color_array[i] = Colors.SORTED    # Now in final position
        visualizer.update_display()

        # Step 3: Heapify the reduced heap
        visualizer.current_step = 3

        # Heapify the reduced heap (excluding sorted elements at end)
        # This bubbles new root down to maintain heap property
        heapify(arr, i, 0)

    # Final visualization: Mark all elements as sorted (green)
    visualizer.current_step = -1  # Reset step
    visualizer.color_array = [Colors.SORTED] * len(arr)
    visualizer.update_display()
