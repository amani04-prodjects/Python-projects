# Python helper game

#First the code should take data from a panda library about previous user performance and use that data.to determine the difficulty level of the exercises it will give to the user. The code should also take into account the user's preferred topic of learning (e.g. variables, loops, functions) and tailor the exercises accordingly.

print("Welcome to the Python helper game!")
print("I will help you learn Python syntax by giving you some exercises.")

#This function Will ask the user to select a mode
def modes():

    mode = input(
        "Please select a mode (Quiz or Practice) and for more information type 'info': "
    ).lower()

    if mode == "info":
        print("Quiz mode will test your knowledge with questions.")
        print("Practice mode will give you exercises to complete.")

    elif mode == "quiz":
        print("You have selected Quiz mode.")

    elif mode == "practice":
        print("You have selected Practice mode.")

    else:
        print("Invalid mode selected.")

#This function will ask the user to select a difficulty
def difficulties():
    difficulty = str(input("Please select a difficulty level (easy, medium, hard): ").lower())
    # For more information on the difficulty levels please type "info"
    if difficulty == "info":
        print("Easy will ask you to copy out code (with unlimited hits and feedback)," \
        " Medium will ask you to fill in the blanks with limited hints, focusing on your strengths and weaknesses based on your previous performance,"
    " and Hard will ask you to write code from scratch with no hints asking only questions you have previously gotten wrong.")

    elif difficulty == "easy":
    print("You have selected Easy difficulty. You will be asked to copy out code with unlimited hits and feedback.")

    elif difficulty == "medium":
    print("You have selected Medium difficulty. You will be asked to fill in the blanks with limited hints, focusing on your strengths and weaknesses based on your previous performance.")

    elif difficulty == "hard":
    print("You have selected Hard difficulty. You will be asked to write code from scratch with no hints, asking only questions you have previously gotten wrong.")

    else:
    print("Invalid difficulty level selected. Please select either 'easy', 'medium', or 'hard'.")

#This function will ask the user to select a topic
def topics():
# For more information on the topics please type "info"
    topic = input(
        "Please select a topic (Syntax, Variables, Loops, Functions): "
    ).lower()

    if topic == "info":
        print("Syntax = basic Python syntax")
        print("Variables = creating and using variables")
        print("Loops = for and while loops")
        print("Functions = defining and calling functions")

    elif topic == "syntax":
        print("You selected Syntax.")

    elif topic == "variables":
        print("You selected Variables.")

    elif topic == "loops":
        print("You selected Loops.")

    elif topic == "functions":
        print("You selected Functions.")

    else:
        print("Invalid topic selected.")

# After choosing the mode, difficulty, and topic, the code should then generate exercises basied on the user's choices. For example, if the user selects "Quiz" mode, "Medium" diffculty, and "Variables" topic, the code should generate a quiz with questions about variables at a medium difficulty level. If the user selects "Practice" mode, "Easy" difficulty, and "Loops" topic, the code should generate practice exercises about loops at an easy difficulty level.

# text = input("Please copy out the following code and paste it here: " + random)
library_Syntax = [
    'print("Hello, World!")',
    'print("Python is fun")',
    'print(5 + 3)',
    'print("My name is Alex")',
    'print(True)'
]

library_Variables = [
    'name = input("Please enter your name: ")',
    'x = 5',
    'y = 10',
    'z = x + y',
    'age = 18'
]

library_loops = [
    'for i in range(5):',
    'while True:',
    'for item in items:',
    'for letter in "Python":',
    'while x < 10:'
]

library_functions = [
    'def greet(name): print("Hello", name)',
    'def add(a, b): return a + b',
    'def say_hello(): print("Hello!")',
    'greet("Alex")',
    'result = add(5, 3)'
]



# Mode quiz, difficulty easy, topic variables
if mode == "quiz" and difficulty == "easy" and topic == "variables":
    def quiz_easy_variables():
        



# Mode quiz, difficulty medium, topic variables
elif mode == "quiz": and difficulty == "medium": and topic == "variables":

# Mode quiz, difficulty hard, topic variables
elif mode == "quiz":
    if difficulty == "hard":
        if topic == "variables":


# Mode practice, difficulty easy, topic variables
elif mode == "practice":
    if difficulty == "easy":
        if topic == "variables":

# Mode practice, difficulty medium, topic variables
elif mode == "practice":
    if difficulty == "medium":
        if topic == "variables":

# Mode practice, difficulty hard, topic variables
elif mode == "practice":
    if difficulty == "hard":
        if topic == "variables":
        
else:   print("Invalid mode, difficulty, or topic selected. Please try again.")
