num_1 = int(input("Enter the number:"))
num_2 = int(input("Enter the another number:"))
choice = input( "Enter the operation + - * /:")
if choice == "+":
    sum = num_1 + num_2
    print ("The sum of numbers is",sum)

if choice == "-":
    diff = num_1 - num_2
    print("The difference is",diff)

if choice =="*":
    mul = num_1 * num_2
    print( "The multiply is" ,mul)

if choice =="/":
    div = num_1 / num_2
    print( "The division is",div)

else:
    print("Invalid operation")