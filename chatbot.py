import datetime
def chatbot():
    user_name = ""
    print("----------------------------------------")
    print("        SIMPLE RULE-BASED CHATBOT")
    print("----------------------------------------")
    print("Type 'exit' to end the conversation.\n")
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "exit":
            print("Bot: Goodbye! Have a great day.")
            break
        elif "hello" in user_input or "hi" in user_input:
            if user_name:
                print(f"Bot: Hello {user_name}! How can I help you?")
            else:
                print("Bot: Hello! How can I help you?")
        elif "my name is" in user_input:
            user_name = user_input.split("my name is")[-1].strip().title()
            print(f"Bot: Nice to meet you, {user_name}.")
        elif "your name" in user_input:
            print("Bot: I am a rule-based chatbot.")
        elif "how are you" in user_input:
            print("Bot: I am functioning properly and ready to assist you.")
        elif "what can you do" in user_input:
            print("Bot: I can answer basic questions, tell time/date, and chat with you.")
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current time is {current_time}")
        elif "date" in user_input:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"Bot: Today's date is {current_date}")
        elif "help" in user_input:
            print("Bot: Try asking greetings, time, date, or tell me your name.")
        elif "what is ai" in user_input:
            print("Bot: AI stands for Artificial Intelligence, enabling machines to learn and make decisions.")
        else:
            print("Bot: I do not understand that. Please try something else.")
if __name__ == "__main__":
    chatbot()