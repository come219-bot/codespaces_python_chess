class ChessPiece:
    def __init__(self, name, cost, health, attack_damage, attack_range, ability):
        self.name = name
        self.cost = cost
        self.health = health
        self.attack_damage = attack_damage
        self.attack_range = attack_range
        self.ability = ability
        # self.starlevel = starlevel

# original chess pieces ...
class Pawn(ChessPiece):
    def __init__(self):
        super().__init__("Pawn", 1, 100, 10, 1, "None")

class Knight(ChessPiece):
    def __init__(self):
        super().__init__("Knight", 3, 200, 20, 2, "Jump attack")

class Bishop(ChessPiece):
    def __init__(self):
        super().__init__("Bishop", 3, 150, 15, 2, "Diagonal attack")

class Rook(ChessPiece):
    def __init__(self):
        super().__init__("Rook", 5, 300, 30, 1, "Area attack")

class Queen(ChessPiece):
    def __init__(self):
        super().__init__("Queen", 7, 400, 40, 3, "Multi-directional attack")

class King(ChessPiece):
    def __init__(self):
        super().__init__("King", 10, 500, 50, 1, "None")

# chess 2 pieces

class Chancellor(ChessPiece):
    def __init__(self):
        super().__init__("Chancellor", 9,  450, 35, 2, "knighted")


class Prince(ChessPiece):
    def __init__(self):
        super().__init__("Prince", 8, 300, 20, 3, "In line")

class Lord(ChessPiece):
    def __init__(self):
        super().__init__("Lord", 2, 100, 10, 2, "has land")


# new pieces from mobachess:

# https://altcodeunicode.com/alt-codes-playing-card-symbols/

# Man ☺☻
# ♠ - damager, deals dps damage x2
# ♣ - tanker, shields damage
# ♥ - healer, heals health
# ♦ - nuker, instant damage w/ mana

# negater 🂠
# disables gambler or any ability only
 
# gambler, 🂡
# damage card 'n' x 10 = symbol is ... damage 

# joker 🃏

# moon 🃩, night more vision?

# aa 🃳, 10% hp and kill


 
