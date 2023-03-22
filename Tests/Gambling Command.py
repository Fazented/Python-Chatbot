from random import randint
import colorama
from colorama import Fore

money = 1000
StillGambling = True

print(Fore.WHITE)
print(Fore.GREEN + "You Have $", money)
print(Fore.WHITE)

while StillGambling == True:
    GambleAmount = input("How much money do you want to gamble? ")
    chance = randint(1,10)
    if GambleAmount.isdigit():
        GambleAmount = int(GambleAmount)
        if GambleAmount < money and chance == 6:
            print("You Won", GambleAmount * 2,"!")
            print(Fore.GREEN + "You now Have $", GambleAmount + money)
            print(Fore.WHITE)
        elif GambleAmount > money:
            print(Fore.RED + "You don't have enough money for that.")
            print(Fore.WHITE)
        elif GambleAmount < money and chance != 6:
            print("You lost", GambleAmount)
            print(Fore.GREEN + "You now Have $", money - GambleAmount)
            print(Fore.WHITE)
        else:
            print("Sorry, Please Try Again")
    else:
        print("Please enter a whole number next time.")