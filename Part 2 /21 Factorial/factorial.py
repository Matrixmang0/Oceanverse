def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter a number : "))
print("The factorial for", num, "is", factorial(num))
