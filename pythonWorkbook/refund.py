print('Small containers are one liter or less.')
nSmall = input('How many small containers are there?\n')
print('Large containers are more than one liter.')
nLarge = input('How many large containers are there?\n')
refund = (float(nSmall) * .10) + (float(nLarge) * 0.25)
print(f'Your refund is ${refund:.2f}.')