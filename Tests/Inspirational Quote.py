import inspirobot
from PIL import Image
import requests

choice = input("What do you want me to do? ").lower()

if "quote" in choice :
    quote = inspirobot.generate()
    #print(quote.url)
    img_url = quote.url
    img = Image.open(requests.get(img_url, stream = True).raw)
    img.save('tests\inspiration.jpg')
    img.show()
else:
    print("Error")
