import random
from ChessPiece import *
from AutoChessShop import *

class AutoChessGameState:
    def __init__(self):
        self.shop = AutoChessShop()
        self.manage_board = ManageBoard()
        self.enemy_board = EnemyBoard()

    def play(self):
        while True:
            print("What would you like to do?")
            print("1. Go to the shop")
            print("2. Manage your board")
            print("3. View the enemy board")
            print("4. End turn")
            print("5. Game options")
            choice = input("> ")
            if choice == "1":
                self.shop.play()
            elif choice == "2":
                self.manage_board.play()
            elif choice == "3":
                self.enemy_board.play()
            elif choice == "4":
                self.end_turn()
            elif choice == "5":
                self.game_options()
            else:
                print("Invalid choice.")

    def end_turn(self):
        print("Ending turn.")

    def game_options(self):
        print("Game options.")

class ManageBoard:
    def __init__(self):
        self.board = []

    def play(self):
        print("Managing board.")

class EnemyBoard:
    def __init__(self):
        self.board = []

    def play(self):
        print("Viewing enemy board.")

if __name__ == "__main__":
    game_state = AutoChessGameState()
    game_state.play()
