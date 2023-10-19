# Calculates if a year is leap or not

year = int(input("Give the year: "))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("YES")
elif year % 4 == 0:
    print("YES")
else:
    print("NO")