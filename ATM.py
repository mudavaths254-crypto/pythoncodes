# ATM Withdrawal Simulation
balance = float(input("Enter your account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal > balance:
    print("Insufficient balance")
elif withdrawal % 1000 != 0:
    print("Amount must be in multiples of 1000")
else:
    balance -= withdrawal
    print("Transaction successful. Remaining balance:", balance)
