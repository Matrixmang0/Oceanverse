num = int(input("Enter a number : "))

if (num % 5 == 0) and (num % 7 == 0):
    print("The number %d is divisible by both 5 and 7" % num)
elif num % 5 == 0:
    print("The number %d is only divisible by 5" % num)
elif num % 7 == 0:
    print("The number %d is only divisible by 7" % num)
else:
    print("The number %d is neither divisible by 5 nor 7" % num)
