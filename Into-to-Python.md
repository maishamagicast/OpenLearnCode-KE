# 🐍 Python for Absolute Beginners

Welcome to your journey into **Python programming**! This beginner-friendly language is one of the most popular and powerful tools used in the world of technology today.

---

## 🌍 What is Python?

**Python** is a high-level, interpreted programming language created by **Guido van Rossum** and first released in **1991**. It emphasizes **code readability**, meaning it's easier to write and understand code compared to many other languages.

### 🔑 Key Features:
- Simple, clean syntax (English-like)
- Large community and library support
- Cross-platform compatibility (Windows, macOS, Linux)
- Free and open-source

---

## 🚀 What Can You Do With Python?

Python is used **everywhere**, including:

| Field | Use Cases |
|------|-----------|
| 💻 Web Development | Backend servers, REST APIs (e.g., Flask, Django) |
| 📊 Data Science | Data analysis, machine learning (e.g., pandas, scikit-learn) |
| 🤖 AI & ML | Neural networks, automation, NLP |
| 🎮 Game Development | Simple 2D/3D games (e.g., Pygame) |
| 🛠 Automation | Writing scripts to automate boring tasks |
| 🧪 Education | Used in schools and universities as a first programming language |

---

## 🧰 Setting Up Python

To write and run Python programs, you need to install **Python interpreter** and optionally a **code editor**.

### ✅ Install Python:
1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download and install the latest version (tick the "Add Python to PATH" option).

### 🧑‍💻 Recommended Code Editors:
- [VSCode](https://code.visualstudio.com/)
- [Thonny](https://thonny.org/) – great for beginners
- [PyCharm](https://www.jetbrains.com/pycharm/) – powerful IDE

---

## 🧪 Your First Python Program

```python
# This line prints a simple greeting message to the screen
# Text inside quotes is called a "string"
print("Hello, world!")

# This line prints the number 42
# Numbers can be printed directly without quotes
print(42)

# This line prints a decimal number (called a float in Python)
print(3.14)

# Below, we are creating two variables: one for a name, and one for an age
# A variable stores a value that we can use later in the program
name = "Alice"  # This stores the text "Alice" in the variable called name
age = 20        # This stores the number 20 in the variable called age

# This prints a message by combining text and the values of the variables
# Python automatically adds a space between each item separated by commas
print("Name:", name, "Age:", age)

# This line uses something called an "f-string" to insert variable values directly into a sentence
# Anything inside the curly braces { } gets replaced with the value of the variable
print(f"My name is {name} and I am {age} years old.")

# Another way to insert variables into strings is using the .format() method
# The curly braces {} are replaced in order by the variables given inside format()
language = "Python"
version = 3
print("I am learning {} version {}.".format(language, version))

# This does the same thing, but shows how you can use position numbers inside the curly braces
# {0} refers to the first value inside format(), {1} to the second
print("I am learning {0} version {1}.".format(language, version))

# This example shows "percent formatting", an older style of formatting strings
# %.1f means: show a float (decimal number) with 1 digit after the decimal point
# %% prints a single % symbol
score = 97.5
print("Your score is %.1f%%" % score)

# By default, print() ends each line with a new line
# The 'end' argument lets us change that; here, it ends with a space instead
print("Hello", end=" ")  # This will not move to a new line
print("World!")          # So this will appear right after "Hello "

# The 'sep' argument changes the separator between printed values
# Normally, print("A", "B") would show "A B", but here we change the space to a dash
print("2025", "07", "08", sep="-")  # This will print: 2025-07-08

# This prints the result of an addition directly
# Python calculates 5 + 3 and inserts the result (8) into the print
print("5 + 3 =", 5 + 3)

# This line multiplies 5 by 10 (which equals 50) and includes it in the message
# Again, this uses an f-string to insert the result
print(f"Area of rectangle: {5 * 10} square units")

# In this example, we create two variables, and use custom formatting when printing them
# 'sep' is used to insert an emoji between the two words
# 'end' is used to end the line with an exclamation mark and new line
first = "Python"
second = "Rocks"
print(first, second, sep="💥", end="!\n")  # Output: Python💥Rocks!

# Another f-string example combining both variables into one clean sentence
language = "Python"
version = 3.11
print(f"{language} {version} is super fast.")

