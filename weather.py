import requests
import speech_to_text
import text_to_speech
import pyttsx3

def weather(city):

    if city:
        url = f"https://wttr.in/{city}?format=j1"

        try:
            data = requests.get(url).json()

            temp = data["current_condition"][0]["temp_C"]
            desc = data["current_condition"][0]["weatherDesc"][0]["value"]
            humidity = data["current_condition"][0]["humidity"]

            message = (
                f"The temperature in {city} is {temp}°C, "
                f"the weather is {desc}, "
                f"and humidity is {humidity}%"
            )


            engine = pyttsx3.init()
            engine.say(message)
            engine.runAndWait()


            return message

        except Exception as e:
            return f"Error: {e}"

    else:
        return "No city name detected"