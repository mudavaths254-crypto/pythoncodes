for number in range(1,10):
    if number==5:
        print("breaking the loop at number 5")
        break
    print("number:",number) 

numbers=[1,3,7,10,5,8]

for num in numbers:
    if num % 2 == 0:
        print("First even number found:",num)
        break

else:
    print("no even number found")
                                                                            

