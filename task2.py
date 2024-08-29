import random

def chatbot():
    print("🌟 Welcome! I am Chatty, the curious chatbot! What's on your mind today? 🌟")

    responses = {
        "greeting": [
            "Hello, human! 🌞 How can I brighten your day?",
            "Hi there! 🤖 What's up?",
            "Hey! Ready to chat about the wonders of the universe?"
        ],
        "how_are_you": [
            "I'm just a bunch of code, but if I could feel, I'd be fantastic! ✨ How about you?",
            "Doing binary-tastic! And you?",
            "Buzzing with ones and zeros! What's new with you?"
        ],
        "weather": [
            "I wish I could enjoy the weather! 🌦 But being a bot has its perks—no need for an umbrella!",
            "Sunny, rainy, or snowy, I'm always here! What's it like outside?",
            "Weather is a mystery to me! Can you describe it?"
        ],
        "name": [
            "I'm Chatty, your virtual companion! 🦄",
            "Call me Chatty, the friendly chatterbox! 💬",
            "I go by Chatty! What's your name?"
        ],
        "unknown": [
            "Hmm, that's a puzzler! 🧩 Can you tell me more?",
            "I'm not sure I understand, but I'm eager to learn! 🌈",
            "That sounds interesting! Could you explain a bit more?"
        ]
    }

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatty:", random.choice(responses["greeting"]))
        
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatty:", random.choice(responses["how_are_you"]))
        
        elif "weather" in user_input:
            print("Chatty:", random.choice(responses["weather"]))
        
        elif "name" in user_input:
            print("Chatty:", random.choice(responses["name"]))
        
        elif user_input in ["exit", "quit", "bye"]:
            print("Chatty: It was nice chatting with you! Stay curious! 🌟")
            break
        
        else:
            print("Chatty:", random.choice(responses["unknown"]))

if __name__ == "__main__":
    chatbot()
