def fibonacci(n):
  a = 0
  b = 1
  for i in range(n-1):
    temp = b
    b = b+a
    a = temp

  return b

print(fibonacci(5))
print(fibonacci(1))
print(fibonacci(2))