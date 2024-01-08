# Define a dictionary of patterns and their corresponding responses
patterns = {
    "hi": "Hello!",
    "how are you?": "I'm good, thank you!",
    "what's your name?": "I am a chatbot.",
    "default": "Sorry, I didn't understand that."
}

# Function to match user input with patterns and return an appropriate response
def respond(input_text):
    input_text = input_text.lower()  # Convert input to lowercase

    # Check if the input matches any patterns
    for pattern, response in patterns.items():
        if pattern in input_text:
            return response

    # If no pattern matches, return a default response
    return patterns["default"]

# Main loop to continuously interact with the user
while True:
    user_input = input("User: ")
    bot_response = respond(user_input)
    print("ChatBot:", bot_response)
