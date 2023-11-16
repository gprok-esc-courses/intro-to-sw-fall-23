
students = {}

students[345] = ["Peter", 56]
students[123] = ["Jenn", 59]
students[893] = ["Mike", 39]
students[109] = ["Mike", 55]

for sid in students:
    print(sid, students[sid][0], students[sid][1])