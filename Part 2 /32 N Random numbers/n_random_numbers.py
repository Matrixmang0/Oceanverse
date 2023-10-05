import random

length = int(input("Length of the list : "))

li = [random.randint(1, 1001) for i in range(length)]

print(li)