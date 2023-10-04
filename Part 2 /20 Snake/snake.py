import numpy as np

lines = int(input("Enter the number of lines : "))
curv = float(input("Enter the curvature : "))

y = np.linspace(-lines // 2, lines // 2, lines)
x = curv * (y**2)
x = x - min(x)

for i in range(lines):
    for j in range(int(x[i])):
        print(" ", end="")
    print("*")
