num_subjects = int(input("Enter the total number of subjects: "))
total_marks = 0

for i in range(num_subjects):
    marks = float(input("Enter the marks obtained in subject " + str(i+1) + ": "))
    total_marks += marks

average_marks = total_marks / num_subjects

print("The average marks of the student is:", average_marks)
