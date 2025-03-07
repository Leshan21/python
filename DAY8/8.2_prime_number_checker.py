n = int(input("Check this number: "))

def prime_number_checker(number):
    count=0
    for i in range(2,number-1):
        if(number%i==0):
            count+=1
    if(count==0):        
        print("It's a prime number")
    else:
        print("It's not a prime number")    

prime_number_checker(number=n)
        
        