n = int(input("enter how many terms: "))

a, b = 0, 1

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
 

