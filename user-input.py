# Python helper game

#First the code should take data from a panda library about previous user performance and use that data.to determine the difficulty level of the exercises it will give to the user. The code should also take into account the user's preferred topic of learning (e.g. variables, loops, functions) and tailor the exercises accordingly.

print("Welcome to the Python helper game!")
print("I will help you learn Python syntax by giving you some exercises.")

#This function Will ask the user to select a mode
# This function asks the user to choose a game mode
def modes():

    # Keep asking forever until a valid answer is given
    while True:

        # Store the user's input in a variable
        mode = input(
            "Please select a mode "
            "(quiz or practice) "
            "or type 'info': "
        ).lower()

        # If the user asks for info
        if mode == "info":

            # Display information
            print("Quiz mode will test your knowledge.")
            print("Practice mode gives exercises.")

            # The loop automatically repeats

        # If the user enters a valid option
        elif mode == "quiz" or mode == "practice":

            # Store success message
            print("Valid mode selected.")

            # Stop the loop
            break

        # If the input is invalid
        else:

            print("Invalid input. Please try again.")

    # Return the final valid answer
    return mode

# This function asks the user to choose a difficulty
def difficulties():

    # Keep repeating until the user enters a valid answer
    while True:

        # Store the user's answer
        difficulty = input(
            "Please select a difficulty level (easy, medium, hard): "
        ).lower()

        # If the user types "info"
        if difficulty == "info":

            # Explain each difficulty
            print(
                "Easy will ask you to copy out code with unlimited hints and feedback."
            )

            print(
                "Medium will ask you to fill in the blanks with limited hints."
            )

            print(
                "Hard will ask you to write code from scratch with no hints."
            )

            # The loop automatically repeats

        # If the user selects easy
        elif difficulty == "easy":

            print("You have selected Easy difficulty.")

            # Stop the loop
            break

        # If the user selects medium
        elif difficulty == "medium":

            print("You have selected Medium difficulty.")

            # Stop the loop
            break

        # If the user selects hard
        elif difficulty == "hard":

            print("You have selected Hard difficulty.")

            # Stop the loop
            break

        # If the user enters something invalid
        else:

            print("Invalid difficulty level selected.")

    # Return the final valid answer
    return difficulty

# This function asks the user to choose a topic
def topics():

    # Keep repeating until the user enters a valid answer
    while True:

        # Ask the user for a topic
        topic = input(
            "Please select a topic "
            "(Syntax, Variables, Loops, Functions): "
        ).lower()

        # If the user asks for information
        if topic == "info":

            # Explain the topics
            print("Syntax = basic Python syntax")
            print("Variables = creating and using variables")
            print("Loops = for and while loops")
            print("Functions = defining and calling functions")

            # The loop automatically repeats

        # If the user selects syntax
        elif topic == "syntax":

            print("You selected Syntax.")

            # Stop the loop
            break

        # If the user selects variables
        elif topic == "variables":

            print("You selected Variables.")

            # Stop the loop
            break

        # If the user selects loops
        elif topic == "loops":

            print("You selected Loops.")

            # Stop the loop
            break

        # If the user selects functions
        elif topic == "functions":

            print("You selected Functions.")

            # Stop the loop
            break

        # If the user enters something invalid
        else:

            print("Invalid topic selected, please try again.")

    # Return the final valid answer
    return topic

    # If the user asks for information
    if topic == "info":

        # Explain the topics
        print("Syntax = basic Python syntax")
        print("Variables = creating and using variables")
        print("Loops = for and while loops")
        print("Functions = defining and calling functions")

    # If the user selects syntax
    elif topic == "syntax":

        print("You selected Syntax.")

    # If the user selects variables
    elif topic == "variables":

        print("You selected Variables.")

    # If the user selects loops
    elif topic == "loops":

        print("You selected Loops.")

    # If the user selects functions
    elif topic == "functions":

        print("You selected Functions.")

    # If the user enters something invalid
    else:

        # Show an error message
        print("Invalid topic selected, please try again.")

        # Run the function again
        topics()

# Run the mode function
modes()

# Run the difficulty function
difficulties()

# Run the topic function
topics()

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


#Running the game itself, the code should use the user's choices to determine which exercises to generate. For example, if the user selects "Quiz" mode, "Medium" difficulty, and "Variables" topic, the code should generate a quiz with questions about variables at a medium difficulty level. If the user selects "Practice" mode, "Easy" difficulty, and "Loops" topic, the code should generate practice exercises about loops at an easy difficulty level.

"""
# Mode quiz, difficulty easy, topic variables
if mode == "quiz" and difficulty == "easy" and topic == "variables":
    def quiz_easy_variables():
    
"""

# Mode quiz, difficulty medium, topic variables
"""
elif mode == "quiz": and difficulty == "medium": and topic == "variables":
"""

# Mode quiz, difficulty hard, topic variables
"""
elif mode == "quiz":
    if difficulty == "hard":
        if topic == "variables":
"""

# Mode practice, difficulty easy, topic variables
"""
elif mode == "practice":
    if difficulty == "easy":
        if topic == "variables":
"""

# Mode practice, difficulty medium, topic variables
"""
elif mode == "practice":
    if difficulty == "medium":
        if topic == "variables":
"""

# Mode practice, difficulty hard, topic variables
"""
elif mode == "practice":
    if difficulty == "hard":
        if topic == "variables":

"""

# Anything else so code doesn't break if user enters something invalid, but instead shows an error message and prompts them to try again.
""" 
else:   print("Invalid mode, difficulty, or topic selected. Please try again.")

"""
