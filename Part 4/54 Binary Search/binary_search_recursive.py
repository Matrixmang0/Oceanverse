def BinarySearch(li, key):
  if len(li)==1:
    if li[0]==key:
      return True
    else:
      return False
  
  mid = len(li)//2

  if li[mid]==key:
    return True
  elif li[mid]>key:
    return BinarySearch(li[:mid], key)
  else:
    return BinarySearch(li[mid:], key)
  
li1 = sorted([5, 67, 8, 90, 12, 123, 78])
li2 = sorted([6, 34, 78, 11, 334, 70, 24])
li3 = list(range(0, 50))

print(BinarySearch(li1, 50))