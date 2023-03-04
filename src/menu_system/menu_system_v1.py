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
        """
        Start a game of Classic Chess
        """
        print(f"Starting {self.game_type} Game...")

    def chess_2(self):
        """
        Start a game of Chess 2
        """
        print(f"Starting {self.game_type} Game...")

    def moba_chess(self):
        """
        Start a game of Moba Chess
        """
        print(f"Starting {self.game_type} Game...")

    def settings(self):
        """
        Open the Settings menu to change game type or access other options
        """
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

        # Check for valid option input and update game_type or call other functions
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
        """
        Open the Chess Options menu to change chess game settings
        """
        print("Opening Chess Options Menu...")
        print("Please select an option:")
        print("1. Set Starting Position")
        print("2. Enable/Disable En Passant")
        print("3. Enable/Disable Castling")
        option = input()

        # Check for valid option input and update chess game settings

    def bot_options(self):
        """
        Open the Bot Options menu to change bot settings
        """
        print("Opening Bot Options Menu...")
        print("Please select an option:")
        print("1. Set Bot Difficulty")
        print("2. Enable/Disable Bot")
        option = input()

        # Check for valid option input and update bot settings

    def exit_game(self):
        """
        Exit the game
        """
        print("Exiting the game...")
        exit()

    def display_menu(self):
        """
        Display the main menu options
        """
        print("Welcome to the Chess Game!")
        print(f"Current game type: {self.game_type}")
        print("Please select an option:")
        print("1. Classic Chess")
        print("2. Chess 2")
        print("3. Moba Chess")
        print("4. Settings")
        print("5. Exit")

    def start(self):
        """
        Start the menu system and continue displaying menu until the user exits the game
        """
        while True:
            self.display_menu()
            option = input()

            # Check for valid option input and call the corresponding function
            if option in self.options:
                self.options[option]()
            else:
                print("Invalid option. Please enter a valid option.")

menu = MenuSystem()
menu.start()
