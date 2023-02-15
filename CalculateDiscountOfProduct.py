original_price = float(input("Enter the original price of the product: "))
discount_percentage = float(input("Enter the percentage discount offered: "))

discount_amount = original_price * discount_percentage / 100
discounted_price = original_price - discount_amount

print("The discount amount is:", discount_amount)
print("The discounted price is:", discounted_price)
