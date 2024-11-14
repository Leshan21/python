scores = input("Enter the students heights: ")

list = scores.split(" ")

sum = 0

for number in range(0, len(list)):
   sum = sum + int(list[number]) 

print(sum/len(list))   