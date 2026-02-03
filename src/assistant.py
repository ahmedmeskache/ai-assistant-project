from utils import clean_text

class AIAssistant:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I help you?",
            "hi": "Hi there! What can I do for you?",
            "help": "I am an AI assistant. You can ask me questions.",
            "bye": "Goodbye! Have a nice day.",
            "name": "I am a simple AI assistant."
        }

    def get_response(self, user_input: str) -> str:
        cleaned_input = clean_text(user_input)

        for keyword in self.responses:
            if keyword in cleaned_input:
                return self.responses[keyword]

        return "I'm sorry, I didn't understand that. Can you rephrase?"
