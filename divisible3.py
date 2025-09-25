# Program to check divisibility by 3 and 5 using logical operators (&, /)
num = int(input("Enter a number: "))

# Using bitwise AND (&) and division (/)
if (num % 3 == 0) & (num % 5 == 0):
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")