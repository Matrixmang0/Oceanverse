year = int(input("Enter a year : "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("The year %d is a leap year" % (year))
else:
    print("The year %d is not a leap year" % (year))
