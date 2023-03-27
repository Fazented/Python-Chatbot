import inspirobot
from PIL import Image
import requests

loop = True

while loop == True:
    choice = input("What do you want me to do? ").lower()
    if "quote" in choice :
        quote = inspirobot.generate()
        img_url = quote.url
        img = Image.open(requests.get(img_url, stream = True).raw)
        img.save('tests\inspiration.jpg')
        img.show()
    elif "exit" in choice:
        print("Okay, Exiting Program")
        loop = False
    else:
        print("Error")
