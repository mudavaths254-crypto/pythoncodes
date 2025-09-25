# sum of prime number from  100 to 500 
total = 0
for num in range(100, 501):
    if num > 1:  
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break   
            if is_prime:
                total += num    
print("Sum of prime numbers from 100 to 500 is:", total)    
