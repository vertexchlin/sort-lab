"""
Algorithm information and complexity data
"""

ALGORITHM_INFO = {
    'Bubble Sort': {
        'description': 'Repeatedly steps through the list, compares adjacent elements and swaps them if in wrong order',
        'time_best': 'O(n)',
        'time_avg': 'O(n²)',
        'time_worst': 'O(n²)',
        'space': 'O(1)',
        'steps': [
            'for i in range(n):',
            '  for j in range(n-i-1):',
            '    if arr[j] > arr[j+1]:',
            '      swap(arr[j], arr[j+1])',
        ]
    },
    'Selection': {
        'description': 'Finds the minimum element from unsorted portion and swaps it with first unsorted element',
        'time_best': 'O(n²)',
        'time_avg': 'O(n²)',
        'time_worst': 'O(n²)',
        'space': 'O(1)',
        'steps': [
            'for i in range(n):',
            '  min_idx = i',
            '  for j in range(i+1, n):',
            '    if arr[j] < arr[min_idx]:',
            '      min_idx = j',
            '  swap(arr[i], arr[min_idx])',
        ]
    },
    'Insertion': {
        'description': 'Builds sorted array one element at a time by inserting each into its correct position',
        'time_best': 'O(n)',
        'time_avg': 'O(n²)',
        'time_worst': 'O(n²)',
        'space': 'O(1)',
        'steps': [
            'for i in range(1, n):',
            '  key = arr[i]',
            '  j = i - 1',
            '  while j >= 0 and arr[j] > key:',
            '    arr[j+1] = arr[j]',
            '    j -= 1',
            '  arr[j+1] = key',
        ]
    },
    'Merge Sort': {
        'description': 'Divides array into halves, recursively sorts them, then merges the sorted halves',
        'time_best': 'O(n log n)',
        'time_avg': 'O(n log n)',
        'time_worst': 'O(n log n)',
        'space': 'O(n)',
        'steps': [
            'if left < right:',
            '  mid = (left + right) // 2',
            '  merge_sort(arr, left, mid)',
            '  merge_sort(arr, mid+1, right)',
            '  merge(arr, left, mid, right)',
        ]
    },
    'Quick Sort': {
        'description': 'Picks a pivot, partitions array around pivot, then recursively sorts partitions',
        'time_best': 'O(n log n)',
        'time_avg': 'O(n log n)',
        'time_worst': 'O(n²)',
        'space': 'O(log n)',
        'steps': [
            'pivot = arr[high]',
            'i = low - 1',
            'for j in range(low, high):',
            '  if arr[j] < pivot:',
            '    i += 1',
            '    swap(arr[i], arr[j])',
            'swap(arr[i+1], arr[high])',
        ]
    },
    'Heap Sort': {
        'description': 'Builds a max heap, then repeatedly extracts maximum element and rebuilds heap',
        'time_best': 'O(n log n)',
        'time_avg': 'O(n log n)',
        'time_worst': 'O(n log n)',
        'space': 'O(1)',
        'steps': [
            'Build max heap',
            'for i in range(n-1, 0, -1):',
            '  swap(arr[0], arr[i])',
            '  heapify(arr, i, 0)',
        ]
    },
}
