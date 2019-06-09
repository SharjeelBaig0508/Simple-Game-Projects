# made by SharjeelBaig0508
#
# A dice rolling app

import random

def dice_roller(min, max):
	return random.randint(min, max)
	
while True:
	print(dice_roller(1, 6))
	repeat = input("Do you want to roll again ([Y]/N) ? >>> ")
	if repeat == 'N' or repeat == 'N':
		break

