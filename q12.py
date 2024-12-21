sal=int(input("Enter your salary="))
yr=int(input("Enter your service years="))
if yr>5:
    new_sal=sal*5/100
    print(f"You got a bonus of 5%,your bonus net bonus amount is {new_sal}")
else:
    print("Invalid years")