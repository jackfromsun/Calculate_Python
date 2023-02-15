rate_per_unit = float(input("Enter the rate of electricity per unit: "))
units_consumed = float(input("Enter the number of units consumed: "))
fixed_charges = float(input("Enter any fixed charges: "))

bill_amount = (rate_per_unit * units_consumed) + fixed_charges

print("The electricity bill amount is:", bill_amount)
