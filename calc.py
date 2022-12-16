num1 = int(input("Enter the value1:"))
num2 = int(input("Enter the value2:"))

opr = input("Enter the operator:")

if opr == "+" :
    print(num1+num2, "Added")
elif opr=="-":
    print(num1-num2, "Subtracted")
elif opr=="*":
    print(num1*num2, "Multiplied")
elif opr=="/":
    print(num1/num2, "Divided")
