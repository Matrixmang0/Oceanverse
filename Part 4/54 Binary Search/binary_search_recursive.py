def BinarySearch(li, key):
    """
    Perform a binary search on a sorted list to find a specified key using a recursive approach.

    Args:
        li (list): A sorted list of elements.
        key: The element to search for in the list.

    Returns:
        bool: True if the key is found in the list, False otherwise.
    """
    if len(li) == 1:
        if li[0] == key:
            return True
        else:
            return False

    mid = len(li) // 2

    if li[mid] == key:
        return True
    elif li[mid] > key:
        return BinarySearch(li[:mid], key)
    else:
        return BinarySearch(li[mid:], key)

# Sample sorted lists
li1 = sorted([5, 67, 8, 90, 12, 123, 78])
li2 = sorted([6, 34, 78, 11, 334, 70, 24])
li3 = list(range(0, 50))

# Perform binary search on a sorted list
print(BinarySearch(li1, 50))  # Example usage: Search for 50 in li1