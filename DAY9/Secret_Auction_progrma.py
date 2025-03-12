import sys

print('''
        ⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠁⡀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣼⣿⣿⣿⡟⢀⣼⣿⣶⣤⣀⠘⠿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣼⣿⣿⣿⠟⢀⣾⣿⣿⣿⣿⣿⣷⣦⣄⠉⠻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⣾⣿⣿⣿⠏⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠈⠻⢿⡿⠃⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⢠⣿⣷⣦⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣠⣿⣿⣿⡟⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣦⣄⠙⠻⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⡟⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣈⠙⠻⣶⠄⠉⠛⠿⣿⡿⠁⣼⣿⣿⣿⠟⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠏⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⠋⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢠⣾⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        
    ''')

print("Welcome to the secret auction program.")

agin ="yes"
dic = {}
while agin == "yes":
    name = input("What is your name? ").lower()
    bid = input("What is your bid? $___ ")
    dic[name] = int(bid[1:])
    otherbidders = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if otherbidders == "yes":
        agin = "yes"
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
    elif otherbidders == "no":
      agin = "no"

max_key = max(dic, key=dic.get)  
max_value = dic[max_key]

print(f"The winner is {max_key} a bid of ${max_value}")
