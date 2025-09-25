# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))
if (side1==side2) and (side2==side3):
    print("The triangle is equilateral triangle")
elif (side1==side2) or (side2==side3) or (side1==side3):
    print("The triangle is isoscele triangle")     
else:
    print("The triangle is scalen triangle")