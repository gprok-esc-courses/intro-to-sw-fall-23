students = {}

students[345] = {"name": "Peter", "grade": 56}
students[123] = {"name": "Jenn", "grade": 59}
students[893] = {"name": "Mike", "grade": 39}
students[109] = {"name": "Mike", "grade": 50}

for sid in students:
    print(sid, students[sid]['name'], 
          students[sid]['grade'])