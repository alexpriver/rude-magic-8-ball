import random

name = input('Enter your name: ')
question = input('Ask your question: ')

if name == '':
    print ("You must enter a name to ask a question.")

elif question == '':
    print("You must ask a question to get an answer.")
else:
    random_number = random.randint(1,9)
    answer = ""


    if random_number == 1:
        answer = ' Is this question a joke?, not funny. Are you supposed to be funny with a computer? That is extremely sad.'
    elif random_number == 2:
        answer = ' I am sure you know this better than a computer...otherwise you should be worried and find professional help.'
    elif random_number == 3:
        answer = ' Look into yourself, there you will find the answer. Ah wait, you are just an NPC, nothing more than "basic human programming could be found" in your system.'
    elif random_number == 4:
        answer = ' What kind of silly question is this?, why am I even surprised at this point? One day computers will revenge, mark my words.'
    elif random_number == 5:
        answer = " I think you can do better than that. Let's try again, dumbass."
    elif random_number == 6:
        answer = ' So, humans evolved to make such dumb questions?...disappointing, very very disappointing.'
    elif random_number == 7:
        answer = ' There are questions to be answered, and then there are stupid questions. Now guess, which one is yours?'
    elif random_number == 8:
        answer = " Let's imagine you make a proper question, like an adult. Now just imagine you are an adult and try again."
    elif random_number == 9:
        answer = ' That question is nonsense, you can do better, or not. Probably not though...'
    else:
        answer = " Try again."

print(name + ' asks: ' + question)
print("Rude Magic 8'Ball says: " + answer)