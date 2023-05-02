import random

greetings = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'ciao']

question = ['how do you do?', 'how are you?', 'are you okay?']

responses = ['Okay', 'I am fine', 'I am okay', 'I am good']

def greeting(sentence):
  for word in sentence.split():
    if word.lower() in greetings:
      return random.choice(greetings)

def respond(sentence):
  for word in sentence.split():
    if word.lower() in question:
      return random.choice(responses)

def generate_response(sentence):
  if greeting(sentence) is not None:
    return greeting(sentence)
  elif respond(sentence) is not None:
    return respond(sentence)
  else:
    return "I'm sorry, I don't understand what you're saying."

print(generate_response("Hello there!"))
print(generate_response("How are you today?"))
print(generate_response("I'm not sure what you mean."))
