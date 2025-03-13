import sys
# operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# create dictionary
dic = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def main_cal():
    num1 = int(input("What is the first number?: "))
    num2 = int(input("What is the second number?: "))

    # print operations symbles 
    for key in dic:
        print(key)
        
    opration_symble = input("Pick an oparation from the line above: ")
    
    # print answer
    print(f"{num1} {opration_symble} {num2} = {dic[opration_symble](num1,num2)}")
  
    cn = input(f"Type 'y' to continue calculating with {dic[opration_symble](num1,num2)}, or type 'n' to start new calculation: ").lower()
    answer = dic[opration_symble](num1,num2)
    # looping
    while cn == 'y' or cn == 'n':
        if cn == 'y':
            opration_symble = input("Pick an Operation: ")
            num1 = answer
            num2 = int(input("What is the next number: "))
            answer = dic[opration_symble](answer,num2)
            print(f"{num1} {opration_symble} {num2} = {answer}")
            cn = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit,: ").lower()
        elif cn == 'n':
            sys.stdout.write("\033[H\033[J")
            sys.stdout.flush()
            main_cal()
              
main_cal()        
    
