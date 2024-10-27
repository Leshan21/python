height = float(input("Enter your height(m): "))
weight = float(input("Enter your weight(kg): "))

BMI = round(weight / (height**2), 1)


if BMI < 18.5:
    print(f"your BMI is {BMI} and Underweight")
elif BMI < 25:
    print(f"your BMI is {BMI} and Normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI} and Over weight")
elif BMI < 35:
    print(f"your BMI is {BMI} and obese")
else:
    print(f"your BMI is {BMI} and clinically obese")   
         
            