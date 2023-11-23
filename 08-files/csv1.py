# Read as plain file, and split by comma

file = open("students.csv")

lines = file.readlines()

headers = lines[0].strip().split(',')
print(headers)
plain_data = lines[1:]
data = []
for row in plain_data:
    data.append(row.strip().split(','))
print(data)

# print student name with id 3
for student in data:
    if student[0] == '3':
        print(student[1])