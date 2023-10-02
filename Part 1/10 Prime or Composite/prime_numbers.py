num = int(input("Enter a number : "))

flag = 0

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(num, "is a composite number")
        flag = 1
        break

if flag == 0:
    print(num, "is a prime number")
