# Ask user for a number and then display 
# the following pattern (in this pattern number
# is 5):
# *
# **
# *** 
# **** 
# ***** 
# **** 
# ***
# **
# *

n = int(input("Give a number: "))

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

