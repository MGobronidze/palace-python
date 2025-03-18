# Python Project: Learning Basic Data Structures and String Operations

class LearnPythonBasics:
    def __init__(self):
        print("Welcome to Python Basics Learning!")

    def lists_tuples_demo(self):
        print("\n--- Lists and Tuples ---")
        # Lists
        fruits = ["apple", "banana", "cherry"]
        print(f"List of fruits: {fruits}")
        fruits.append("orange")
        print(f"After adding an item: {fruits}")

        # Demonstrating mutability
        fruits[0] = "grape"
        print(f"After modifying an item (mutable): {fruits}")

        # Tuples
        colors = ("red", "green", "blue")
        print(f"Tuple of colors: {colors}")
        print(f"Accessing second color: {colors[1]}")

        # Demonstrating immutability
        try:
            colors[0] = "yellow"
        except TypeError:
            print("Tuples are immutable; you cannot modify their elements.")

    def dictionary_demo(self):
        print("\n--- Dictionaries ---")
        # Create a dictionary
        student = {"name": "Alice", "age": 12, "grade": "7th"}
        print(f"Student dictionary: {student}")

        # Accessing values
        print(f"Student's name: {student['name']}")

        # Adding a new key-value pair
        student["favorite_subject"] = "Math"
        print(f"Updated dictionary: {student}")

        # Demonstrating mutability
        student["age"] = 13
        print(f"After modifying a value (mutable): {student}")

    def set_demo(self):
        print("\n--- Sets ---")
        # Create sets
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}

        # Operations
        print(f"Set 1: {set1}")
        print(f"Set 2: {set2}")
        print(f"Union: {set1 | set2}")
        print(f"Intersection: {set1 & set2}")
        print(f"Difference: {set1 - set2}")

        # Demonstrating mutability
        set1.add(5)
        print(f"After adding an element to Set 1 (mutable): {set1}")

    def string_operations_demo(self):
        print("\n--- String Operations ---")
        # Basic string operations
        message = "Hello, Python!"
        print(f"Original message: {message}")
        print(f"Uppercase: {message.upper()}")
        print(f"Lowercase: {message.lower()}")
        print(f"Replace: {message.replace('Python', 'World')}")

        # Demonstrating immutability
        print(f"Original message remains unchanged: {message}")

        # Multiline strings
        multiline = """This is a multiline
        string. It spans multiple lines."""
        print(f"Multiline string:\n{multiline}")

    def string_formatting_demo(self):
        print("\n--- String Formatting ---")
        name = "Bob"
        age = 10
        print(f"Hello, my name is {name} and I am {age} years old.")
        print("My name is {} and I am {} years old.".format(name, age))

    def review_questions(self):
        print("\n--- Review Questions ---")
        questions = [
            {
                "question": "1. What is the difference between a list and a tuple?",
                "options": [
                    "a) Lists are immutable, and tuples are mutable.",
                    "b) Lists are mutable, and tuples are immutable.",
                    "c) Both are mutable."
                ],
                "correct": "b"
            },
            {
                "question": "2. How can you add an element to a dictionary?",
                "options": [
                    "a) Using the add() method.",
                    "b) By assigning a value to a new key.",
                    "c) Dictionaries are immutable; you cannot add elements."
                ],
                "correct": "b"
            },
            {
                "question": "3. Are strings mutable or immutable?",
                "options": [
                    "a) Mutable.",
                    "b) Immutable.",
                    "c) It depends on the operation."
                ],
                "correct": "b"
            },
            {
                "question": "4. What is the result of the union operation on sets {1, 2} and {2, 3}?",
                "options": [
                    "a) {1, 2, 3}",
                    "b) {2}",
                    "c) {1, 3}"
                ],
                "correct": "a"
            },
            {
                "question": "5. How do you access the value associated with a key in a dictionary?",
                "options": [
                    "a) Using square brackets with the key.",
                    "b) Using the get() method.",
                    "c) Both a and b."
                ],
                "correct": "c"
            },
            {
                "question": "6. Which method is used to add an element to a set?",
                "options": [
                    "a) append()",
                    "b) add()",
                    "c) insert()"
                ],
                "correct": "b"
            }
        ]

        for q in questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Your answer: ").strip().lower()
            if answer == q["correct"]:
                print("Correct!\n")
            else:
                print(f"Incorrect. The correct answer is {q['correct']}.")

# Create an instance and run the demos
learning_tool = LearnPythonBasics()
learning_tool.lists_tuples_demo()
learning_tool.dictionary_demo()
learning_tool.set_demo()
learning_tool.string_operations_demo()
learning_tool.string_formatting_demo()
learning_tool.review_questions()
