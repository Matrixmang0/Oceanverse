vowels = "aeiouAEIOU"

string = input("Enter a string : ")

vow = 0
con = 0

for char in string:
    if char in vowels:
        vow += 1
    else:
        con += 1

print("Vowels     : ", vow)
print("Consonants : ", con)
