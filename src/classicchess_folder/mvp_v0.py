# Import necessary modules
import os
import sys
import time

# Define constants
BOARD_SIZE = 8
EMPTY = '-'
BLACK = 'b'
WHITE = 'w'

# Define the initial state of the chess board
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Define a function to print the current state of the board
def print_board(board):
    print('    a b c d e f g h')
    print('  +-----------------+')
    for i in range(BOARD_SIZE):
        print(str(BOARD_SIZE - i) + ' |', end=' ')
        for j in range(BOARD_SIZE):
            print(board[i][j], end=' ')
        print('| ' + str(BOARD_SIZE - i))
    print('  +-----------------+')
    print('    a b c d e f g h')

# Define a function to get the position of a piece on the board
def get_position(prompt):
    while True:
        try:
            pos = input(prompt)
            if len(pos) != 2:
                raise ValueError('Invalid position')
            col = ord(pos[0]) - ord('a')
            row = BOARD_SIZE - int(pos[1])
            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                raise ValueError('Invalid position')
            return row, col
        except ValueError as e:
            print(e)

# Define a function to move a piece on the board
def move_piece(board, from_pos, to_pos):
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    piece = board[from_row][from_col]
    board[from_row][from_col] = EMPTY
    board[to_row][to_col] = piece

# Define the main function that controls the flow of the game
def play_game():
    print('Welcome to Chess!')
    print_board(board)
    turn = WHITE
    while True:
        print('Turn: ' + turn)
        from_pos = get_position('Enter the position of the piece to move: ')
        if board[from_pos[0]][from_pos[1]].lower() != turn:
            print('Invalid move: You can only move your own pieces')
            continue
        to_pos = get_position('Enter the position to move the piece to: ')
        move_piece(board, from_pos, to_pos)
        print_board(board)
        turn = BLACK if turn == WHITE else WHITE

# Run the game
play_game()
