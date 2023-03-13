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
    winner = player1
else:
    print(f"{player2} won the coin toss!")
    winner = player2

# The winner chooses whether they want first pick or second pick
print(f"{winner}, do you want first pick or second pick?")
pick_order = input().lower()

if pick_order == "first":
    first_picker = winner
    second_picker = player2 if winner == player1 else player1
else:
    first_picker = player2 if winner == player1 else player1
    second_picker = winner

# Define the list of characters to choose from
characters = ["Character1", "Character2", "Character3", "Character4", "Character5"]

# The two players take turns banning characters from the list
banned_characters = []
for i in range(2):
    print(f"{first_picker}, choose a character to ban:")
    ban_choice = input()
    banned_characters.append(ban_choice)
    characters.remove(ban_choice)
    
    print(f"{second_picker}, choose a character to ban:")
    ban_choice = input()
    banned_characters.append(ban_choice)
    characters.remove(ban_choice)

# The two players take turns picking from the list of available characters
drafted_characters = []
for i in range(2):
    print(f"{first_picker}, choose a character:")
    pick_choice = input()
    drafted_characters.append(pick_choice)
    characters.remove(pick_choice)
    
    print(f"{second_picker}, choose a character:")
    pick_choice = input()
    drafted_characters.append(pick_choice)
    characters.remove(pick_choice)

print("Draft phase complete!")
print(f"{first_picker} drafted {drafted_characters[0]} and {second_picker} drafted {drafted_characters[1]}")
print(f"{second_picker} drafted {drafted_characters[2]} and {first_picker} drafted {drafted_characters[3]}")
