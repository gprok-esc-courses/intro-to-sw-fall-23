import csv

file = open("students.csv")

reader = csv.reader(file)

for row in reader:
    print(row)