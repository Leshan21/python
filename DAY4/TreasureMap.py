row1 = [" ◻️ "," ◻️ "," ◻️ "]
row2 = [" ◻️ "," ◻️ "," ◻️ "]
row3 = [" ◻️ "," ◻️ "," ◻️ "]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")


int_col = int(position[0])
int_row = int(position[1])


if(int_row == 1):
    row1[int_col-1] = "🏴"
elif(int_row == 2):
    row2[int_col-1] = "🏴"   
elif(int_row == 3):
    row3[int_col-1] = "🏴"     

print(f"{row1}\n{row2}\n{row3}")    