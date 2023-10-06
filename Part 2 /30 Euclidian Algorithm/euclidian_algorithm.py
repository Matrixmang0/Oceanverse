def euclids_algo(a, b, steps=0):

  if (b>a):
    (a, b) = (b, a)
  if (b==0):
    return (a,steps)
  else:
    return euclids_algo(b, a%b, steps+1)
  
def seq_fibo(k):

  num1 = 0
  num2 = 1

  li = []

  while(1):
    if (len(str(num1))==k) and (len(str(num2))==k):
      li = [num1, num2]
    elif (len(str(num1))==k) and (len(str(num2))==k+1):
      return li
    
    temp = num1
    num1 = num2
    num2 += temp

k = int(input("Enter the number of digits : "))  

dig1, dig2 = seq_fibo(k)[0], seq_fibo(k)[1]

(gcd, steps) = euclids_algo(dig1, dig2)

print("The two digits of length k are "+str(dig1)+" and "+str(dig2))
print("Their GCD is", gcd,"and number of steps taken is", steps)
  
