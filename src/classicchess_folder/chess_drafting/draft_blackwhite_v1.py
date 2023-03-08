import random

# Define the two players and assign them a coin face
player1 = "Alice"
player2 = "Bob"
player1_coin_face = "heads"
player2_coin_face = "tails"

# Simulate the coin toss and announce the winner
coin_toss_result = random.choice(["heads", "tails"])
if coin_toss_result == player1_coin_face:
    print(f"{player1} won the coin toss!")
    first_picker = player1
    second_picker = player2
else:
    print(f"{player2} won the coin toss!")
    first_picker = player2
    second_picker = player1

# The two players choose their color
valid_color_choices = ["black", "white"]
while True:
    print(f"{first_picker}, do you want to play as black or white?")
    first_player_color_choice = input().lower()

    if first_player_color_choice in valid_color_choices:
        first_player_color = first_player_color_choice
        second_player_color = valid_color_choices[(valid_color_choices.index(first_player_color) + 1) % len(valid_color_choices)]
        print(f"{second_picker}, you are playing as {second_player_color}.")
        break
    else:
        print("Invalid input! Please enter 'black' or 'white'.")


