sub1 = int(input("Enter the English mark:"))
sub2 = int(input("Enter the Science mark:"))
sub3 = int(input("Enter the math mark:"))
sub4 = int(input("Enter the Social mark:"))
sub5 = int(input("Enter the GK mark:"))

Total = (int(sub1+sub2+sub3+sub4+sub5))
print(Total,"is total mark of the student")
if (sub1>=35 and sub2>=35 and sub3>=35 and sub4>=35 and sub5>=35):
    print("PASS")
else:
    print("FAIL")
if(Total>=250):
    print("THIRD CLASS")
elif(Total>=350):
    print("Second class")
elif(Total>=450):
    print("First class")