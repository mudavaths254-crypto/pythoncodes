#1 write a program to take two numbers as input and perform all arithmetic operations

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

#2 swap two variable using assignment operators (+= , -=)without using a third variable

a = 5
b = 10

a += b  # a = a + b
b = a - b  # b = (a + b) - b = a
a -= b  # a = (a + b) - a = b

print("a:", a)
print("b:", b)


#3 write a program that check whether two numbers are equa
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
	print("The numbers are equal.")
else:
	print("The numbers are not equal.")


#4 writr a program to reverse an array without using slicing
arr = []
n = int(input("Enter number of elements in array: "))
for i in range(n):
	arr.append(int(input(f"Enter element {i+1}: ")))

for i in range(n // 2): # Reverse array without slicing
	arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print("Reversed array:", arr)


#5 find the sum and average of array elements 

arr = [10, 20, 30, 40, 50]  # Example array

total = sum(arr)
average = total / len(arr)

print("Sum:", total)
print("Average:", average)


#6 reshape a numpy array from 1d to 2d
import numpy as np
array_1d = np.array([1, 2, 3, 4, 5, 6])
array_2d = array_1d.reshape((2, 3))  # Reshape to 2 rows, 3 columns
print("Original 1D array:", array_1d)
print("Reshaped 2D array:\n", array_2d)


#7 multiply two matrices using numpy
import numpy as np
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Product of matrices:\n", result)
