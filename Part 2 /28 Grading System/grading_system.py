sub1 = int(input("Enter the marks in first subject : "))
sub2 = int(input("Enter the marks in second subject : "))
sub3 = int(input("Enter the marks in third subject : "))
sub4 = int(input("Enter the marks in fourth subject : "))
sub5 = int(input("Enter the marks in fifth subject : "))

avg_marks = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if avg_marks >= 90:
    print("The grade is A")
elif avg_marks >= 80:
    print("The grade is B")
elif avg_marks >= 70:
    print("The grade is C")
elif avg_marks >= 60:
    print("The grade is D")
else:
    print("The grade is F")
