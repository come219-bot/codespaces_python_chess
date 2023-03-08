import random

# Define the chess pieces
pieces = {
    "pawn": {
        "cost": 1,
        "power": 1,
        "health": 1
    },
    "knight": {
        "cost": 2,
        "power": 2,
        "health": 2
    },
    "bishop": {
        "cost": 3,
        "power": 3,
        "health": 3
    },
    "rook": {
        "cost": 4,
        "power": 4,
        "health": 4
    },
    "queen": {
        "cost": 5,
        "power": 5,
        "health": 5
    },
    "king": {
        "cost": 6,
        "power": 6,
        "health": 6
    }
}

# Define the game board
board = [[None for _ in range(8)] for _ in range(8)]

# Define the players
players = {
    "player1": {
        "name": "Player 1",
        "pieces": [],
        "gold": 5
    },
    "player2": {
        "name": "Player 2",
        "pieces": [],
        "gold": 5
    }
}

# Function to randomly generate a chess piece for a player
def generate_piece():
    piece_name = random.choice(list(pieces.keys()))
    piece = {
        "name": piece_name,
        "power": pieces[piece_name]["power"],
        "health": pieces[piece_name]["health"]
    }
    return piece

# Function to print the game board
def print_board():
    for row in board:
        print(row)

# Function to start the game
def start_game():
    # Generate pieces for each player
    for player in players.values():
        for i in range(5):
            piece = generate_piece()
            player["pieces"].append(piece)

    # Print the game board
    print_board()

# Call the start_game function to start the game
start_game()
