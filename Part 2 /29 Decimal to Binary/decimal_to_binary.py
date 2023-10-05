num = int(input("Enter a number : "))

dec = num

binary = ""

while(dec>0):
    rem = int(dec % 2)
    binary = str(rem)+binary
    dec = (dec - rem)/2

print("The binary representation of", num, "is " + binary)


