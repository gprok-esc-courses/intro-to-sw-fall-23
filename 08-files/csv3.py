import csv

file = open("students.csv")

reader = csv.DictReader(file)

# for row in reader:
#     print(row)

# Find name of student with id 3
for row in reader:
    if row['id'] == '3':
        print(row['name'])