total_days = int(input("Enter total number of days: "))
absent_days = int(input("Enter total number of absent days: "))
attended_days = total_days - absent_days
attendance_percentage = (attended_days / total_days) * 100
print(f"Attendance Percentage: {attendance_percentage}%")
if attendance_percentage < 75:
    print("Student will not be able to sit in exam\n")
else:
    print("Student is eligible for the exam\n")