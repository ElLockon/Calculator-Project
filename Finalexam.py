# Jesus Liriano
# Basic Calculator
# Michael Penta
# May 8, 2020

# So first we need to get the numbers and operator from the user
# We use float to get decimal numbers to work in our calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator")
num2 = float(input("Enter second number"))

# After this we need and if statement to know what we do with the numbers

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)

# If the user enters anything other than the signs above he will get an error
else:
    print("Invalid operator")
