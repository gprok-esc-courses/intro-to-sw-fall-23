# Find the average grade of a student

courses = 0
total = 0

# Ask user how many courses they have
courses = int(input("How many courses: "))

for i in range(courses):
    print("Grade", i+1)
    grade = float(input())
    total = total + grade

print("Average", total/courses)