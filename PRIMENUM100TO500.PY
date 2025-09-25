# 100 to 500 prime numbers 
for num in range(100, 501):
    if num > 1:  # prime numbers are greater than 1
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)  
            
         
   