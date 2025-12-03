# Sort Lab - Sorting Algorithm Visualization Project

## Project Overview
Sort Lab is a visual demonstration project for various sorting algorithms. Each algorithm is presented with animations to help understand how the sorting process works step-by-step.

## Sorting Algorithms to Implement

### 1. Bubble Sort
**Algorithm Idea**: Repeatedly step through the list, compare adjacent elements and swap them if they are in the wrong order.

**Implementation Steps**:
1. Start at the beginning of the array
2. Compare each pair of adjacent elements
3. Swap them if they are in the wrong order
4. After each pass, the largest unsorted element "bubbles up" to its correct position
5. Repeat until no swaps are needed

**Time Complexity**: O(n²)
**Space Complexity**: O(1)

---

### 2. Selection Sort
**Algorithm Idea**: Divide the array into sorted and unsorted regions. Repeatedly find the minimum element from the unsorted region and move it to the sorted region.

**Implementation Steps**:
1. Set the first position as the current position
2. Find the minimum element in the remaining unsorted array
3. Swap the minimum element with the element at current position
4. Move to the next position
5. Repeat until the entire array is sorted

**Time Complexity**: O(n²)
**Space Complexity**: O(1)

---

### 3. Insertion Sort
**Algorithm Idea**: Build the sorted array one element at a time by inserting each element into its correct position.

**Implementation Steps**:
1. Start with the second element (consider first element as sorted)
2. Compare current element with elements in the sorted portion
3. Shift larger elements one position to the right
4. Insert the current element at the correct position
5. Repeat for all elements

**Time Complexity**: O(n²)
**Space Complexity**: O(1)

---

### 4. Merge Sort
**Algorithm Idea**: Divide the array into halves, recursively sort them, then merge the sorted halves.

**Implementation Steps**:
1. Divide the array into two halves
2. Recursively sort the left half
3. Recursively sort the right half
4. Merge the two sorted halves back together
5. Base case: array of size 1 is already sorted

**Time Complexity**: O(n log n)
**Space Complexity**: O(n)

---

### 5. Quick Sort
**Algorithm Idea**: Pick a pivot element, partition the array around the pivot, then recursively sort the partitions.

**Implementation Steps**:
1. Choose a pivot element (commonly last element, first element, or random)
2. Partition: rearrange array so elements smaller than pivot are on the left, larger on the right
3. Recursively apply quicksort to the left partition
4. Recursively apply quicksort to the right partition
5. Base case: array of size 0 or 1 is already sorted

**Time Complexity**: O(n log n) average, O(n²) worst case
**Space Complexity**: O(log n)

---

### 6. Heap Sort
**Algorithm Idea**: Build a max heap, then repeatedly extract the maximum element and rebuild the heap.

**Implementation Steps**:
1. Build a max heap from the input array
2. Swap the root (maximum element) with the last element
3. Reduce heap size by 1
4. Heapify the root to maintain max heap property
5. Repeat steps 2-4 until heap size is 1

**Time Complexity**: O(n log n)
**Space Complexity**: O(1)

---

## Project Implementation Plan

### Phase 1: Project Setup
1. Initialize project structure (HTML/CSS/JavaScript or framework of choice)
2. Set up canvas or SVG for visualization
3. Create basic UI with algorithm selector
4. Add control buttons (Start, Pause, Reset, Speed Control)

### Phase 2: Core Visualization Engine
1. Create array representation (visual bars or elements)
2. Implement color coding system:
   - Default state (unsorted)
   - Comparing elements
   - Swapping elements
   - Sorted elements
3. Add animation delay/speed control
4. Create step-by-step execution framework

### Phase 3: Algorithm Implementation
1. Implement each sorting algorithm with visualization hooks
2. Add comparisons counter
3. Add swaps/moves counter
4. Implement step-through mode for educational purposes

### Phase 4: UI/UX Enhancement
1. Add array size control
2. Add option to input custom arrays
3. Add randomize array button
4. Display algorithm complexity information
5. Add algorithm description panel

### Phase 5: Advanced Features
1. Side-by-side algorithm comparison
2. Sound effects for comparisons/swaps
3. Export animation as video/GIF
4. Code display showing current line being executed

## Animation Guidelines

### Color Scheme
The visualization uses a consistent color palette:
- **#000000** (Black) - Text and borders
- **#FFFFFF** (White) - Background
- **#005087** (Dark Blue) - UI buttons and swapping state
- **#65dcf2** (Light Cyan) - Default unsorted bars
- **#ffe564** (Light Yellow) - Comparing elements
- **#b590dc** (Light Purple) - Pivot element
- **#8edb62** (Light Green) - Sorted elements

### Visual States
- **Default**: Light cyan (#65dcf2) - unsorted bars
- **Comparing**: Light yellow (#ffe564) - elements being compared
- **Swapping**: Dark blue (#005087) - elements being swapped
- **Sorted**: Light green (#8edb62) - sorted elements
- **Pivot** (for Quick Sort): Light purple (#b590dc) - pivot element

### Animation Timing
- Default speed: 50ms per operation
- Speed range: 1ms (fast) to 500ms (slow)
- Smooth transitions using Pygame rendering

## Development Notes
- Keep sorting logic separate from visualization code
- Use async/await or Promises for step-by-step animation control
- Consider using generator functions for pausable execution
- Ensure responsive design for different screen sizes
