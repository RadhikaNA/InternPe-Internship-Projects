import random

#Define a list of promots and their corresponding resposes
promots={
    "hi":["Hello!","Hi there!","Hey!"],
    "who are you":["I'm a chatbot!","You can call me ChatBot."],
    "what is your name":["I'm a chatbot!","chatbot"]
}
def get_response(message):
    #convert the message to lowercase
    message = message.lower()

    #check if the message matches any of the prompts
    for promt,responses in promots.items():
        if promt in message:
            return random.choice(responses)
        
    #If no promt matches, return a default responses
    return random.choice(promots["default"])

#Main loop
while True:
    user_input=input("User: ")
    response = get_response(user_input)
    print("ChatBot:", response)
