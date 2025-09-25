num=int(input("Enter a number: "))#num=13
count=0
for i in range(1,num+1):
    if (num%i==0):#13%1==0,13%2==0,13%3==0,13%3==0
        count=count+1#count=1,count=2

if(count==2):
    print("the given number is prime number")
else:
    print("the given number is not a prime number")
    