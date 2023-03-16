from random import random
import colorama
from colorama import Fore

money = 1000
StillGambling = True

print(Fore.GREEN + "You Have $", money)
print(Fore.WHITE)

while StillGambling == True:
    GambleAmount = input("How much money do you want to gamble? ")
    if GambleAmount.isdigit():
        GambleAmount == int(GambleAmount)
        GambleAmount == GambleAmount * 2
        print(GambleAmount)
    else:
        print("Please enter a whole number next time.")