height = input("enter your height in m: ")
weight = input("enter your weught in kg: ")
flt_weight = float(weight)
flt_height = float(height)
bmi = flt_weight/(flt_height ** 2)

int_bmi = int(bmi)
str_bmi = str(int_bmi)

print(str_bmi)