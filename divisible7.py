# Get the weight of the user
weight = float(input("Enter your weight: "))

if weight < 50:
    print("Under weight")
elif 50 <= weight < 80:
    print("Normal weight")
else:
    print("Over weight")