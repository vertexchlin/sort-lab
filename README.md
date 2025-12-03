# Sort Lab - Sorting Algorithm Visualizer

A Python-based interactive visualization tool for understanding various sorting algorithms through animated demonstrations.

## Features

- **6 Sorting Algorithms**:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort

- **Interactive Controls**:
  - Algorithm selection buttons
  - Speed control (faster/slower)
  - Array size adjustment (Size +/-)
  - Reset/Randomize array

- **Real-time Statistics**:
  - Comparison counter
  - Swap counter
  - Current array size
  - Animation speed

- **Visual Features**:
  - Color-coded states:
    - Blue: Unsorted elements
    - Yellow: Elements being compared
    - Red-Orange: Elements being swapped
    - Purple: Pivot element (Quick Sort)
    - Green: Sorted elements
  - Algorithm complexity information panel
  - Algorithm description

## Installation

1. Make sure you have Python 3.7+ installed

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

### Controls

1. **Select Algorithm**: Click on any algorithm button (Bubble Sort, Selection, etc.)
2. **Adjust Speed**: Click "Faster" or "Slower" to change animation speed
3. **Change Array Size**: Click "Size +" or "Size -" to increase/decrease array size
4. **Reset**: Click "Reset" to generate a new random array

## Project Structure

```
sort-lab/
├── main.py                 # Application entry point
├── algorithms/             # Sorting algorithm implementations
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── heap_sort.py
├── visualization/          # Visualization engine
│   ├── __init__.py
│   └── visualizer.py
├── utils/                  # Utilities and configuration
│   ├── __init__.py
│   ├── colors.py
│   ├── config.py
│   └── algorithm_info.py
├── requirements.txt        # Python dependencies
├── CLAUDE.md              # Algorithm documentation
└── README.md              # This file
```

## Algorithm Complexity Reference

| Algorithm      | Best Case    | Average Case | Worst Case   | Space    |
|---------------|--------------|--------------|--------------|----------|
| Bubble Sort   | O(n)         | O(n²)        | O(n²)        | O(1)     |
| Selection Sort| O(n²)        | O(n²)        | O(n²)        | O(1)     |
| Insertion Sort| O(n)         | O(n²)        | O(n²)        | O(1)     |
| Merge Sort    | O(n log n)   | O(n log n)   | O(n log n)   | O(n)     |
| Quick Sort    | O(n log n)   | O(n log n)   | O(n²)        | O(log n) |
| Heap Sort     | O(n log n)   | O(n log n)   | O(n log n)   | O(1)     |

## How It Works

Each sorting algorithm is implemented with visualization hooks that:
1. Update the color array to highlight comparisons and swaps
2. Track statistics (comparisons and swaps)
3. Call `update_display()` to refresh the screen
4. Use animation delays for smooth visualization

## Contributing

Feel free to add more sorting algorithms or enhance the visualization features!

## License

This project is open source and available for educational purposes.
