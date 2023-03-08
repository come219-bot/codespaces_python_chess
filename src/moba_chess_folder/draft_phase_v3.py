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
while True:
    print(f"{winner}, do you want first pick or second pick?")
    pick_order = input().lower()

    if pick_order == "first":
        first_picker = winner
        second_picker = player2 if winner == player1 else player1
        break
    elif pick_order == "second":
        first_picker = player2 if winner == player1 else player1
        second_picker = winner
        break
    else:
        print("Invalid input! Please enter 'first' or 'second'.")

# Define the list of characters to choose from
characters = ["Character1", "Character2", "Character3", "Character4", "Character5", "bob", "prince", "james", "simon", "alice"]

# The two players take turns banning characters from the list
banned_characters = []

print("Characters: ")
for character in characters:
    print(character + ",        ")

for i in range(2):
    while True:
        print(f"{first_picker}, choose a character to ban:")
        ban_choice = input()
        
        if ban_choice.lower() in [c.lower() for c in characters]:
            banned_characters.append(ban_choice)
            characters.remove(ban_choice)
            break
        else:
            print(f"{ban_choice} is not a valid character! Please choose from the following characters: {', '.join(characters)}")
    
    while True:
        print(f"{second_picker}, choose a character to ban:")
        ban_choice = input()
        
        if ban_choice.lower() in [c.lower() for c in characters]:
            banned_characters.append(ban_choice)
            characters.remove(ban_choice)
            break
        else:
            print(f"{ban_choice} is not a valid character! Please choose from the following characters: {', '.join(characters)}")

print("Banned Characters: ")
for bannedcharacter in banned_characters:
    print(bannedcharacter + ",  ")

print("Characters: " + str(characters))


# The two players take turns picking from the list of available characters
drafted_characters = []
for i in range(2):
    while True:
        print(f"{first_picker}, choose a character:")
        pick_choice = input()
        
        if pick_choice.lower() in [c.lower() for c in characters]:
            drafted_characters.append(pick_choice)
            characters.remove(pick_choice)
            break
        else:
            print(f"{pick_choice} is not a valid character! Please choose from the following characters: {', '.join(characters)}")
    
    while True:
        print(f"{second_picker}, choose a character:")
        pick_choice = input()
        
        if pick_choice.lower() in [c.lower() for c in characters]:
            drafted_characters.append(pick_choice)
            characters.remove(pick_choice)
            break
        else:
            print(f"{pick_choice} is not a valid character! Please choose from the following characters: {', '.join(characters)}")

print("Draft phase complete!")
print(f"{first_picker} drafted {drafted_characters[0]} and {second_picker} drafted {drafted_characters[1]}")
print(f"{second_picker} drafted {drafted_characters[2]} and {first_picker} drafted {drafted_characters[3]}")
