num = int(input("Enter a number : "))

sqr_list = []

for i in range(1, num + 1):
    sqr_list.append(i * i)

print("The list of squares upto", num, "are ", end="")

for sqrs in sqr_list:
    print(sqrs, end=" ")
print()
