from random import randint # importing all the packages
import random
import time
import inspirobot
from PIL import Image
import requests
import python_weather
import asyncio
import os
from datetime import datetime

commandlist = ["Chat", "Joke", "Flip a Coin", "Weather", "Gambling", "Hangman", "Day", "Maths", "Inspirational Quote", "Help" ] # List of commands for help command
words = ["python", "computer", "programming", "code", "algorithm", "coder", "school"] # words to guess in Hangman

# Lists of words for the chat part to recognise
greetings = ["hello", "hi", "yo", "greeting", "howdy", "hey", "bonjour"] # List of greetings
bad_feeling = ["bad", "not good", "sad", "depressed", "angry", "annoying", "not good", "not feeling good", "not happy", "", "", ] # List of replies to detect bad feelings
good_feeling = ["good", "happy", "joy", "great", "wonderful", "", "", "", "", "", "", ]
colours = ["red", "orange", "yellow", "green", "purple", "blue", "light blue", "pink", "gray", "grey", "indigo", "turquoise", "black", "white", "navy", "brown", "maroon", "aqua", "light gray", "light grey", "dark gray", "dark grey", "dark green", "tan", ""] # List of coulours for the bot to recognise, incase an input includes other words

turns = 10 # Amount of turns for hangman, here because it's referenced by help command
word = random.choice(words) #Picks a random word for hangman
gamblingchance = randint(1,20) # Chance to score a win while gambling
money = 1000 # Amount of money to start gambling
running = True # loops the chatbot

# Defining the actual chat part of chatbot
def chat():

    print("Hello, what is your name?")
    name = input("> ")

    name = name.removeprefix("my name is ")

    print(f"How are you {name}?")
    feeling = input("> ")

    # Will reply to the users emotions
    if feeling in good_feeling:
        print("That's great, good to hear that.")
    elif feeling in bad_feeling:
        print("That's not good, I hope you feel better soon!")
    else:
        print("Cool!")
    
    print("What is your favourite colour?")
    colour = input("> ").lower()

    colour = colour.removeprefix("my favourite colour is")

    if colour in colours:
        print(f"Cool! I love {colour}, got to be one of my favourites")
    else:
        print("Good choice!")

# Defining all commands
def joke():

    randomizer = randint(1,6) # Randomizes responses for jokes

    # Could add jokes in a list, but I want the delay between them and this is easier
    if randomizer == 1:
        print("What do you call a fish with no eyes?")
        time.sleep(1)
        print("\nA fsh!")
    
    elif randomizer == 2:
        print("What do you call a can opener that doesn't work?")
        time.sleep(1)
        print("\nA can't opener!") # My fav joke :)
    
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

    quote = inspirobot.generate() # Generates a quote and puts the url to quote.url

    img_url = quote.url # Saves the link to a variable that Pillow can use

    img = Image.open(requests.get(img_url, stream = True).raw) #Opens the image from the url
    img.save('inspiration.jpg') # Downloads the image

    img.show() # Shows the image

def weather():

    today = datetime.today() # Gets the current day for weather
    print("What place do you want the weather from?")
    location = input("> ")

    async def getweather():
        async with python_weather.Client(format=python_weather.METRIC) as client:

            # taking weather for a city
            weather = await client.get(location)
  
            # returns the current temperature (int)
            print(f"The current temperature on {today:%B %d} is {weather.current.temperature}°")

    if __name__ == "__main__":
        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())

def gambling():

    money = 1000 # Amount of money to start gambling

    while money > 0:
        print(f"You Have ${money}")
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

        guess = input("\nGuess a character: ")
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
    print(f"Today is {today:%B %d}")

def maths():

    while True:
        print("\nWhat operation do you want to use? ")
        print("You can use addition, subtraction, multiplication and division.")

        choice = input("> ")
        
        if "add" in choice or "subtract" in choice or "multiply" in choice or "divide" in choice:
            break
        elif "quit" in choice or "exit" in choice:
            print("Exiting...")
            break
        else:
            print("Error, not an operation. Type exit or quit to leave.")

    if "add" in choice:
        while True:
            try: # Will try to take in a number, or it will come with an error.
                x = int(input("Enter the first number you want to add: "))
                y = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Sorry, That is not a valid number!")
                continue
        print(f"The answer is {x+y}")

    elif "subtract" in choice or "minus" in choice:
        while True:
            try:
                x = int(input("Enter the first number you want to subtract: "))
                y = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Sorry, That is not a valid number!")
                continue
        print(f"The answer is {x-y}")

    elif "multiply" in choice or "multiplication" in choice:
        while True:
            try:
                x = int(input("Enter the first number you want to multiply: "))
                y = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Sorry, That is not a valid number!")
                continue
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

    else:
        print("Error, enter a correct operation. Or, type exit or quit to leave.")

def random_command():

    selectedcommand = random.choice(commandlist) # Will take a random command from the list

    print(f"The command selected is {selectedcommand}")

    if "help" in selectedcommand.lower(): # Added the .lower() because The list is for help command, and it is capitalised
        help()
    elif "joke" in selectedcommand.lower():
        joke()
    elif "coin" in selectedcommand.lower():
        flipcoin()
    elif "quote" in selectedcommand.lower():
        quote()
    elif "weather" in selectedcommand.lower():
        weather()
    elif "gambling" in selectedcommand.lower():
        gambling()
    elif "hangman" in selectedcommand.lower():
        hangman()
    elif "day" in selectedcommand.lower():
        day()
    elif "math" in selectedcommand.lower():
        maths()
    else:
        print("Error!")  

def help():

    print(f"What command do you want to know about? There are currently {len(commandlist)} commands.")

    for index, x in enumerate(commandlist): # this code is from https://stackoverflow.com/questions/72497658/how-do-i-add-and-at-the-end-of-the-list-element
        if index != len(commandlist)-1:     # because I spent a lesson on this and this code is simple
            print("{}, ".format(x), end = "");
        else:
            print("and {}.".format(x), end = "");
    
    choice = input("\nHelp: ").lower()
    
    if "joke" in choice:
        print("The Joke command will tell you a random joke when you ask.")

    elif "coin" in choice or "flip" in choice:
        print("The Flip a Coin command will flip a coin and return either Heads or Tails.")

    elif "weather" in choice:
        print("The Weather command will return the temperature of an inputted ")

    elif "gambling" in choice or "gamble" in choice:
        print("The Gambling command will give you a set abount of money to gamble, and you have to pick an amount of money to gamble. There is a small chance you win back your money and more, but be careful you do not gamble all your money away too soon!")

    elif "hangman" in choice:
        print(f"The hangman command will make a game of hangman for 1 or 2 players, where a friend will input a word or the program and you have to guess the word within {turns} guesses.")

    elif "quote" in choice:
        print("The Quote command will get a random inspirational quote from InspiroBot. These quotes may be very strange though, so beware!")

    elif "help" in choice:
        print("I would assume the help command would be simple, but I guess not...")
    
    elif "maths" in choice:
        print("The maths command with add, subtract, divide or multiply 2 numbers.")

    elif "random" in choice:
        print("Will run a random command, can even run itself!")

    elif "day" in choice:
        print("The day command returns the current day.")

    else:
        print("Error! That is not a real command!")

# Main Chatbot (finally)

print("Hello, I am Sadness Bot. An eternally sad chatbot. Use 'Help' to see a list of commands.")

# Main chatbot loop
while running == True:
    user_choice = input("> ").lower()

    if user_choice in greetings:
        chat()
    elif "joke" in user_choice:
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
