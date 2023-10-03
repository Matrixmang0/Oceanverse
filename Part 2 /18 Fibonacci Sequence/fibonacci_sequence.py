num = int(input("Enter a number : "))

num1 = 0
num2 = 1

fibo = []

for i in range(num):
    fibo.append(num2)
    temp = num2
    num2 += num1
    num1 = temp

print("The first", num, "fibonacci numbers are ", end="")

for i in fibo:
    print(i, end=" ")
print()
