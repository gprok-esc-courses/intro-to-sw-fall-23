
data = [
    [1, 2, 3, 4, 5],
    [6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17]
]

# I want to print this list as Rows and Cols
for row in range(4):
    columns = len(data[row])
    for col in range(columns):
        print(data[row][col], end=' ')
    print()
