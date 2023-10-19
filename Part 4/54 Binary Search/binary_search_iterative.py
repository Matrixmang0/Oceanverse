def BinarySearch(li, key):
  l = 0
  h = len(li)-1
  while(l<=h):
    mid = (l+h)//2
    if  li[mid]==key:
      return True
    if li[mid]>key:
      h = mid
    elif li[mid]<key:
      l = mid
  return False


li1 = sorted([5, 67, 8, 90, 12, 123, 78])
li2 = sorted([6, 34, 78, 11, 334, 70, 24])
li3 = list(range(0, 50))
print(li1)
print(BinarySearch(li1, 75))
