deposit = input('What is the amount of the initial deposit? ')
year1 = float(deposit) * 1.04
year2 = year1 * 1.04
year3 = year2 * 1.04
print(f'The amount after year 1 is ${year1:.2f}.')
print(f'The amount after year 2 is ${year2:.2f}.')
print(f'The amount after year 3 is ${year3:.2f}.')
year1_2 = "{:.2f}".format(year1)
year2_2 = "{:.2f}".format(year2)
year3_2 = "{:.2f}".format(year3)
print('The amount after year 1 is $' + (year1_2) + '.')
print('The amount after year 2 is $' + (year2_2) + '.')
print('The amount after year 3 is $' + (year3_2) + '.')