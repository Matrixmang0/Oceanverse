num = int(input("Enter a number : "))

print("Multiplication Table for", num)

for i in range(1, 11):
    print("%dX%d=%d" % (num, i, (num * i)))
