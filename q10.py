time=int(input("Please Enter your service year in numbers ="))
sal=int(input("Please enter your salary="))
if time>10:
    new_sal=sal*10/100
    print(f"You got a bonus of 10%, Your bonus is {new_sal}.")
elif time>=6 and time<=10:
    new_sal=sal*8/100
    print(f"You got a bonus of 8%, Your bonus is {new_sal}")
elif time<6:
    new_sal=sal*8/100
    print(f"You got a bonus of 5%, Your bonus is {new_sal}")
else:
    print("invalid years")