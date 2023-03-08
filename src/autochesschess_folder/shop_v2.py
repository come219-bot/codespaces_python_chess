import random
from ChessPiece import *

class AutoChessShop:
    def __init__(self):
        self.inventory = []
        self.shop = []
        self.generate_shop()

    def generate_shop(self):
        self.shop = []
        for i in range(5):
            piece = self.random_chess_piece()
            self.shop.append(piece)

    def random_chess_piece(self):
        piece_types = [Pawn, Knight, Bishop, Rook, Queen, King]
        piece_type = random.choice(piece_types)
        piece = piece_type()
        return piece

    def buy_piece(self, piece_index):
        if piece_index >= len(self.shop):
            print("Invalid piece index.")
            return
        piece = self.shop[piece_index]
        if piece.cost > self.gold:
            print("You do not have enough gold to buy this piece.")
            return
        self.inventory.append(piece)
        self.gold -= piece.cost
        self.shop.pop(piece_index)
        print("You bought a", piece.name, "for", piece.cost, "gold.")



    def sell_piece(self, piece_index):
        if piece_index >= len(self.inventory):
            print("Invalid piece index.")
            return
        piece = self.inventory[piece_index]
        self.gold += piece.cost
        self.inventory.pop(piece_index)
        print("You sold a", piece.name, "for", piece.cost, "gold.")

    def reroll_shop(self):
        if self.gold < 2:
            print("You do not have enough gold to reroll.")
            return
        self.gold -= 2
        self.generate_shop()
        print("You rerolled the shop for 2 gold.")

    def print_shop(self):
        print("Shop:")
        for i, piece in enumerate(self.shop):
            print(str(i) + ".", piece.name, "-", piece.cost, "gold")
        print("")

    def print_inventory(self):
        print("Inventory:")
        for i, piece in enumerate(self.inventory):
            print(str(i) + ".", piece.name)
        print("")

    def play(self):
        self.gold = 5
        while True:
            self.print_shop()
            self.print_inventory()
            print("Gold:", self.gold)
            print("What would you like to do?")
            print("1. Buy a piece")
            print("2. Sell a piece")
            print("3. Reroll the shop")
            print("4. End turn")
            choice = input("> ")
            if choice == "1":
                piece_index = int(input("Enter the index of the piece you would like to buy: "))
                self.buy_piece(piece_index)
            elif choice == "2":
                piece_index = int(input("Enter the index of the piece you would like to sell: "))
                self.sell_piece(piece_index)
            elif choice == "3":
                self.reroll_shop()
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    shop = AutoChessShop()
    shop.play()
