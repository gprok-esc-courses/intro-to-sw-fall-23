
students = []
grades = []

def display_menu() -> None:
    print("1. Add")
    print("2. Change grade")
    print("3. Delete")
    print("4. Print")
    print("0. Exit")

def get_user_choice() -> int:
    try:
        choice = int(input("Choose: "))
    except ValueError:
        return -1
    return choice

def get_grade() -> int:
    try:
        grade = int(input("Give grade: "))
        if grade >= 0 and grade <= 100:
            return grade
        else:
            print("Invalid grade")
            return -1
    except ValueError:
        print("Invalid grade")
        return -1

def add_student(s: list[str], g: list[int]) -> None:
    name = input("Give name: ")
    if name in s:
        print("Name already in list")
        return
    else:
        grade = get_grade()
        if grade != -1:
            s.append(name)
            g.append(grade)


def get_existing_name(s: list[str]) -> str:
    name = input("Give name: ")
    if name not in s:
        return None
    else:
        return name

def change_grade(s: list[str], g: list[int]) -> None:
    name = get_existing_name(s)
    if name is not None:
        grade = get_grade()
        if grade != -1:
            for i in range(len(s)):
                if s[i] == name:
                    g[i] = grade
                    break

def delete_student(s: list[str], g: list[int]) -> None:
    name = get_existing_name(s)
    if name is not None:
        for i in range(len(s)):
            if s[i] == name:
                del s[i]
                del g[i]
                break

def print_students(s: list[str], g: list[int]) -> None:
    for i in range(len(s)):
        print(s[i], end=', grade: ')
        print(g[i])

while True:
    display_menu()
    choice = get_user_choice()
    if choice == 1:
        add_student(students, grades)
    elif choice == 2:
        change_grade(students, grades)
    elif choice == 3:
        delete_student(students, grades)
    elif choice == 4:
        print_students(students, grades)
    elif choice == 0:
        print("Bye!")
        break
    else:
        print("Wrong choice")