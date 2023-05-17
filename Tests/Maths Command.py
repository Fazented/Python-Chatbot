
choice = input("What do you want me to do? ").lower()

if "math" in choice:
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