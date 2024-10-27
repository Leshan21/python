print("Welcome to python pizza Deliveries.")
size = input("What size pizza do you wants?\nS/M/L: ")
add_pepperoni = input("Do you want pepperoni?\nY/N: ")
extra_chees = input("Do you want extra chees?\nY/N: ")

bill = 0 

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
if size == "L":
    bill += 25 
    if add_pepperoni == "Y":
        bill += 3
if extra_chees == "Y":
    bill += 1
            
print(f"Your final bill is: {bill}")                   