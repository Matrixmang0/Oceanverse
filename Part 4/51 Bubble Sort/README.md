# Bubble Sort Algorithm

## Introduction

Bubble Sort is a simple and intuitive sorting algorithm that is often used for educational purposes and understanding sorting algorithms. This tutorial provides an overview of how Bubble Sort works and how to implement it.

## How Bubble Sort Works

Bubble Sort works by repeatedly comparing adjacent elements in a list and swapping them if they are in the wrong order. The process is repeated until no swaps are needed, indicating that the list is sorted.

### Step-by-Step Process

1. Start with the first element (index 0) and compare it with the next element (index 1).
2. If the first element is greater than the second element, swap them.
3. Move to the next pair of elements (index 1 and index 2) and repeat the comparison and swapping process.
4. Continue this process for the entire list, comparing and swapping adjacent elements until you reach the end of the list.
5. After one pass through the list, the largest element will have "bubbled up" to the end.
6. Repeat the process for the entire list again, excluding the last element (which is already in its correct position).
7. Continue these passes through the list until no more swaps are needed.

## Example

Let's use a simple example to demonstrate Bubble Sort:

Suppose we have an unsorted list: `[5, 3, 1, 4, 2]`

1. First pass:

   - Compare 5 and 3. Swap to get: `[3, 5, 1, 4, 2]`
   - Compare 5 and 1. Swap to get: `[3, 1, 5, 4, 2]`
   - Compare 5 and 4. Swap to get: `[3, 1, 4, 5, 2]`
   - Compare 5 and 2. Swap to get: `[3, 1, 4, 2, 5]`

   After the first pass, the largest element (5) is in its correct position at the end of the list.

2. Second pass:

   - Compare 3 and 1. Swap to get: `[1, 3, 4, 2, 5]`
   - Compare 3 and 4. No swap needed.
   - Compare 4 and 2. Swap to get: `[1, 3, 2, 4, 5]`

   After the second pass, the second-largest element (4) is in its correct position.

3. Continue the passes until no swaps are needed. In this case, after the third pass, the list is sorted.

## Time Complexity

Bubble Sort has a time complexity of O(n^2) in the worst case, making it less efficient for large datasets. However, it is a simple sorting algorithm and easy to understand and implement.

Bubble Sort is primarily used for educational purposes and understanding sorting algorithms. For practical purposes, consider using built-in sorting functions or more advanced sorting algorithms.
