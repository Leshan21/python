import random

names = input("Enter the names(x, y, ...): ")

list = names.split(", ")

list_length = len(list)

ran_num = random.randint(0,list_length-1)
print(ran_num)
if(ran_num == 0):
    print(f"{list[0]} is going to buy the meal today!")
elif(ran_num == 1):
    print(f"{list[1]} is going to buy the meal today!")
elif(ran_num == 2):
    print(f"{list[2]} is going to buy the meal today!")        
elif(ran_num == 3):
    print(f"{list[3]} is going to buy the meal today!")
elif(ran_num == 4):
    print(f"{list[4]} is going to buy the meal today!")        