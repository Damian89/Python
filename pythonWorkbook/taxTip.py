cost = input('How much did the meal cost?  $')
mealCost = float(cost)
taxAmount = mealCost * 0.06
tip = mealCost * 0.18
total = mealCost + taxAmount + tip
# print(f"The cost of the meal is ${mealCost:.2f}")
print(f"The tax is ${taxAmount:.2f}")
print(f"The tip is ${tip:.2f}")
print(f"The total bill is ${total:.2f}")

