# Ask user for a number N, 
# if N is even, decrease by 1
# Print a xmas tree with its base equal to N
# Add O chars as decoration with a probability 20%

import random

n = int(input("Give N: "))

if n % 2 == 0:
    n -= 1

lines = n // 2 + 1
asterisks = 1
spaces = n // 2
probability = 20

# Repeat line times
    # Repeat spaces times and print a space
    # Repeat asterisks time and print an asterisk
    # Decrease spaces by 1
    # Increase asterisks by 2

for i in range(lines):
    for s in range(spaces):
        print(' ', end='')
    for a in range(asterisks):
        r = random.randint(1, 100)
        if r < probability:
            print('O', end='')
        else:
            print('*', end='')
    print()
    spaces -= 1
    asterisks += 2

# Print the base of the tree
for i in range(n // 2):
    print(' ', end='')
print('#')
for i in range(n // 2):
    print(' ', end='')
print('#')
