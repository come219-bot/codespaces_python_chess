class ManageBoard:
    def __init__(self):
        self.board = [['-' for _ in range(8)] for _ in range(8)]
        self.board[3][4] = 'P' # set the position of Pawn on the board
        self.board[2][3] = 'P' # set the position of Pawn on the board
        self.board[6][3] = 'P' # set the position of Pawn on the board
        self.board[5][4] = 'P' # set the position of Pawn on the board
        self.board[7][4] = 'K' # set the position of Knight on the board
    
    def print_board(self):
        print('  a b c d e f g h ')
        print('+-----------------+')
        for i in range(8):
            row = ''
            for j in range(8):
                row += '|' + ' ' + self.board[i][j]
            row += '|' + ' ' + str(8 - i)
            print(row)
            print('+-----------------+')
        print('  a b c d e f g h ')
        
    def alliances(self):
        hunter = {'attack': 3, 'health': 3, 'cost': 5}
        blood_bound = {'attack': 1, 'health': 3, 'cost': None}
        print('Alliances:')
        print('Hunter: (attack: {}, health: {}, cost: {})'.format(hunter['attack'], hunter['health'], hunter['cost']))
        print('Blood-bound: (attack: {}, health: {}, cost: {})'.format(blood_bound['attack'], blood_bound['health'], blood_bound['cost']))




board = ManageBoard()
board.print_board()
board.alliances()
