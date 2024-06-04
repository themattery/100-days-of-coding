
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? "))
split = int(input("How many people to split the bill? "))

total = (bill + (tip/100*bill))/split

print(f"Each person should pay: ${total:.2f}")