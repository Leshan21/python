print("Welcome to the tip calculator.")
bill = input("What was the totel bill: $")
flt_bill = float(bill)
tip = input("What percentage tip would you like to give?\n10%, 12% or 15%: ")
int_tip = int(tip)
peopleCount = input("How many people to split the bill: ")
int_peopleCount = int(peopleCount)
tip_balance = (flt_bill * int_tip) / 100
new_balance = flt_bill + tip_balance
onePersonBalance = new_balance / int_peopleCount
print(f"Each person should pay: ${round(onePersonBalance, 2)}")
