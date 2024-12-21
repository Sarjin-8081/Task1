sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
sub4 = int(input("Enter marks for subject 4: "))

total = sub1 + sub2 + sub3 + sub4
print("Total marks =", total)

percent = total / 400 * 100
print(f"Percentage = {percent:.2f}%")

if percent > 70:
    print("Distinction")
elif percent > 60:
    print("First")
elif percent > 40:
    print("Pass")
else:
    print("Fail")
