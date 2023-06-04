print("Select Oppression")
print("For Addition press 1")
print("For Subtraction press 2")
print("For Multiplication press 3")
print("For Division press 4")

select = int (input("Select Oppression :- "))

# For Addition
if select == 1:
    num1 = int(input("Enter a number :- "))
    num2 = int(input("Enter a number :- "))
    print(num1+num2)

# For Subtraction
elif select == 2:
    num1 = int(input("Enter a number :- "))
    num2 = int(input("Enter a number :- "))
    print(num2-num1)

# For Multiplication
elif select == 3:
    num1 = int(input("Enter a number :- "))
    num2 = int(input("Enter a number :- "))
    print(num1*num2)

# For Division
elif select == 4:
    num1 = int(input("Enter a number :- "))
    num2 = int(input("Enter a number :- "))
    print(num1/num2)

else:
    print("Wrong Operation is Choosen")

