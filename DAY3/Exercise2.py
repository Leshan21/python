height = int(input("Enter your height: "))
bill = 0
if height > 120:
    print("You can ride")
    age = int(input("Enter your age: "))
    
    if age < 12:
        bill += 5
        print("Your ticket price is $5.")
    elif age < 18:
        bill += 7
        print("Your ticket price is $7.")
    else:
        bill += 12
        print("Your ticket price is $12.")
    
    take_photo = input("Are you need a photo?\nY/N: ") 
    if take_photo == "Y":
        bill += 3
        
    print(f"Your final bill ${bill}")               
else:
    print("You can't ride")