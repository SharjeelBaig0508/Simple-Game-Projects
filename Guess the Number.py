# made by SharjeelBaig0508
#
# Number Guessing Game

import random

def checker(user_number, my_number):
	if user_number > my_number:
		return ["\nToo high", False]
	elif user_number < my_number:
		return ["\nToo low", False]
	else:
		return ["\nGuessed it", True]
while True:
	count = 0
	max = random.randint(100, 1001)
	min = random.randint(0, (max -100))
	my_number = random.randint(min, max)
	
	while True:
		user_number = int(input("\nGuess the number\nHint : Its between {} to {} >>> ".format(min, max)))
		result = checker(user_number, my_number)
		print(result[0])
		if result[1]:
			break
		else:
			count += 1

	print("\nCongratulations! You've won!\n")
	print("You used {} guesses to win\n".format(count + 1))
	if input("Wanna Play Again ? >>> ") in "NOPESNEVERnopesneverNopesNever":
		break