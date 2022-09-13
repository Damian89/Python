width = input("Please enter the width of the field in feet): ")
length = input("Please enter the lenth of the field (in feet)")
fwidth = float(width)
flength = float(length)
acres = (fwidth*flength)/43560
print("The area of the field is", str(acres), "acres.")
print("The area of the field is %f acres." % (acres))