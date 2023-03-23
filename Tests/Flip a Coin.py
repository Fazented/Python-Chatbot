from random import randint
import time

choice = input("What do you want me to do? ").lower()


coinflip = randint(1,2)

if "coin" in choice:
    print("Okay, Flipping a coin.")
    time.sleep(1)
    if coinflip == 1:
        print("The coin is Tails.")
    else:
        print("The coin is Heads.")
else:
    print("Error")



