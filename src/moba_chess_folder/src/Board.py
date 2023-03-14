from src.Coordinate import Coordinate as C

class Board:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = [[None] * num_cols for _ in range(num_rows)]
    
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def set_piece(self, row, col, piece_type):
        self.board[row][col] = piece_type
    
    def clear_square(self, row, col):
        self.board[row][col] = None
    
    def display_board(self):
    # Define the characters to use for the pieces
        piece_chars = {
            'K': '♔',
            'Q': '♕',
            'R': '♖',
            'B': '♗',
            'N': '♘',
            'P': '♙',
        }

        # Print the column headers
        print('  ', end='')
        for col in range(self.num_cols):
            print(chr(ord('a') + col), end=' ')
        print()

        # Draw the board
        for row in range(self.num_rows):
            print(row + 1, end=' ')
            for col in range(self.num_cols):
                if (row + col) % 2 == 0:
                    print('██', end='')
                else:
                    print('  ', end='')
                p = self.get_piece(row, col)
                if p is not None:
                    print(piece_chars[p], end='')
                else:
                    print(' ', end='')
            print(' ' + str(row + 1))

        # Print the column headers again
        print('  ', end='')
        for col in range(self.num_cols):
            print(chr(ord('a') + col), end=' ')
        print()




board = Board(33, 33)
board.set_piece(0, 0, 'R')
board.set_piece(0, 1, 'N')
board.set_piece(0, 2, 'B')
board.set_piece(0, 3, 'Q')
board.set_piece(0, 4, 'K')
board.set_piece(0, 5, 'B')
board.set_piece(0, 6, 'N')
board.set_piece(0, 7, 'R')
for col in range(8):
    board.set_piece(1, col, 'P')
    board.set_piece(6, col, 'P')
board.set_piece(7, 0, 'R')
board.set_piece(7, 1, 'N')
board.set_piece(7, 2, 'B')
board.set_piece(7, 3, 'Q')
board.set_piece(7, 4, 'K')
board.set_piece(7, 5, 'B')
board.set_piece(7, 6, 'N')
board.set_piece(7, 7, 'R')

board.display_board()
