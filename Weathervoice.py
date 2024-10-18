import requests  # to access data over the network
import json  # for parsing JSON data
import pyttsx3  # for text-to-speech

# Initialize the TTS engine
engine = pyttsx3.init()

while True:
    # Input city name from the user
    city = input("Enter the name of the city\n")

    # URL for the Weather API (replace with your API key)
    url = f"https://api.weatherapi.com/v1/current.json?key=215d0ff840b9429f845110114241710&q={city}"

    # Make the request to the API
    r = requests.get(url)

    # Load the response into a dictionary
    wdictionnary = json.loads(r.text)

    # Check if the 'current' key exists in the API response
    if 'current' in wdictionnary:
        # Extracting weather information from the API response
        w = wdictionnary["current"]["temp_c"]  # Current temperature
        c = wdictionnary["current"]["condition"]["text"]  # Weather condition

        # Make the bot speak the weather information
        engine.say(f"The current weather in {city} is {w} degrees and weather condition in {city} is {c}")
        engine.runAndWait()
    else:
        # Handle the error if 'current' key is missing (e.g., invalid city name)
        engine.say(f"Sorry, I couldn't find weather information for {city}. Please check the city name and try again.")
        engine.runAndWait()
        print("Error: Could not find 'current' in the API response. Please check the city name.")
        break