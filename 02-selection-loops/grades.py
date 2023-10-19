# Display a message acoording to a student's grade

student_grade = float(input("Type your grade: "))

print(student_grade)

if student_grade > 70:
    print("Exceptional!")
elif student_grade > 60:
    print("Excellent")
elif student_grade > 50:
    print("Good")
elif student_grade >= 40:
    print("Fair")
else:
    print("Fail")