import speech_recognition as sr
import pyttsx3
import time
import re
import json

# Load responses from JSON file
with open("responses.json", "r") as f:
    responses = json.load(f)

def speak(text):
    engine = pyttsx3.init(driverName='sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def chatbot_response(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)  # remove punctuation
    for key in responses:
        if key in user_input:  # fuzzy match
            return responses[key]
    return "Sorry, I don't understand that yet, but I'm learning more every day."

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        reply = chatbot_response(text)
        print("Bot:", reply)
        speak(reply)

        if "bye" in text.lower():
            break

        time.sleep(0.5)

    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
    except sr.RequestError:
        speak("Could not request results; please check your internet connection.")
