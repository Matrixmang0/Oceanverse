def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number : "))

print("The prime numbers upto", num, "are", end=" ")

for i in range(2, num + 1):
    if is_prime(i):
        print(i, end=" ")

print()
