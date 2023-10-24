def adaptive_bubble_sort(array):

  for i in range(len(array)-1):
    flag = 0
    for j in range(len(array)-1-i):
      if array[j] > array[j+1] :
        (array[j], array[j+1]) = (array[j+1], array[j])
        flag=1
    if flag==0:
      break

  return array

li1 = [5, 67, 8, 90, 12, 123, 78]
li2 = [6, 34, 78, 11, 334, 70, 24]
li3 = list(range(50, 0, -1))

print(adaptive_bubble_sort(li3))