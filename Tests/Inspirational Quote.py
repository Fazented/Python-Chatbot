
import inspirobot


choice = input("What do you want me to do? ").lower()

if "quote" in choice :
    quote = inspirobot.generate()
    print(quote.url) # I am working on a way to display this image 
else:
    print("error")