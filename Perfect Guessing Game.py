# Produced by Mohammad Sharjeel Baig
# Inspired by Harvest Moon: Friends of the Mineral Town Gameboy Advance Rom

import random

# Introduction of the game

print("+" + "-" * 58 + "+")
print("|" + "\t" * 2 + "    Python Guessing Game                   " + "|")
print("+" + "-" * 58 + "+")

print("Hey! Welcome to this awesome guessing game.\n")

# How to play

print("In this game, first I will give you a number then you will \nguess whether the next one is higher or lower.\n")

# Getting started

print("Ok? So let's get started\n")

print("+" + "-" * 58 + "+\n")

difficulty = [ 25, 50, 100]
enterence = 1
difficulty_level = 1

# difficulty level setter

print("Choose the difficulty level\nInput only these 3 nmbers : ")
while (difficulty_level > 3 or difficulty_level <= 0) or enterence == 1 :
    difficulty_level = int(input("1: Easy\n2: Normal\n3: Hard >>> "))
    enterence -= 1

# The game starts

print("\n+" + "-" * 58 + "+\n")

# Generating a random number
hidden_number = random.randint(0, 9)
print("My number is : \n")
print((str(hidden_number) * 60 + "\n") * 5)

hit = 0
hits_to_win = difficulty[difficulty_level - 1]
miss = False

# Loop starts

while hit < hits_to_win and not(miss) :
    shown_number = hidden_number
    hidden_number = random.randint(0, 9)
    
    # User chooses
    
    choice = input("Now guess, the next number is higher or lower ? (Only type\n\"higher\" and \"lower\" >>> ")
    
    # Shows the hidden number
    
    print("\n+" + "-" * 58 + "+\n")
    print("Hidden Number was : \n")
    print((str(hidden_number) * 60 + "\n") * 5)
    
    # Checking that the choice was True or not
    
    if hidden_number < shown_number:
    	if choice in "HIGHERhigherHigher":
    		miss = True
    		print("Wrong!\n")
    	elif choice in "LOWERlowerLower":
    		print("Good Job! It's a hit!\n")
    		hit += 1
    	else:
    		print("Wrong Input!\nOnly type \"higher\" or \"lower\" \n")
    elif hidden_number > shown_number:
    	if choice in "HIGHERhigherHigher":
    		print("Good Job! It's a hit!\n")
    		hit += 1
    	elif choice in "LOWERlowerLower":
    		miss = True
    		print("Wrong!\n")
    	else:
    		print("Wrong Input!\nOnly type \"higher\" or \"lower\" \n")
    else:
    	print("It's a same number\n")
    	print("Let's try another one.\n")

# Out of loop
# Check that the user is winner or loser
print("+" + "-" * 58 + "+\n")
if miss :
	print("Sorry! You lost!\n")
	print("Your hit points were", hit)
	print("\nBetter Luck! Next time.\n")
	print("You lost by", hits_to_win - hit)
else:
	print("Congratulations! You are a winner!\n")
	print("You won with a perfect hit points of", hit)

print("\n+" + "-" * 58 + "+\n")

# End of Game
