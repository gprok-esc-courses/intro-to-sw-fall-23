# Calculates if a year is leap or not

year = int(input("Give the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")