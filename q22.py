percentage = float(input("Enter your percentage: "))
if percentage < 40:
    print("Category: Failed\n")
elif percentage >=40 and percentage < 55:
    print("Category: Fair\n")
elif percentage >=55 and percentage < 65:
    print("Category: Good\n")
else:
    print("Category: Excellent\n")