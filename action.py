import speech_to_text
import text_to_speech
import datetime
import webbrowser
import weather

def Action(data):
    user_data=data.lower()
    if  "your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return "My name is Virtual Assistant"
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hai,sir how can i help you")
        return "Hai,sir how can i help you"
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning sir")
        return "Good morning sir"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time=(str)(current_time)+"Hour:",(str)(current_time.minute)+"minute"
        text_to_speech.text_to_speech(Time)
        return Time
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok bye")
        return "ok bye"
    elif "play music" in user_data:
        webbrowser.open("https://www.gaana.com/")
        text_to_speech.text_to_speech("gaana.com is now ready for you")
        return "gaana.com is now ready for you"
    elif "play videos" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"
    elif "search" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"
    elif "weather" in user_data:
        city = user_data.replace("weather", "").strip()
        if city == "":
            city = speech_to_text.speech_to_text()
        ans = weather.weather(city)
        return ans
    else:
        text_to_speech.text_to_speech("I'm sorry, but I don't understand you")
        return "I'm sorry, but I don't understand you"


