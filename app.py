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
words = ["python", "computer", "programming", "code", "algorithm", "coder", "school"] # words to guess in Hangman
# Lists of words for the chat part to recognise
greetings = ["hello", "hi", "yo", "greeting", "howdy", "hey", "bonjour"] # List of greetings
bad_feeling = ["", "", "", "", "", "", "", "", "", "", "", ] 

gamblingchance = randint(1,20) # Chance to score a win while gambling
money = 1000 # Amount of money to start gambling
running = True # loops the chatbot

# Defining the actual chat part of chatbot
def chat():

    print("Hello, what is your name?")
    name = input("> ")
    print(f"How are you {name}?")
    user_choice = input("> ")
    print("Not done yet")

# Defining all commands
def joke():

    randomizer = randint(1,6)
    if randomizer == 1:
        print("What do you call a fish with no eyes?")
        time.sleep(1)
        print("\nA fsh!")
    elif randomizer == 2:
        print("What do you call a can opener that doesn't work?")
        time.sleep(1)
        print("\nA can't opener!")
    elif randomizer == 3:
        print("What do you get when you combine a rhetorical question and a joke?")
        time.sleep(1)
        print("\n...")
    elif randomizer == 4:
        print("Did you hear about the italian chef that died?")
        time.sleep(1)
        print("\nHe pasta way")
    elif randomizer == 5:
        print("A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”")
        time.sleep(1)
        print("\nThe doctor replies “Sorry, I don't follow you.”")
    elif randomizer == 6:
        print("What did the left eye say to the right eye?")
        time.sleep(1)
        print("\nBetween you and me, something smells.") 
 
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

def quote():

    quote = inspirobot.generate()
    img_url = quote.url
    img = Image.open(requests.get(img_url, stream = True).raw)
    img.save('inspiration.jpg')
    img.show()

def weather():

    today = datetime.today() # Gets the current day for weather
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
        guess = input("Guess a character: ")
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

def maths():

    print("What operation do you want to use? ")
    print("You can use addition, subtraction, multiplication and division.")
    choice = input("")
    if "add" in choice:
        while True:
            try:
                x = int(input("Enter the first number you want to add: "))
                y = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Sorry, That is not a valid number!")
        print(f"The answer is {x+y}")
    elif "subtract" in choice or "minus" in choice:
        while True:
            try:
                x = int(input("Enter the first number you want to subtract: "))
                y = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Sorry, That is not a valid number!")
        print(f"The answer is {x-y}")
    elif "multiply" in choice or "multiplication" in choice:
        while True:
            try:
                x = int(input("Enter the first number you want to multiply: "))
                y = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Sorry, That is not a valid number!")
        print(f"The answer is {x*y}")
    elif "divide" in choice or "division" in choice:
        while True:
            try:
                x = int(input("Enter the first number you want to divide: "))
                y = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Sorry, That is not a valid number!")
        print(f"The answer is {x/y}")
    elif "quit" in choice or "exit" in choice:
        print("Exiting Program")
        break
    else:
        print("Error, enter a correct operation. Or, type exit or quit to leave.")

def help():

    print(f"What command do you want to know about? There are currently {len(commandlist)} commands.")
    for index, x in enumerate(commandlist): # this code is from https://stackoverflow.com/questions/72497658/how-do-i-add-and-at-the-end-of-the-list-element
        if index != len(commandlist)-1:     # because I spent a whole lesson on this and this code is simple
            print("{}, ".format(x), end = "");
        else:
            print("and {}.".format(x), end = "");
    choice = input(" ").lower
    
    if "joke" in choice:
        print("The Joke command will tell you a random joke when you ask.")
    elif "coin" in choice or "flip" in choice:
        print("The Flip a Coin command will flip a coin and return either Heads or Tails.")
    elif "weather" in choice:
        print("The Weather command will return the temperature of an inputted ")
    elif "gambling" in choice or "gamble" in choice:
        print("The Gambling command will give you a set abount of money to gamble, and you have to pick an amount of money to gamble. There is a small chance you win back your money and more, but be careful you do not gamble all your money away too soon!")
    elif "hangman" in choice:
        print("The hangman command will make a game of hangman for 1 or 2 players, where a friend will input a word or the program and you have to guess the word within 10 guesses.")
    elif "quote" in choice:
        print("The Quote command will get a random inspirational quote from InspiroBot. These quotes may be very strange though, so beware!")
    elif "help" in choice:
        print("I would assume the help command would be simple, but I guess not...")
    elif "day" in choice:
        print("The day command returns the current day.")
    else:
        print("error")

print("Hello, I am Sadness Bot. An eternally sad chatbot. Use 'Help' to see a list of commands.")

# Main chatbot loop
while running == True:
    user_choice = input("> ").lower()

    if user_choice in greetings:
        chat()
    if "joke" in user_choice:
        joke()
    elif "coin" in user_choice:
        flipcoin()
    elif "quote" in user_choice:
        quote()
    elif "weather" in user_choice:
        weather()
    elif "gambling" in user_choice:
        gambling()
    elif "hangman" in user_choice:
        hangman()
    elif "day" in user_choice:
        day()
    elif "math" in user_choice:
        maths()
    elif "help" in user_choice:
        help()
    else:
        print("Sorry, that is not a valid command. Type 'Help' to see all usable commands.")
