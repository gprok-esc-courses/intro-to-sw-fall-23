# We have 2 lists of sorted integers
# Merge into a single sorted list

a = [3, 6, 9, 12, 18, 19, 20]
b = [4, 5, 6, 12, 17, 21, 45, 56]

# [3, 4, 5, 6, 6, 9, 12, 12, 17, 18, 19, 20, 21, 45, 56]

# Easy, pythonian way
# c = a + b
# print(sorted(c))
# but you are not allowed to use that ...

ia = 0
ib = 0
c = []

while ia < len(a) and ib < len(b):
    if a[ia] < b[ib]:
        c.append(a[ia])
        ia += 1
    else:
        c.append(b[ib])
        ib += 1

if ia < len(a):
    c = c + a[ia:]
elif ib < len(b):
    c = c + b[ib:]

print(c)




