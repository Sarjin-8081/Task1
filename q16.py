
N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))

apples_per_student = K // N
remaining_apples = K % N

print("Each student gets:", apples_per_student)
print("Apples remaining in the basket:", remaining_apples)
