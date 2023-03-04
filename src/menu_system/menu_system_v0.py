class MenuSystem:
    def __init__(self):
        self.game_type = "Classic Chess"
        self.options = {
            "1": self.classic_chess,
            "2": self.chess_2,
            "3": self.moba_chess,
            "4": self.settings,
            "5": self.exit_game
        }

    def classic_chess(self):
        print(f"Starting {self.game_type} Game...")

    def chess_2(self):
        print(f"Starting {self.game_type} Game...")

    def moba_chess(self):
        print(f"Starting {self.game_type} Game...")

    def settings(self):
        # Implement settings logic here to change game_type
        print("Opening Settings Menu...")
        print(f"Current game type: {self.game_type}")
        print("Please select a game type:")
        print("1. Singleplayer")
        print("2. 2 Players")
        print("3. Multiplayer")
        print("4. Custom Lobby")
        print("5. Chess Options")
        print("6. Bot Options")
        option = input()

        if option == "1":
            self.game_type = "Singleplayer"
        elif option == "2":
            self.game_type = "2 Players"
        elif option == "3":
            self.game_type = "Multiplayer"
        elif option == "4":
            self.game_type = "Custom Lobby"
        elif option == "5":
            self.chess_options()
        elif option == "6":
            self.bot_options()
        else:
            print("Invalid option. Returning to main menu.")

    def chess_options(self):
        print("Opening Chess Options Menu...")
        print("Please select an option:")
        print("1. Set Starting Position")
        print("2. Enable/Disable En Passant")
        print("3. Enable/Disable Castling")
        option = input()

        # Implement Chess Options logic here

    def bot_options(self):
        print("Opening Bot Options Menu...")
        print("Please select an option:")
        print("1. Set Bot Difficulty")
        print("2. Enable/Disable Bot")
        option = input()

        # Implement Bot Options logic here

    def exit_game(self):
        # Implement exit game logic here
        print("Exiting the game...")
        exit()

    def display_menu(self):
        print("Welcome to the Chess Game!")
        print(f"Current game type: {self.game_type}")
        print("Please select an option:")
        print("1. Classic Chess")
        print("2. Chess 2")
        print("3. Moba Chess")
        print("4. Settings")
        print("5. Exit")

    def start(self):
        while True:
            self.display_menu()
            option = input()

            if option in self.options:
                self.options[option]()
            else:
                print("Invalid option. Please enter a number from 1 to 5.")

menu = MenuSystem()
menu.start()

