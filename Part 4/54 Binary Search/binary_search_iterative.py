def BinarySearch(li, key):
    """
    Perform a binary search on a sorted list to find a specified key.

    Args:
        li (list): A sorted list of elements.
        key: The element to search for in the list.

    Returns:
        bool: True if the key is found in the list, False otherwise.
    """
    l = 0
    h = len(li)

    while l <= h:
        mid = (l + h) // 2
        if li[mid] == key:
            return True
        elif li[mid] > key:
            h = mid - 1
        elif li[mid] < key:
            l = mid + 1

    return False

# Sample sorted lists
li1 = sorted([5, 67, 8, 90, 12, 123, 78])
li2 = sorted([6, 34, 78, 11, 334, 70, 24])
li3 = list(range(0, 50))

# Perform binary search on a sorted list
print(BinarySearch(li1, 65))  # Example usage: Search for 65 in li1