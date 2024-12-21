age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))
if 18 <= age < 30:
     if gender == "M" :
         wage=700
     else:
         wage=750
elif 30 <= age <= 40:
    wage = 800 if gender == "M" else 850
else:
    wage = 0
    
if wage:
    print(f"Total wages: {wage * days}\n")
else:
    print("Wages not defined for the given age\n")