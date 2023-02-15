num_subjects = int(input("Enter the number of subjects: "))
total_credits = 0
total_grade_points = 0

for i in range(num_subjects):
    credits = int(input("Enter the credit hours of subject " + str(i+1) + ": "))
    grade = float(input("Enter the grade of subject " + str(i+1) + ": "))
    total_credits += credits
    total_grade_points += grade * credits

cgpa = total_grade_points / total_credits

print("The CGPA is:", cgpa)
