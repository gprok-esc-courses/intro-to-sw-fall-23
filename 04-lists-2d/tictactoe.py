# Tic Tac Toe simple implementation

player = 'X'
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

while True:
    # display the board
    print(player, "is playing")
    for r in range(3):
        for c in range(3):
            print(board[r][c], end=' ')
        print()
    
    # ask curent user to play (row, col)
    row = int(input("Give row (1-3): "))
    col = int(input("Give col (1-3): "))

    # check for valid row and col
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid row or col, play again")
        continue

    # check if position is available
    row -= 1
    col -= 1
    if board[row][col] == '-':
        # if available update the position and change player
        board[row][col] = player
        player = 'X' if player == 'O' else 'O'
    else:
        print("Cell occupied, play again")

    # Check for winner

    # Check for tie

    
