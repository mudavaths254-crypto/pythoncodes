# Get input from the user
num1 = float(input("Enter the dividend: "))
num2 = float(input("Enter the divisor: "))

if num2 != 0:
    quotient = num1 // num2
    remainder = num1 % num2
    print("Quotient:", quotient)
    print("Remainder:", remainder)
else:
    print("Error: Cannot divide by zero")