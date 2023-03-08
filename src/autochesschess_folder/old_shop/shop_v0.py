from ChessPiece import ChessPiece, Pawn, Knight, Bishop, Rook, Queen, King
import random

class AutoChessShop:
    def __init__(self):
        self.available_pieces = [Pawn(), Knight(), Bishop(), Rook(), Queen(), King()]

    def sell_piece(self):
        if len(self.available_pieces) == 0:
            print("There are no more pieces available to sell.")
            return None
        piece = random.choice(self.available_pieces)
        self.available_pieces.remove(piece)
        print("Sold a", piece.name, "for", piece.cost, "gold.")
        return piece

shop = AutoChessShop()

while True:
    command = input("Enter a command (buy, exit): ")
    if command == "buy":
        piece = shop.sell_piece()
        if piece is not None:
            # Add code here to add the purchased piece to the player's inventory
            print("Added", piece.name, "to your inventory.")
    elif command == "exit":
        print("Exiting shop.")
        break
    else:
        print("Invalid command. Try again.")
