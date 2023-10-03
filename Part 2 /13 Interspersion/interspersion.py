print("Enter two strings of equal length")

str1 = input("String 1 : ")
str2 = input("String 2 : ")

while len(str1) != len(str2):
    print("The strings are not equal in length, reenter the strings")
    str1 = input("String 1 : ")
    str2 = input("String 2 : ")

newstr = ""

for i in range(len(str1)):
    newstr += str1[i] + str2[i]

print("The interspersed string is " + newstr)
