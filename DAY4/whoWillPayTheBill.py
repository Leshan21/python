import random

names = input("Enter the names(x, y, ...): ")

list = names.split(", ")

list_length = len(list)

ran_num = random.randint(0,list_length-1)

print(f"{list[ran_num]} is going to buy the meal today!")
     