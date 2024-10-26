age = input("What is your current age: ")

days = 90 * 365
weeks = 90 * 52
months = 90 * 12

user_days = int(age) * 365
user_weeeks = int(age) * 52
user_months = int(age) * 12

print(f"you have {days - user_days} days, {weeks - user_weeeks} weeks, and {months - user_months} months left.")