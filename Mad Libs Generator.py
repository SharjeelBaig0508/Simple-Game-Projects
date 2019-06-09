# made by SharjeelBaig0508
#
# Mad Libs Generator
import random

phrases = ["""
I want to be the very {0},
Like no one ever was.
To {1} them is my {2},
To {3} them is my {4}!
(I will {1} across the land,
{3} far and wide.
Each {5} to understand
The {6} that's inside!)
{5}!
Gotta {1} em' all!
"""
]

choice = random.randint(0, len(phrases) - 1)

phrase = phrases[choice]

print(phrase.replace("{}", "______"))

print()

adjective = input("Enter an Adjective >>> ")

verb = input("Enter an Action >>> ")

purpose = input("For what purpose are you going to " + verb + " >>> ")

verb1 = input("Enter another Action >>> ")

purpose1 = input("For what purpose are you going to " + verb1 + " >>> ")

creature = input("Enter the name of any creature >>> ")

ability = input("Enter an ability of " + creature + " >>> ")

print()

print(phrase.format(adjective, verb, purpose, verb1, purpose1, creature, ability))