def simple_chatbot(user_input):

    # Predefined rules and responses--------------------------------------
    greetings = ['hello', 'hi', 'hey']
    farewells = ['bye', 'goodbye', 'see you']
    inquiries = ['how are you', 'what is your name', 'who are you']
    song = ['top songs', 'songs', 'suggest songs', 'hit songs', 'latest songs']
    instructions = ['tell me a joke', 'explain natural language processing', 'recommend a book']

    # Check user input against predefined rules--------------------------

    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I help you today?"

    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a great day!"

    elif any(inquiry in user_input for inquiry in inquiries):
        return "I'm just a simple chatbot. Ask me anything!"
        
    elif any(songs in user_input for songs in song):
        return "\n1. Heeriye\n2. Chaleya\n3. Restart - Rap 'N' Folk \n4. Apna Bana Le\n "

    elif any(instruction in user_input for instruction in instructions):
        return process_instruction(user_input)

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def process_instruction(instruction):
    if 'joke' in instruction:
        return "Why did the computer go to therapy? It had too many bytes of emotional baggage!"

    elif 'natural language processing' in instruction:
        return "Natural Language Processing (NLP) is a field of AI that focuses on the interaction between computers and humans using natural language."
    
    elif 'recommend a book' in instruction:
        return "I recommend 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams. It's a classic!"
   
    else:
        return "I'm not sure how to respond to that instruction. Ask me something else!"

# Interactive chatbot-----------------------------------------------------
print("Welcome to the Rule-Based Chatbot!")

while True:
    user_input = input("You: ").lower()

    if user_input == 'exit':
        print("Chatbot: Goodbye! If you have more questions, feel free to ask later.")
        break

    response = simple_chatbot(user_input)
    print("Chatbot:", response)
