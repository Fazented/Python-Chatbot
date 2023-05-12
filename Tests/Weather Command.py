# import the module
import python_weather
import asyncio
import os
from datetime import datetime
 
today = datetime.today()

# PRETTY MUCH ALL OF THIS CODE IS FROM PYTHON-WEATHER, EXCEPT FOR THE DATETIME PART AND THE OUTPUT

location = input("What place do you want the weather from? ")

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