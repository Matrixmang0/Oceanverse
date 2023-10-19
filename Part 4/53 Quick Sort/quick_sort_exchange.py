def quicksort(li):
  if len(li)==1:
    return li
  pivot = li[0]
  i=1
  j=len(li)-1
  while(i<j):
    if li[i]>pivot and li[j]<pivot:
      (li[i], li[j]) = (li[j], li[i])
    if li[i]<pivot:
      i += 1
    if li[j]>pivot:
      j -= 1

  return (quicksort(li[1:j+1])+[pivot]+quicksort(li[j+1:]))

li1 = [5, 67, 8, 90, 12, 123, 78]
li2 = [6, 34, 78, 11, 334, 70, 24]
li3 = list(range(50, 0, -1))

print(quicksort(li1))