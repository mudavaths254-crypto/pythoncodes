# Electricity Bill Calculator
units = int(input("Enter the number of units consumed: "))

# You can change the value of rate2 as needed
rate1 = 5       
rate2 = 10 
rate3 = 100     

if units <= 100:
    bill = units * rate1
elif units <= 200:
    bill = (100 * rate1) + ((units - 100) * rate2)
else:
    bill = (100 * rate1) + (100 * rate2) + ((units - 200) * rate3)

print("Total Electricity Bill: Rs", bill)
