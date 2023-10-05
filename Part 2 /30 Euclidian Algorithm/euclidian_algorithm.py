def fibonacci_k(k):
  num1 = 0
  num2 = 1

  li = [num2]
  
  while(str(num2<=k)):
    temp = num2
    num2 += num1
    num1 = temp
    if (str(num2<=k)):
      li.append(num2)

  return li


def euclid_gcd(m, n):
  if (n > m):
    (m, n) = (n, m)
  steps = 0
  while(n > 0):
    temp = m%n
    m = n
    n = temp
    if (n > m):
      (m, n) = (n, m)
    steps += 1
  return (m, steps)

print(fibonacci_k(1)) 
