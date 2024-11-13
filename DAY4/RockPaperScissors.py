import random
ran_num = random.randint(0,2)

num = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors: "))

if num == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif num == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif num == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

print("computer chose: ")

if ran_num == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif ran_num == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif ran_num == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if num == ran_num:
    print("Draw")
elif num == 0 and ran_num == 2:
    print("You win..!")
elif num == 1 and ran_num == 0:
    print("you win..!")                        
elif num == 2 and ran_num == 1:
    print("you win..!")
else:
    print("You lose..!")        