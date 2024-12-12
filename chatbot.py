def chatbot():
    print("Hello! I am your chatbot. You can ask me simple questions.")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        # Get user input
        user_input = input("You: ").lower()  # Convert input to lowercase for consistency
        
        # Exit conditions
        if user_input in ["exit", "bye", "goodbye"]:
            print("Chatbot: Thank you for chatting! Goodbye!")
            break
        # Predefined responses
        elif "hello" in user_input:
            print("Chatbot: Hi there! How can I assist you?")
        elif "name" in user_input:
            print("Chatbot: My name is Chatbot. How can I help you?")
        elif "weather" in user_input:
            print("Chatbot: I can't provide weather updates, but you can check a weather app!")
        elif "time" in user_input:
            print("Chatbot: I recommend checking your device's clock for the time.")
        elif 
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome!")
        else:
            print("Chatbot: Sorry, I don't have an answer for that. Can I help with something else?")
            
# Run the chatbot
chatbot()
