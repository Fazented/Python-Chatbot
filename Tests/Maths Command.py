
choice = input("What do you want me to do? ").lower()

if "math" in choice:
    print("What operation do you want to use? ")
    print("You can use addition, subtraction, multiplication and division.")
    choice = input("")
    if "add" in choice:
        x = int(input("Enter the fist number you want to add: "))
        y = int(input("What is the second number "))
        print("The answer is", x+y)
    elif "subtract" in choice:
        while True:
            try:
                x = int(input("Enter the first number you want to add: "))
                y = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Sorry, That is not a valid number!")
        print("The answer is", x+y)
    elif "multiply" in choice or "multiplication" in choice:
        int(input(""))
    elif "divide" in choice or "division" in choice:
        int(input(""))
    else:
        print("Error")