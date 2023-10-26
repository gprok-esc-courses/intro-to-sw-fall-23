grades = []

for i in range(5):
    g = float(input("Give next grade: "))
    grades.append(g)


print(max(grades))
print(min(grades))
print(sum(grades))
print(sum(grades)/len(grades))
print(sorted(grades))
print(grades)

if 40.0 in grades:
    print("found")

# Last element in the list
print(grades[len(grades)-1])
print(grades[-1])