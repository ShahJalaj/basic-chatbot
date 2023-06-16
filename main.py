import random

greetings = ['hello', 'hi', 'hey', 'howdy', 'hola']

question_words = ['who', 'what', 'when', 'where', 'why', 'how']

def respond_to_greeting(greeting):
    return random.choice(['hi there', 'hello', 'greetings', 'hey there'])

def respond_to_question(question):
    return "I'm sorry, I'm not capable of answering questions yet."

def respond(message):
    message = message.lower()
    words = message.split()
    for word in words:
        if word in greetings:
            return respond_to_greeting(word)
        elif word in question_words:
            return respond_to_question(message)
    return "I'm sorry, I didn't understand that."

while True:
    message = input('User: ')
    response = respond(message)
    print('Bot:', response)
