print("Welcome to Love calculator")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

count_first_line = 0
count_second_line = 0

#firstsecond
count_first_line += lower_name1.count("t")
count_first_line += lower_name2.count("t")

count_first_line += lower_name1.count("r")
count_first_line += lower_name2.count("r")

count_first_line += lower_name1.count("u")
count_first_line += lower_name2.count("u")

count_first_line += lower_name1.count("e")
count_first_line += lower_name2.count("e")

#second_line
count_second_line += lower_name1.count("l")
count_second_line += lower_name2.count("l")

count_second_line += lower_name1.count("o")
count_second_line += lower_name2.count("o")

count_second_line += lower_name1.count("v")
count_second_line += lower_name2.count("v")

count_second_line += lower_name1.count("e")
count_second_line += lower_name2.count("e")

love_percentage = (count_first_line * 10) + count_second_line

if love_percentage <= 10 or love_percentage >= 90:
    print(f"Your score is {love_percentage}, You go together like coke and mentos.")
elif love_percentage >=40 and love_percentage <= 50:
    print(f"Your score is {love_percentage}, You are alright together.")
else:
    print(f"Your score is {love_percentage}")         