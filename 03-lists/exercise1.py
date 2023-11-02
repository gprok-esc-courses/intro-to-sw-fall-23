# 1.	Create a list of 10 numbers [18, 92, 75, 44, 70, 56, 40, 33, 41, 68, 49, 28] representing the grades of some students. Write Python code to: 
# a.	Change 2nd grade from 92 to 72.
# b.	Find the grades lower than 40 and put them in a new list.
# c.	Print the lists sorted.
# d.	Ask the user for a number and find if the number is in the list. If yes, find its position in the list.

grades = [18, 92, 75, 44, 70, 56, 40, 33, 41, 68, 49, 28]

# task a
grades[1] = 72

# task b
less_than_40 = []
for g in grades:
    if g < 40:
        less_than_40.append(g)
print(less_than_40)

# task c
print(sorted(grades))

# task d
n = int(input("Give a number: "))
if n in grades:
    print(n, "is in the list")
    print("At position:", grades.index(n))
else:
    print(n, "not in the list")