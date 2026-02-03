from assistant import AIAssistant

def main():
    assistant = AIAssistant()
    print("AI Assistant is running. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = assistant.get_response(user_input)
        print("Assistant:", response)

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
