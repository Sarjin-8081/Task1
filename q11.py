day = int(input("Please enter number of days: "))
if day == 5:
    print("Your charge is Rs2 per day.")
elif 6 <= day <= 10:
    print("Your charge is Rs3 per day.")
elif 11 <= day <= 15:
    print("Your charge is Rs4 per day.")
elif day > 15:
    print("Your charge is Rs5 per day.")
else:
    print("Invalid days")
