def write_numbers_upto(n):

  with open('output.txt', 'w') as f:
    for i in range(1, n+1):
      print(i)
      f.write(f"{i}\n")

num = 100
write_numbers_upto(num)