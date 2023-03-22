from random import randint
from colorama import Fore

money = 1000
StillGambling = True

print(Fore.WHITE)
print(Fore.GREEN + f"You Have ${money}")
print(Fore.WHITE)

while StillGambling == True:
    GambleAmount = input(Fore.WHITE + "How much money do you want to gamble? ")
    chance = randint(1,6)
    if GambleAmount.isdigit():
        GambleAmount = int(GambleAmount)
        if GambleAmount <= money and chance == 6:
            GambleAmount*=2
            print(f"You Won ${GambleAmount}")
            GambleAmount += money
            print(Fore.GREEN + f"You now Have ${money}")
            print(Fore.WHITE)
        elif GambleAmount > money:
            print(Fore.RED + "You don't have enough money for that.")
            print(Fore.WHITE)
        elif GambleAmount <= money and chance != 6:
            print(f"You lost ${GambleAmount}!")
            money -= GambleAmount
            print(Fore.GREEN + f"You now Have ${money}")
            print(Fore.WHITE)
        else:
            print("Sorry, Please Try Again")
    else:
        print("Please enter a whole number next time.")