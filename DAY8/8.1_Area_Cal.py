import math

test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))

coverage = 5
def number_of_cans(height,width,coverage):
    cans = math.ceil((test_h*test_w)/coverage) #round the number like 2.1->3   4.6->5
    print(f"number of cans {cans}")

number_of_cans(height=test_h,width=test_w,coverage=coverage)    