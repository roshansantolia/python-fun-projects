# Tip Calculator

print("Welcome to Tip Calculator.")
total_bill = float(input("What was the total bill"))
one_percent = float(total_bill/100)
tip_to_add = int(input("What percent tip you want to add"))
tip_percent = one_percent * tip_to_add
tip_with_bill = total_bill + tip_percent
total_peoples = int(input("How many peoples are there"))
to_pay = (tip_with_bill / total_peoples)
print(f"Each person should pay {to_pay}")