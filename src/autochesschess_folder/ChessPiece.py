class ChessPiece:
    def __init__(self, name, cost, health, attack_damage, attack_range, ability):
        self.name = name
        self.cost = cost
        self.health = health
        self.attack_damage = attack_damage
        self.attack_range = attack_range
        self.ability = ability

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
