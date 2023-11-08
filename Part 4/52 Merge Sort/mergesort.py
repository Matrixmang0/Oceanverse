def merge(li1, li2):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        li1 (list): The first sorted list.
        li2 (list): The second sorted list.

    Returns:
        list: A single sorted list containing all elements from li1 and li2.
    """
    i = 0
    j = 0
    k = 0
    nl = []  # Create an empty list to store the merged result
    while k < (len(li1) + len(li2)):
        # Compare elements from both lists and merge them in sorted order
        if i == len(li1):
            nl += li2[j:]
            k += len(li2[j:])
            j += len(li2[j:])
        elif j == len(li2):
            nl += li1[i:]
            k += len(li1[i:])
            i += len(li1[i:])
        elif li1[i] > li2[j]:
            nl.append(li2[j])
            j += 1
            k += 1
        else:
            nl.append(li1[i])
            i += 1
            k += 1
    return nl

def mergesort(lst):
    """
    Sorts a list using the Merge Sort algorithm.

    Args:
        lst (list): The unsorted list.

    Returns:
        list: A sorted list.
    """
    if len(lst) == 1:
        return lst  # Base case: If the list has only one element, it is already sorted
    mid = len(lst) // 2  # Find the midpoint of the list
    # Recursively split the list and merge the sorted sublists
    return merge(mergesort(lst[:mid]), mergesort(lst[mid:]))

li1 = [5, 67, 8, 90, 12, 123, 78]
li2 = [6, 34, 78, 11, 334, 70, 24]
li3 = list(range(50, 0, -1))

# Sort the list using the Merge Sort algorithm
sorted_li = mergesort(li3)

print(sorted_li)
