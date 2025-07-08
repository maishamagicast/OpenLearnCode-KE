# Intro to Python Course

"""
Welcome to the Intro to Python course! This course is designed for absolute beginners
with no prior programming experience. Python is a powerful and beginner-friendly programming language
used in web development, data science, automation, artificial intelligence, and more.

In this course, you'll learn Python step-by-step with detailed explanations and hands-on examples.
Each lesson builds on the previous one, so take your time and practice.
"""

# ----------------------------------------
# Lesson 1: Hello World
# ----------------------------------------
"""
The 'Hello, world!' program is the traditional first step in learning a new programming language.
It simply prints a message to the screen.
"""
print("Hello, world!")

# ----------------------------------------
# Lesson 2: Variables and Data Types
# ----------------------------------------
"""
Variables are like containers that store information. Each variable has a name and holds a value.
Python automatically figures out what kind of data (data type) you're storing.
"""
name = "Alice"         # A string of text (str)
age = 25               # A whole number (int)
height = 5.4           # A decimal number (float)
is_student = True      # A boolean value (True or False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# ----------------------------------------
# Lesson 2.1: Data Types and Their Methods
# ----------------------------------------
"""
Every data type in Python comes with useful methods (built-in functions) that help you work with them.
Let's explore the common ones with examples.
"""

# String methods
text = "  Hello Python!  "
print(text.lower())     # Converts all characters to lowercase
print(text.upper())     # Converts all characters to uppercase
print(text.strip())     # Removes leading/trailing whitespace
print(text.replace("Python", "World"))  # Replaces a word in the string
print(len(text))        # Returns length of the string including spaces

# Integer and float don't have many methods but can be converted
num = 42
print(float(num))       # Convert integer to float
print(str(num))         # Convert integer to string

# Boolean is mostly used in conditions and logic
print(bool(1))          # True, because 1 is truthy
print(bool(0))          # False, because 0 is falsy

# List methods
colors = ["red", "blue", "green"]
colors.append("yellow")         # Adds item to end of list
colors.remove("blue")           # Removes the first occurrence of an item
colors.insert(1, "orange")      # Inserts at a specific position
print(colors)
print(len(colors))              # Number of items in the list

# Dictionary methods
student = {"name": "Sam", "age": 20}
print(student.keys())           # Returns all keys
print(student.values())         # Returns all values
print(student.get("name"))      # Safer way to access a key
student["grade"] = "A"           # Adds a new key-value pair
print(student)

# Type checking
print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(colors))   # <class 'list'>

# Always feel free to experiment with different methods using the dot (.) notation.
# You can also use help(str), help(list), etc. to see all available methods.

# ----------------------------------------
# Lesson 3: Basic Input and Output
# ----------------------------------------
"""
You can get input from a user with the input() function, and display output using print().
"""
user_name = input("What is your name? ")
print("Nice to meet you,", user_name)

# ----------------------------------------
# Lesson 4: Conditionals (If Statements)
# ----------------------------------------
"""
Conditionals let you run different code depending on whether something is true or false.
Use if, elif (else if), and else to create conditions.
"""
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# ----------------------------------------
# Lesson 5: Loops
# ----------------------------------------
"""
Loops help you repeat actions.
Use 'for' loops when you know how many times to repeat.
Use 'while' loops when you want to repeat until a condition is false.
"""
print("\nFor loop example:")
for i in range(5):
    print("Iteration number:", i)

print("\nWhile loop example:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# ----------------------------------------
# Lesson 6: Functions
# ----------------------------------------
"""
Functions are reusable blocks of code. You define a function once, and use (call) it whenever needed.
"""
def greet(name):
    """This function greets the person by name."""
    print("Hello,", name)

greet("Bob")

# ----------------------------------------
# Lesson 7: Lists
# ----------------------------------------
"""
Lists are used to store multiple values in a single variable.
You can loop through a list using a for loop.
"""
fruits = ["apple", "banana", "cherry"]

print("My favorite fruits are:")
for fruit in fruits:
    print(fruit)

# ----------------------------------------
# Lesson 8: Dictionaries
# ----------------------------------------
"""
Dictionaries store data in key-value pairs. It's like a mini-database.
"""
person = {
    "name": "John",
    "age": 30,
    "city": "Nairobi"
}

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# ----------------------------------------
# Lesson 9: File Handling
# ----------------------------------------
"""
Python can read from and write to files. Use 'with open' to safely handle files.
"""
# Writing to a file
with open("example.txt", "w") as f:
    f.write("This is a sample file.\nPython is writing to it!")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("\nFile contents:")
    print(content)

# ----------------------------------------
# Lesson 10: Classes and Objects
# ----------------------------------------
"""
Classes are blueprints for creating objects. Objects have data (attributes) and actions (methods).
"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "says woof!")

# Creating an object of the class
my_dog = Dog("Buddy", "Labrador")
my_dog.bark()

# ----------------------------------------
# End of Intro Course
# ----------------------------------------
"""
Great work! You've completed the basic introduction to Python.
To build your skills further, try making small projects like a calculator, a quiz game, or a to-do list app.
Keep practicing, and soon you'll be ready for more advanced Python topics!
"""
