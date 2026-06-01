import random

print("Welcome to the Python helper game!")
print("I will help you learn Python syntax by giving you some exercises.")
print("First, let's select a topic, difficulty level, and game mode.")

# ----------------------------
# Choose Mode
# ----------------------------

def Choose_modes():
    while True:
        mode = input(
            "Please select a mode "
            "(quiz or practice) "
            "or type 'info' for more information: "
        ).lower()

        if mode == "info" or mode == "help" or mode == "information":
            print("Quiz mode will give you multiple-choice questions.")
            print("Practice mode gives you coding exercises to copy.")

        elif mode in ["quiz", "practice"]:
            print("You selected ", mode)
            return mode

        else:
            print("Invalid input. Please try again.")

# ----------------------------
# Choose Difficulty
# ----------------------------

def Choose_difficulties():
    while True:
        difficulty = input(
            "Please select a difficulty"
            "(easy, medium, hard) "
            "or type 'info' for more information: "
        ).lower()

        if difficulty == "info" or difficulty == "help" or difficulty == "information":
            print("Easy = unlimited tries")
            print("Medium = limited hints and attempts, (You will have 5 lives)")
            print("Hard = no hints and (3 lives)")

        elif difficulty in ["easy", "medium", "hard"]:
            print("You selected", difficulty)
            return difficulty

        else:
            print("Invalid difficulty level selected.")


# ----------------------------
# Choose Topic
# ----------------------------

def Choose_topics():
    while True:
        topic = input(
            "Please select a topic "
            "(syntax, variables, loops, functions) "
            "or type 'info': "
        ).lower()

        if topic == "info":
            print("Their are 4 topics that can be selected:syntax, variables, loops, functions")

        elif topic in ["syntax", "variables", "loops", "functions"]:
            print("You selected", topic)
            return topic

        else:
            print("Invalid topic selected, please try again.")


# ----------------------------
# Question Libraries
# ----------------------------

library_Syntax = [
    'print("Hello, World!")',
    'print("Python is fun")',
    'print(5 + 3)',
]

library_Variables = [
    'name = input("Please enter your name: ")',
    'x = 5',
    'z = x + 10',
]

library_Loops = [
    'for i in range(5):',
    'while True:',
    'for item in items:',
]

library_Functions = [
    'def greet(name): print("Hello", name)',
    'def add(a, b): return a + b',
    'def say_hello(): print("Hello!")',
]


# ----------------------------
# Game Logic
# ----------------------------

def start_game(mode, difficulty, topic):

    if topic == "syntax":
        selected_library = library_Syntax.copy()
    elif topic == "variables":
        selected_library = library_Variables.copy()
    elif topic == "loops":
        selected_library = library_Loops.copy()
    elif topic == "functions":
        selected_library = library_Functions.copy()
    else:
        print("Invalid topic.")
        return

    while selected_library:

        question = random.choice(selected_library)
        print("\nPlease copy the following code:")
        print(question)

        if difficulty == "easy":

            while True:
                answer = input("Answer: ")

                if answer == question:
                    print("Correct!")
                    selected_library.remove(question)
                    break
                else:
                    print("Try again.")

        elif difficulty == "medium":

            attempts = 3

            while attempts > 0:
                answer = input("Answer: ")

                if answer == question:
                    print("Correct!")
                    selected_library.remove(question)
                    break

                attempts -= 1
                print("Incorrect. Attempts left:", attempts)

            else:
                print("Correct answer was:")
                print(question)
                selected_library.remove(question)

        elif difficulty == "hard":

            answer = input("Answer: ")

            if answer == question:
                print("Correct!")
            else:
                print("Incorrect. Correct answer was:")
                print(question)

            selected_library.remove(question)

    print("\nYou completed all questions!")


# ----------------------------
# Main Loop
# ----------------------------

while True:

    mode = Choose_modes()
    difficulty = Choose_difficulties()
    topic = Choose_topics()

    start_game(mode, difficulty, topic)

    again = input("\nPlay again? (yes/no): ").lower()

    if again == "no":
        print("Thanks for playing!")
        break
