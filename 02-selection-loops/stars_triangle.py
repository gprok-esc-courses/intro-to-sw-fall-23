# Print n stars

n = int(input("Give n: "))

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()
print()