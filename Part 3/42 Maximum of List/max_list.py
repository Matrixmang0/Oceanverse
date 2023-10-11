def find_max(li):

  maxi = li[0]

  for i in range(1, len(li)):
    if li[i]>maxi:
      maxi = li[i]
  
  return maxi

l1 = [4, 6, 7, 3, 76, 234, 769, 12]
l2 = [8, 54, 78, 4, 12, 15, 65, 87]

print(find_max(l1))
print(find_max(l2))