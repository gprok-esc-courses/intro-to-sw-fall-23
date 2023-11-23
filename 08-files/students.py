file = open("students.txt", "w")

while True:
    name = input("Give a name (- to stop): ")
    if name == '-':
        break
    else:
        file.write(name + '\n')

file.close()