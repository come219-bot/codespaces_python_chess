import random

# Define the two players and assign them a coin face
player1 = "Alice"
player2 = "Bob"
player1_coin_face = "heads"
player2_coin_face = "tails"

# Simulate the coin toss and announce the winner
coin_toss_result = random.choice([player1_coin_face, player2_coin_face])
if coin_toss_result == player1_coin_face:
    print(f"{player1} won the coin toss!")
    winner = player1
else:
    print(f"{player2} won the coin toss!")
    winner = player2

# The winner chooses whether they want first pick or second pick
while True:
    pick_order = input(f"{winner}, do you want first pick or second pick? ").lower()
    if pick_order in ["first", "second"]:
        break
    else:
        print("Invalid input! Please enter 'first' or 'second'.")

first_picker, second_picker = (winner, player2) if pick_order == "first" else (player2, winner)

# Define the list of characters to choose from
characters = ["a","b","c","d","z", "x","Character1", "Character2", "Character3", "Character4", "Character5", "Bob", "Prince", "James", "Simon", "Alice"]

# The two players take turns banning characters from the list
banned_characters = []

print("Characters: ")
print(", ".join(characters))

for i in range(2):
    while True:
        ban_choice = input(f"{first_picker}, choose a character to ban: ")
        if ban_choice.lower() in [c.lower() for c in characters]:
            banned_characters.append(ban_choice)
            characters.remove(ban_choice)
            break
        else:
            print(f"{ban_choice} is not a valid character! Please choose from the following characters: {', '.join(characters)}")

    while True:
        ban_choice = input(f"{second_picker}, choose a character to ban: ")
        if ban_choice.lower() in [c.lower() for c in characters]:
            banned_characters.append(ban_choice)
            characters.remove(ban_choice)
            break
        else:
            print(f"{ban_choice} is not a valid character! Please choose from the following characters: {', '.join(characters)}")

print("Banned Characters: ")
print(", ".join(banned_characters))

print("Characters: ")
print(", ".join(characters))

# The two players take turns picking from the list of available characters
drafted_characters = []
for i in range(2):
    while True:
        pick_choice = input(f"{first_picker}, choose a character: ")
        if pick_choice.lower() in [c.lower() for c in characters]:
            drafted_characters.append(pick_choice)
            characters.remove(pick_choice)
            break
        else:
            print(f"{pick_choice} is not a valid character! Please choose from the following characters: {', '.join(characters)}")

    while True:
        pick_choice = input(f"{second_picker}, choose a character: ")
        if pick_choice.lower() in [c.lower() for c in characters]:
            drafted_characters.append(pick_choice)
            characters.remove(pick_choice)
            break
        else:
            print(f"{pick_choice} is not a valid character! Please choose from the following characters: {', '.join(characters)}")

print("Draft phase complete!")
print(f"{first_picker} drafted {drafted_characters[0]} and {second_picker} drafted {drafted_characters[1]}")
print(f"{second_picker} drafted {drafted_characters[2]} and {first_picker} drafted {drafted_characters[3]}")
