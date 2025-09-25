# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Addition  
add = num1 + num2
print("Addition:", add)

# Subtraction
sub = num1 - num2
print("Subtraction:", sub)

# Multiplication
mul = num1 * num2
print("Multiplication:", mul)

# Division
if num2 != 0:
    div = num1 / num2
    print("Division:", div)
else:
    print("Division: Cannot divide by zero")