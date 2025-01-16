# Creating a simple chatbot 🫠

# Purpose is to be a friend bot

import difflib

questions = [["hello", "hey", "hi", "sup","howdy"],
             ["how are you", "How do you do", "how are you feeling","how is life"],
             ["what do you like to do for fun", "what do you do in your free time"],
             ["what do you like most about yourself", "what makes you, you"],
             ["where do you come from", "where do you live"],
             ["what should i name you", "what would you like to be called", "what is your name"]]

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

    best_match = None
    best_index = -1

    for index, variations in enumerate(questions):
        match = difflib.get_close_matches(user_input, variations, n=1, cutoff=0.6)

        if match:
            best_match = match[0]
            best_index = index
            break
    if best_match:
        print(answers[best_index])
    else:
        print("Question not recognised.")