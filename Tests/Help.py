commandlist = ["Joke", "Flip a Coin", "Weather", "Gambling", "Hangman", "Day", "Inspirational Quote", "Help" ] # List of commands for help command

choice = input("What do you want me to do? ").lower()

if "help" in choice:
    print(f"What command do you want to know about? There are currently {len(commandlist)} commands.")
    for index, x in enumerate(commandlist): # this code is from https://stackoverflow.com/questions/72497658/how-do-i-add-and-at-the-end-of-the-list-element
        if index != len(commandlist)-1:     # because I spent a whole lesson on this and this code is so simple and good, I had just given up and used this: print(*commandlist, sep = ", ")
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