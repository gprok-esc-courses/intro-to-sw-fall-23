
data = [
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33]
]

print(data[1][3])
print(data)

# for every row
for row in range(3):
    # for each column
    for col in range(4):
        print(data[row][col], end=' ')
    print()