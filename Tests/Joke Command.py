from random import randint
import time

randomizer = randint(1,6)

choice = input("What do you want me to do? ").lower()

if "joke" in choice :
    if randomizer == 1:
        print("What do you call a fish with no eyes?")
        time.sleep(1)
        print("A fsh!")
    elif randomizer == 2:
        print("What do you call a can opener that doesn't work?")
        time.sleep(1)
        print("A can't opener!")
    elif randomizer == 3:
        print("What do you get when you combine a rhetorical question and a joke?")
        time.sleep(1)
        print("...")
    elif randomizer == 4:
        print("Did you hear about the italian chef that died?")
        time.sleep(1)
        print("He pasta way")
    elif randomizer == 5:
        print("A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”")
        time.sleep(1)
        print("The doctor replies “Sorry, I don't follow you.”")
    elif randomizer == 6:
        print("What did the left eye say to the right eye?")
        time.sleep(1)
        print("Between you and me, something smells.") 