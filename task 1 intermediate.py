import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'i am (good|well)', ['That\'s great to hear!', 'Awesome!']),
    (r'i am (bad|not good)', ['I\'m sorry to hear that. How can I help?', 'Is there anything I can do to make you feel better?']),
    (r'(.*) your name?', ['My name is Chatbot.', 'I am just a chatbot.']),
    (r'(.*) (age|old) are you?', ['I am a computer program, so I don\'t have an age.']),
    (r'(.*) (do for a living|work)', ['I am designed to chat with humans.', 'I am here to assist you with your queries.']),
    (r'(.*) (weather|temperature) (.*)', ['I am sorry, I am not capable of providing weather information at the moment.']),
    (r'quit', ['Bye!', 'Goodbye!', 'See you later.']),
]

# Create a Chat object
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Welcome! I am an AI Chatbot. You can start chatting with me. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
