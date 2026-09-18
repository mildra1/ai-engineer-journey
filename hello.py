# print statements

print("Hello World!")
print("My name is Chioma")
print("Learning to code is fun")
print(5 + 3)
print("Result:", 5 + 3)

#Variables

name = "Chioma"
age = 26
print("My name is", name,)
print("I am", age, "years old")
print(name, "is", age, "years old")

#Getting input from the user

name = input("What's your name? ")
print("Hello,", name)
age = input("How old are you? ")


# Variables and Printing 

name = "Chioma"
age = 26
height = 5.7
is_student = True

print(name)
print(age)
print(height)
print(is_student)
print(name, age, height, is_student)

# Data Types — check what everything is

values = [20, 3.14, "hello", True, [1, 2, 3], (1, 2), {"a": 1}, None]

for v in values:
    print(v, "→", type(v))

# Arithmetic Operators
print(10 + 5)  # Addition
print(10 - 5)  # Subtraction
print(10 * 5)  # Multiplication
print(10 / 5)  # Division
print(10 % 3)  # Modulus
print(10 ** 2) # Exponentiation 

a = 10
b = 3

print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
print("Floor divide:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Comparison Operators

x = 7
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= 7)
print(y <= 10)


# Logical Operators

age = 20
has_ticket = True
is_banned = False

print(age >= 18 and has_ticket)
print(is_banned or has_ticket)
print(not is_banned)


# If / Elif / Else

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Type Conversion

num_str = "42"
num_int = int(num_str)
print(num_int + 8)

price = "9.99"
price_float = float(price)
print(price_float * 2)

age = 20
print("I am " + str(age) + " years old")

# Mutable vs Immutable in action

# Immutable string
name = "Alex"
name = "J" + name[1:]
print(name)

# Mutable list
numbers = [1, 2, 3]
numbers[0] = 99
print(numbers)

numbers.append(4)
print(numbers)

# Lists — the basics

fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[-1])
print(len(fruits))

fruits.append("mango")
print(fruits)

fruits.remove("banana")
print(fruits)

for fruit in fruits:
    print("I like", fruit)

# Dictionaries — the basics

person = {"name": "Alex", "age": 20, "city": "Lagos"}

print(person["name"])
print(person.get("age"))

person["age"] = 21
print(person)

for key, value in person.items():
    print(key, ":", value)

# For Loops

for i in range(5):
    print(i)

for i in range(1, 11):
    print(i, "squared is", i ** 2)

# While Loops

count = 0
while count < 5:
    print("Count is", count)
    count += 1

# Functions

def greet(name):
    return "Hello, " + name + "!"

print(greet("Alex"))

def add(a, b):
    return a + b

print(add(4, 7))

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(15))
print(check_age(25))

# Error Handling

try:
    age = int(input("Enter your age: "))
    print(100 / age)
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Age can't be zero.")

# Membership & Identity Operators

colors = ["red", "green", "blue"]

print("green" in colors)
print("purple" not in colors)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a == c)

# A Combined Mini-Program (put it all together)

def classify_age(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

people = {"Alex": 16, "Sam": 34, "Jordan": 70, "Kai": 8}

for name, age in people.items():
    category = classify_age(age)
    print(f"{name} ({age}) is a {category}")

# String Methods

text = "  Hello, World!  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("World", "Python"))
print(text.strip().split(","))
print(len(text))
print("hello" in text.lower())

# String Formatting (f-strings)

name = "Alex"
age = 20
height = 5.9

print(f"My name is {name} and I am {age} years old.")
print(f"Next year I'll be {age + 1}.")
print(f"Height: {height:.1f} ft")

# List Slicing

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])     # items 2 to 4
print(numbers[:3])       # first 3 items
print(numbers[7:])       # from index 7 to end
print(numbers[::2])      # every 2nd item
print(numbers[::-1])   

# List Comprehensions (a Python favorite)
squares = [x ** 2 for x in range(10)]
print(squares)

evens = [x for x in range(20) if x % 2 == 0]
print(evens)

names = ["alex", "sam", "jordan"]
capitalized = [name.title() for name in names]
print(capitalized)

# Nested Lists (2D data)

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid[1][2])   # row 1, column 2 → 6

for row in grid:
    for item in row:
        print(item, end=" ")
    print()

# Sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a | b)   # union shorthand
print(a & b)   # intersection shorthand

# Tuples & Unpacking

point = (10, 20)
x, y = point
print(x, y)

person = ("Alex", 20, "Lagos")
name, age, city = person
print(f"{name} is {age} and lives in {city}")

# Functions with Default Arguments

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alex"))
print(greet("Sam", "Hi"))

def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))

# *args and **kwargs

def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))

def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe(name="Alex", age=20, city="Lagos")

# Classes — your first object

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Rex", "Labrador")
print(my_dog.name)
print(my_dog.breed)
print(my_dog.bark())

# Classes with More Behavior

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

account = BankAccount("Alex", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(1000)

# Working with Files

# Write to a file
with open("notes.txt", "w") as f:
    f.write("Hello, this is my first file!\n")
    f.write("Python is fun.\n")

# Read from a file

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
#Enumerate & Zip (loop helpers)

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

names = ["Alex", "Sam"]
ages = [20, 25]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Random Module (fun stuff)

import random

print(random.randint(1, 10))
print(random.choice(["rock", "paper", "scissors"]))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# A Bigger Combined Project — Simple Quiz Game

questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "What color is the sky?": "blue"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The answer was {answer}.")

print(f"\nYou scored {score} out of {len(questions)}")

# Number Guessing Game

import random

secret = random.randint(1, 20)
guess = None
attempts = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} tries.")