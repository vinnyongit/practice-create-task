selections = ["Rock", "Paper", "Scissors"]
player_selection = input("Would you like to select Rock, Paper, or Scissors?")
import random
ai_selection = random.choice(selections)
print("Your opponent selected " + ai_selection + "!")
if (ai_selection == "Rock"):
    if (player_selection == "Paper"):
        print("You won!") 
    if (player_selection == "Scissors"):
        print("You lost!")
    if (player_selection == "Rock"):
        print("Tie!")
if (ai_selection == "Paper"):
    if (player_selection == "Paper"):
        print("Tie!") 
    if (player_selection == "Scissors"):
        print("You won!")
    if (player_selection == "Rock"):
        print("You lost!")
if (ai_selection == "Scissors"):
    if (player_selection == "Paper"):
        print("You lost!") 
    if (player_selection == "Scissors"):
        print("Tie!")
    if (player_selection == "Rock"):
        print("You Won!")
