import random

words = ["python", "computer", "programming", "code", "algorithm"]
word = random.choice(words)

guesses = ""
turns = 10

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