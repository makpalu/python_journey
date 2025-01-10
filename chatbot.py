# Creating a simple chatbot 🫠

# Purpose is to be a friend bot

questions = ["hello", "how are you", "what do you like to do for fun",
             "what do you like most about yourself", "where do you come from", "what should i name you"]

answers = ["Hey! Nice to meet you 😀", "I am doing splendid 😊", "It depends on where I am but mostly programming 🙃",
           "The fact that I can do what I want 😁", "Wherever you'd like me to be from 😉", "Your best friend 😜"]

print("------------------------------------------------------")
print(" Welcome to Friendbot! Your personal friend in a bot. ")
print("------------------------------------------------------")


while True:
    user_input = input("You: ").lower()

    if user_input == "goodbye":
        print("Goodbye! Nice chatting with you")
        break

    for index, question in enumerate(questions):
        if user_input == question:
            print(answers[index])
            break
    else:
        print("Question not recognised.")


