import speech_recognition as sr
import pyttsx3
import time

# Dictionary of responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm doing great, how are you doing?",
    "who are you?": "I am a smart AI chatbuddy designed to help you with your queries.",
    "motivate": "Believe in yourself and remember that no one is defeated unless they accept defeat from within",
    "what is programming?": "It is creating a set of instructions that tells a computer how to perform a task.",
    "what is python?": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    "what is machine learning?": "Machine learning is a subset of artificial intelligence that enables computers to learn from data and improve their performance without being explicitly programmed.",
    "what is artificial intelligence?": "Artificial intelligence is the science and engineering of imparting human-like reasoning and decision-making capabilities to machines.",
    "what are types of ai?": "There are three types of AI: Narrow AI, General AI and Super AI.",
    "what is super ai?": "Super AI is a theoretical concept that surpasses all human intelligence combined, capable of performing any intellectual task that a human can do and much more.",
    "happy": "Great to hear that! Keep smiling and spreading positivity!",
    "sad": "I'm sorry to hear that. Remember, it's okay to feel sad sometimes. If you want to talk about it, I'm here to listen.",
    "thank you": "You're welcome! If you have any more questions, feel free to ask.",
    "bye": "Goodbye! Have a great day!"
}

# Speak function
def speak(text):
    engine = pyttsx3.init(driverName='sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "Sorry, I don't understand that yet, but I am learning more every day."

# Recognizer
recognizer = sr.Recognizer()

# Continuous loop
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

