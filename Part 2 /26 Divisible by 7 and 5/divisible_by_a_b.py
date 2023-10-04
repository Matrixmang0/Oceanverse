num = int(input("Enter a number : "))
a = int(input("Enter a number 'a' : "))
b = int(input("Enter another number 'b' : "))

if (num % a == 0) and (num % b == 0):
    print("The number %d is divisible by both %d and %d" % (num, a, b))
elif num % a == 0:
    print("The number %d is only divisible by %d" % (num, a))
elif num % b == 0:
    print("The number %d is only divisible by %d" % (num, b))
else:
    print("The number %d is neither divisible by %d nor %d" % (num, a, b))
