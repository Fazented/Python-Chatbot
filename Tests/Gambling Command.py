from random import randint
import colorama
from colorama import Fore

money = 1000
StillGambling = True

print(Fore.GREEN + "You Have $", money)
print(Fore.WHITE)

while StillGambling == True:
    GambleAmount = input("How much money do you want to gamble? ")
    chance = randint(1,10)
    if GambleAmount.isdigit():
        GambleAmount = int(GambleAmount)
        if chance == randint(1,10):
            print("You Won", GambleAmount * 2)
        else:
            print("You lost", GambleAmount)
    else:
        print("Please enter a whole number next time.")