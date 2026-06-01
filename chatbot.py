from responses import responses


def get_response(user_input):

    user_input = user_input.lower().strip()

    if user_input in responses:
        return responses[user_input]

    else:
        return "Sorry, I don't understand that."


print("=" * 40)
print("      SIMPLE RULE-BASED CHATBOT")
print("=" * 40)
print("Type 'exit' or 'quit' to stop the chatbot.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    print("Bot:", get_response(user_input))