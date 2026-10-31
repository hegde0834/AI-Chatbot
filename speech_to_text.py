from importlib import import_module

def speech_to_text():
    try:
        sr = import_module("speech_recognition")
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "SpeechRecognition is not installed. Run: python -m pip install SpeechRecognition"
        ) from exc

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    try:
        voice_data = r.recognize_google(audio)
        return voice_data
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    except sr.RequestError:
        print("Request Error")
        return ""
