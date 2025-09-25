# Program to classify marks
marks = float(input("Enter your marks (0-100): "))

if marks < 35:
    print("Fail")
elif 35 <= marks <= 59:
    print("Pass")
elif 60 <= marks <= 84:
    print("First Class")
elif marks >= 85:
    print("Distinction")
else:
    print("Invalid marks entered")
    
