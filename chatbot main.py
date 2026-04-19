#Rule Based Chatbot in Python
import datetime
import time
name = input("Welcome to our Chatbot Service! Please enter your name:")
present_time = datetime.datetime.now().hour
if present_time < 12:
    print(f"Good Morning {name}!")
elif present_time < 17:
    print(f"Good Afternoon {name}!")
else:
    print(f"Good evening {name}!")


print("Namaste! Welcome to your chatbuddy")
print("How can i help you today? Type \"Bye\" to exit from the bot")

responses = {

    "hello" : "Hi there! How can i assist you today?",
    "how are you": "I'm doing great, how are you doing?",
    "who are you?": "I am a smart AI chatbuddy designed to help you with your queries.",
    "motivate": "Believe in yourself and remember that no one is defeated unless they accept defeat from within",
    "what is programming?": "It is creating a set of instructions that tells a computer how to perform a task.",
    "what is python?": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    "what is machine learning?": "Machine learning is a subset of artificial intelligence that enables computers to learn from data and improve their performance without being explicitly programmed.",
    "what is artificial intelligence?": "Artificial intelligence is the science and engineering of imparting human-like resononing and decision-making capabilities to machines.",
    "what are types of AI?": "There are three types of AI: Narrow AI, GeneralAI and Super AI.",
    "what is super AI?": "Super AI is a theoretical concept that surpasses all human intelligence combined, capable of performing any intellectual task that a human can do and much more.",
    "happy": "Great to hear that! Keep smiling and spreading positivity!",
    "sad": "I'm sorry to hear that. Remember, it's okay to feel sad sometimes. If you want to talk about it, I'm here to listen.",
    "thank you": "You're welcome! If you have any more questions, feel free to ask."
}

# Respond to user
def respondto_user(user_input):
    user_input = user_input.lower()
    for eachkey in responses:
        if eachkey in user_input:
            return responses[eachkey]
    
    return "Sorry i don't understand it yet, but i am learning every day to understand more and more queries."

# Take user input
while True:
    user_input = input("You: ")
    response = respondto_user(user_input)
    time.sleep(1) #Simulate thinking time
    print("Chatbuddy:", response)
    if "bye" in user_input.lower():
        print("Chatbuddy: Goodbye! Have a great day!")
        break
   
   
  