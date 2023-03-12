class Inventory:
    def __init__(self):
        self.units = []
        
    def add_unit(self, unit):
        self.units.append(unit)
        
    def remove_unit(self, unit):
        self.units.remove(unit)
        
    def get_units(self):
        return self.units
    
    def clear(self):
        self.units = []
        
    def sort(self):
        self.units.sort()


class ManageBoard:
    def __init__(self):
        self.board = [['-' for i in range(8)] for j in range(8)]
        self.inventory = Inventory()
        
    def display(self):
        print('  a b c d e f g h')
        print(' +' + '-'*17 + '+')
        for i in range(8):
            row = str(8-i) + '|'
            for j in range(8):
                if self.board[i][j] == '#':
                    row += ' #'
                else:
                    unit = self.get_unit_at_position(i, j)
                    if unit:
                        row += ' ' + unit
                    else:
                        row += ' -'
            row += ' |' + str(8-i)
            print(row)
        print(' +' + '-'*17 + '+')
        print('  a b c d e f g h')
        
    def add_unit(self, unit, row, col):
        self.inventory.add_unit(unit)
        self.board[row][col] = '#'
        
    def remove_unit(self, unit, row, col):
        self.inventory.remove_unit(unit)
        self.board[row][col] = '-'
        
    def get_unit_at_position(self, row, col):
        for unit in self.inventory.get_units():
            if unit.get_row() == row and unit.get_col() == col:
                return unit.get_symbol()
        return None






# create a ManageBoard instance
board = ManageBoard()

# add some units to the board
board.add_unit('P', 4, 4)
board.add_unit('K', 7, 4)

# display the board
board.display()

# create an Inventory instance
inv = Inventory()

# add some units to the inventory
inv.add_unit('P')
inv.add_unit('K')

# display the units in the inventory
print(inv.get_units())
