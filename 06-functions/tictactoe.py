# Tic Tac Toe simple implementation

player = 'X'
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def display_current_player(player):
    print(player, "is playing")

def display_board(board):
    for r in range(3):
        for c in range(3):
            print(board[r][c], end=' ')
        print()

def play(board, player):
    # ask curent user to play (row, col)
    row = int(input("Give row (1-3): "))
    col = int(input("Give col (1-3): "))
    # check for valid row and col
    if row < 1 or row > 3 or col < 1 or col > 3:
        return -1, -1, "Invalid row or col, play again")
    else:
        # change from 1-3 to 0-2
        row -= 1
        col -= 1
        if board[row][col] == '-':
            return row, col, None
        else:
            return -1, -1, "Cell occupied, play again")

def update_board(board, player, row, col):
    board[row][col] = player

def change_player(player):
    return 'X' if player == 'O' else 'O'

while True:
    display_current_player(player)
    display_board(board)
    row, col, err = play(board)
    if err is None:
        update_board(board, player, row, col)
        player = change_player(player)
    else:
        print(err)
            

    # Check for winner

    # Check for tie

    
