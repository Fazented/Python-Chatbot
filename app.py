from random import randint # importing all the packages
import random
import time
import inspirobot
from PIL import Image
import requests
import python_weather
import asyncio
import os
import datetime

commandlist = ["Joke", "Flip a Coin", "Weather", "Gambling", "Hangman", "Day", "Inspirational Quote", "Help" ] # List of commands for help command
words = ["python", "computer", "programming", "code", "algorithm"] # words to guess in Hangman

today = datetime.today() # Gets the current day for weather and day command
gamblingchance = randint(1,20) # Chance to score a win while gambling
money = 1000 # Amount of money to start gambling

# Defining all commands
def joke():

    randomizer = randint(1,6)
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
 
def flipcoin():

    coinflip = randint(1,2)
    coinside = randint(1,100) # A joke, to make a 1 in 200 chance for a coin to land on it's side

    print("Okay, Flipping a coin.")
    time.sleep(1)
    if coinflip == 1 and coinside == 69:
        print("\nThat's odd, the coin landed on it's side! Heads AND Tails!")
    elif coinflip == 1:
        print("\nThe coin is Tails.")
    else:
        print("\nThe coin is Heads.")

def weather():

    location = input("What place do you want the weather from? ")

    async def getweather():
        async with python_weather.Client(format=python_weather.METRIC) as client:

            # taking weather for a city
            weather = await client.get(location)
  
            # returns the current temperature (int)
            print(f"The current temperature on {today:%B %d} is {weather.current.temperature}°")
            # get the weather forecast for a few days

    if __name__ == "__main__":
        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())

def gambling():

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

def hangman():

    guesses = ""
    turns = 10
    word = random.choice(words)

    while turns > 0:
        failedwords = 0
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failedwords += 1

        if failedwords == 0:
            print("")
            print("You won the game!")
            break
        guess = input("\n\nGuess a character: ")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Incorrect")
            print(f"You have {turns} turns left.")
            if turns == 0:
                print("You lost the game.")
                print("The word was", word)
    else:
        print("Error")

def day():

    today = datetime.today()
    print("Today is", today)

def quote():

    quote = inspirobot.generate()
    img_url = quote.url
    img = Image.open(requests.get(img_url, stream = True).raw)
    img.save('inspiration.jpg')
    img.show()

def help():


print("Hello, I am Sadness Bot. An eternally sad chatbot. Use 'Help' to see a list of commands.")
choice = input("What do you want me to do? ")









