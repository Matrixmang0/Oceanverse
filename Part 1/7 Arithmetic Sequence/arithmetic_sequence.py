a = int(input("Enter a value for a: "))
d = int(input("Enter a value for d: "))
b = int(input("Enter a value for b: "))

print("Output: ", end="")

for i in range(a, b, d):
    print(i, end=" ")
print()
