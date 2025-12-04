"""
Algorithm information and complexity data
"""

ALGORITHM_INFO = {
    'Bubble Sort': {
        'description': 'Like bubbles rising: largest elements "bubble up" to the end. Compares neighbors and swaps if wrong order.',
        'analogy': '🎈 Bubbles in water - biggest rise to top first!',
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
        'description': 'Picks the smallest from unsorted items and moves it to sorted section. Repeats until done.',
        'analogy': '🎯 Picking tallest players first for basketball team!',
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
        'description': 'Like sorting cards in your hand - pick each card and insert it in the right spot among sorted cards.',
        'analogy': '🃏 Organizing playing cards in your hand one by one!',
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
        'description': 'Divide into small pieces, sort each piece, then merge back together. Like organizing paper stacks.',
        'analogy': '📚 Split papers into tiny piles, sort each, merge into one sorted stack!',
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
        'description': 'Pick a "pivot", put smaller items left, larger items right. Repeat for each side until sorted.',
        'analogy': '🎯 Party organizer: pick medium height, shorter left, taller right!',
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
        'description': 'Build a "heap" (tree where parent > children). Keep removing the top (max) and rebuild until done.',
        'analogy': '🏔️ Mountain peak is always highest - keep removing peak, rebuild mountain!',
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
