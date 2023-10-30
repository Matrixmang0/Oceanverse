import numpy as np

def kadane_algo(array):

  max_sum = -np.inf
  curr_sum = 0
  start = 0
  end = 0
  for i in range(len(array)):
    curr_sum = max(array[i], curr_sum + array[i])
    if curr_sum==array[i]:
      start = i
    max_sum = max(curr_sum, max_sum)
    if curr_sum==max_sum:
      end = i

  return (max_sum, array[start:end+1])


li = [-5, -43, -9, -5, -44, -54, -1, -7, 89, -6, -55]

(summ, sub_array) = kadane_algo(li)

print("The maximum sum is ", summ)
print("The maximum sum sub-array is ", sub_array)