sub1 = int(input("Enter the English mark:"))
sub2 = int(input("Enter the Science mark:"))
sub3 = int(input("Enter the math mark:"))
sub4 = int(input("Enter the Social mark:"))
sub5 = int(input("Enter the GK mark:"))

Total = (int(sub1+sub2+sub3+sub4+sub5))
print(Total,"is total mark of the student")

if Total >= 400:
    print("Frist class")
elif Total >= 300:
    print("Second class")

elif Total >= 250:
    print("Third class")
else:
    print("Fail")