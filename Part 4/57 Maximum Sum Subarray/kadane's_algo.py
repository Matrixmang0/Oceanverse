import numpy as np

def kadane_algo(array):
    """
    Find the maximum subarray sum using the Kadane's algorithm.

    Args:
        array (list): A list of integers.

    Returns:
        tuple: A tuple containing the maximum subarray sum and the subarray itself.
    """
    max_sum = -np.inf  # Initialize the maximum sum to negative infinity
    curr_sum = 0      # Initialize the current sum to 0
    start = 0         # Initialize the start index of the maximum subarray
    end = 0           # Initialize the end index of the maximum subarray

    for i in range(len(array)):
        curr_sum = max(array[i], curr_sum + array[i])

        # Update the start index if a new subarray with a higher sum is found
        if curr_sum == array[i]:
            start = i

        max_sum = max(curr_sum, max_sum)

        # Update the end index if a new maximum subarray is found
        if curr_sum == max_sum:
            end = i

    return (max_sum, array[start:end+1])

li = [-5, -43, -9, -5, -44, -54, -1, -7, 89, -6, -55]

# Apply the Kadane's algorithm to find the maximum subarray sum and subarray
(summ, sub_array) = kadane_algo(li)

print("The maximum sum is ", summ)
print("The maximum sum sub-array is ", sub_array)