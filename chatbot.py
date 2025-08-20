import nltk
import random
import string
import re

# Download the necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Predefined patterns and responses
patterns = {
    "greeting": ["hello", "hi", "greetings", "sup", "what's up"],
    "goodbye": ["bye", "farewell", "see you later"],
    "thanks": ["thank you", "thanks", "appreciate it"],
    "name": ["what is your name", "who are you", "can you tell me your name", "what should I call you"],
    "default": ["I'm sorry, I don't understand that."]
}

responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "name": ["I'm a chatbot created to assist you.", "I am a virtual assistant."],
    "default": ["I'm sorry, I don't understand that."]
}

# Function to preprocess user input
def preprocess_input(user_input):
    user_input = user_input.lower()  # Convert to lowercase
    user_input = re.sub(f"[{string.punctuation}]", "", user_input)  # Remove punctuation
    return user_input

# Function to get a response based on user input
def get_response(user_input):
    user_input = preprocess_input(user_input)
    
    for key, value in patterns.items():
        # Check if any of the patterns match the user input
        if any(re.search(r'\b' + re.escape(v) + r'\b', user_input) for v in value):
            return random.choice(responses[key])
    
    # Additional flexible matching for the "name" intent
    if "name" in user_input or "who" in user_input:
        return random.choice(responses["name"])
    
    return random.choice(responses["default"])

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hello! I'm here to help you. Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()