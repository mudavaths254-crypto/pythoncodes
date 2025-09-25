for number in range(1,6):
    if number==3:
        print("skipping number 3")
        continue
    print("number:",number)


 # Skip negative numbers
numbers = (3, -2, 7, -5, 10, -1)

for num in numbers:
    if num < 0:
        continue  
    print (num)