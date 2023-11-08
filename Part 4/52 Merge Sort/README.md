# Merge Sort Algorithm

## Introduction

Merge Sort is a popular and efficient sorting algorithm used to sort a list of elements. This tutorial provides an overview of how Merge Sort works and how to implement it in Python.

## How Merge Sort Works

Merge Sort is a divide-and-conquer sorting algorithm. It operates by dividing the unsorted list into smaller sublists, sorting those sublists, and merging them back into a single sorted list. The key steps are as follows:

### Divide

1. Start with an unsorted list.
2. Divide the list into smaller sublists until each sublist contains only one element. These single-element sublists are considered sorted.

### Conquer

3. Merge the sorted sublists by combining two sublists at a time. Continue this process until a single sorted list is achieved.

## Example

Let's use a simple example to demonstrate Merge Sort:

Suppose we have an unsorted list: `[5, 67, 8, 90, 12, 123, 78]`

1. Divide the list into smaller sublists:

   - `[5, 67, 8]`, `[90, 12, 123, 78]`

2. Sort the sublists (Conquer):

   - `[5, 8, 67]`, `[12, 78, 90, 123]`

3. Merge the sorted sublists to create the final sorted list:
   - `[5, 8, 12, 67, 78, 90, 123]`

The result is a fully sorted list.

## Time Complexity

Merge Sort is known for its consistent time complexity of O(n log n), making it an efficient choice for sorting large datasets. It is a stable and reliable sorting algorithm.

## Usage

1. Open the script in your preferred Python environment or editor.

2. Modify the `li3` list or replace it with your own list of elements that you want to sort.

3. Run the script. The sorted list will be displayed in the console.

```python
li = list(range(50, 0, -1))
sorted_li = mergesort(li)
print(sorted_li)
```
