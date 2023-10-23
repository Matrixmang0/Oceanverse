def merge(li1, li2):
  i = 0
  j = 0
  k = 0
  nl = []
  while (k<(len(li1)+len(li2))):
    if i==(len(li1)):
      nl += li2[j:]
      k += len(li2[j:])
      j += len(li2[j:])
    elif j==(len(li2)):
      nl += li1[i:]
      k += len(li1[i:])
      i += len(li1[i:])
    elif li1[i]>li2[j]:
      nl.append(li2[j])
      j += 1
      k += 1
    else:
      nl.append(li1[i])
      i += 1
      k += 1
  return nl

def mergesort(lst):
  if len(lst)==1:
    return lst
  mid = len(lst)//2
  return merge(mergesort(lst[:mid]), mergesort(lst[mid:]))

li1 = [5, 67, 8, 90, 12, 123, 78]
li2 = [6, 34, 78, 11, 334, 70, 24]
li3 = list(range(50, 0, -1))

print(mergesort(li3))