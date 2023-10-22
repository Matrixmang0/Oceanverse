def quicksort(li):
  if len(li)==1 or len(li)==0:
    return li
  pivot = li[0]
  left = []
  right = []

  for i in li[1:]:
    if i>pivot:
      right.append(i)
    else:
      left.append(i)

  return (quicksort(left)+[pivot]+quicksort(right))

li1 = [5, 67, 8, 90, 12, 123, 78]
li2 = [6, 34, 78, 11, 334, 70, 24]
li3 = list(range(50, 0, -1))

print(quicksort(li3))