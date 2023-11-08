def adaptive_bubble_sort(array):
    """
    Sorts a given list using the adaptive version of the Bubble Sort algorithm.

    Args:
        array (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(len(array) - 1):
        flag = 0  # Initialize a flag to track whether any swaps were made in this pass
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                # Swap elements if they are in the wrong order
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = 1  # Set the flag to 1, indicating a swap occurred in this pass
        if flag == 0:
            # If no swaps were made in this pass, the list is already sorted
            break

    return array

li1 = [5, 67, 8, 90, 12, 123, 78]
li2 = [6, 34, 78, 11, 334, 70, 24]
li3 = list(range(50, 0, -1))

# Sort the list using the adaptive bubble sort
sorted_li = adaptive_bubble_sort(li3)

print(sorted_li)