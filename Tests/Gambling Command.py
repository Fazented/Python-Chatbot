from random import randint
import random

money = 1000
gamblingchance = randint(1,20) # Chance to score a win while gambling

while money > 0:
    print("You have", money)
    bet = input("\nHow much do you want to bet? ")
    if bet.isdigit():   
        bet = int(bet)
        if bet * 2 > money:
            print("You don't have enough money for that. If you are out of money, type exit to stop gambling.")
        elif bet < money:
            bet = bet * 2
            if gamblingchance == 1:
                print(f"You won! ${bet}")
                money = money + bet
            else:
                print(f"You lost ${bet}!")
                money = money - bet
        else:
            print("You don't have enough money for that.")
    elif "exit" in bet:
        break
    else:
        print("Sorry, that is not a valid number")

print("GAME OVER.")
