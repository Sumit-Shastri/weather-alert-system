"""
-------------------------------------------------------------------------------------------
    Imports
-------------------------------------------------------------------------------------------
"""
import requests
from dotenv import load_dotenv
import os
import sys
import json

"""
-------------------------------------------------------------------------------------------
    Methods
-------------------------------------------------------------------------------------------
"""


"""
-------------------------------------------------------------------------------------------
    Method name : weatherAlert()
-------------------------------------------------------------------------------------------
"""

def weatherAlert(url, parameters, userLoc):
    r = requests.get(url, params = parameters)
    data = r.json()
    pretty_data = json.dumps(data, indent = 4)
    #print(pretty_data)

    #print("code : ",data['cod'])
    code = data['cod']

    if code == "404":
        print("City not found, Try again")
        return 1

    else:
        temperature = (data['main'])['temp']
        humidity = (data['main'])['humidity']
        condition = ((data['weather'])[0])['main']

        print(f"----  Weather report for {userLoc}  ----\n\n")
        #print(pretty_data)
        print(f"Temperature : {temperature}")
        print(f"Humidity : {humidity}")
        print(f"Condition : {condition}\n")

        if temperature >= 35:
            print("Warning : Tempearature too high , stay hydrated.")
        elif temperature <= 12:
            print("Warming : Temperature too low , keep yourself warm")

"""
-------------------------------------------------------------------------------------------
    Main
-------------------------------------------------------------------------------------------
"""

url = "https://api.openweathermap.org/data/2.5/weather"

# loading Weather api key in API_KEY
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


# get city name from command line arguments

if len(sys.argv) < 2:
    print("Print give city name.")
    print("Usage : python weatherAlertSystem.py <cityname>")
    sys.exit()

userLoc = sys.argv[1]

params = {
    "q" : userLoc,
    "appid" : API_KEY,
    "units" : "metric"
}

weatherAlert(url, params, userLoc)

"""
-------------------------------------------------------------------------------------------
    END
-------------------------------------------------------------------------------------------
"""
