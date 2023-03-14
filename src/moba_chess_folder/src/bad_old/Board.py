import Piece as Piece

class Board:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = [[None] * num_cols for _ in range(num_rows)]
    
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def set_piece(self, row, col, piece):
        self.board[row][col] = piece
        
    def clear_square(self, row, col):
        self.board[row][col] = None
    
    def display_board(self):
        # Define the characters to use for the pieces
        piece_chars = {
            piece.King: 'K',
            piece.Queen: 'Q',
            piece.Rook: 'R',
            piece.Bishop: 'B',
            piece.Knight: 'N',
            piece.Pawn: 'P',
        }
        
        # Draw the board
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (row + col) % 2 == 0:
                    print('██', end='')
                else:
                    print('  ', end='')
                p = self.get_piece(row, col)
                if p is not None:
                    print(piece_chars[type(p)], end='')
                else:
                    print(' ', end='')
            print()

# Create a sample board
board = Board(8, 8)
board.set_piece(0, 0, Piece.Rook())
board.set_piece(0, 1, Piece.Knight())
board.set_piece(0, 2, Piece.Bishop())
board.set_piece(0, 3, Piece.Queen())
board.set_piece(0, 4, Piece.King())
board.set_piece(0, 5, Piece.Bishop())
board.set_piece(0, 6, Piece.Knight())
board.set_piece(0, 7, Piece.Rook())
for col in range(8):
    board.set_piece(1, col, Piece.Pawn())
    board.set_piece(6, col, Piece.Pawn())
board.set_piece(7, 0, Piece.Rook())
board.set_piece(7, 1, Piece.Knight())
board.set_piece(7, 2, Piece.Bishop())
board.set_piece(7, 3, Piece.Queen())
board.set_piece(7, 4, Piece.King())
board.set_piece(7, 5, Piece.Bishop())
board.set_piece(7, 6, Piece.Knight())
board.set_piece(7, 7, Piece.Rook())

# Print the board
board.display_board()
