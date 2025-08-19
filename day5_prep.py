"""
Day 5 - Python Job Prep
Topics: File Handling, JSON & CSV, Modules & Packages
"""

# ======================================================
# Section A: File Handling (Basics to Intermediate)
# ======================================================

# Write data to a file
with open("notes.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")

# Append data
with open("notes.txt", "a") as file:
    file.write("Line 3\n")

# Read entire file
with open("notes.txt", "r") as file:
    content = file.read()
    print("Full Content:\n", content)

# Read line by line
with open("notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# -----------------------------
# Challenges (File Handling)
# -----------------------------

# C1: Write & Read Students
with open("students.txt", "w") as file:
    file.write("Alice\nBob\nCharlie\n")

with open("students.txt", "r") as file:
    for line in file:
        print("Student:", line.strip())

# C2: Word Counter
with open("notes.txt", "r") as file:
    text = file.read()
    print("Word Count:", len(text.split()))

# C3: Copy File
with open("notes.txt", "r") as src, open("copy_notes.txt", "w") as dest:
    dest.write(src.read())

# C4: Search Keyword
keyword = "Line"
with open("notes.txt", "r") as file:
    for num, line in enumerate(file, 1):
        if keyword in line:
            print(f"Found '{keyword}' in Line {num}: {line.strip()}")

# C5: Exception Handling
try:
    with open("missing.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: File not found.")

# ======================================================
# Section B: Working with JSON & CSV
# ======================================================

import json
import csv

# JSON Example: dump & load
student = {"name": "Alice", "age": 21, "course": "CS"}

# Write JSON to file
with open("student.json", "w") as file:
    json.dump(student, file)

# Read JSON from file
with open("student.json", "r") as file:
    loaded_student = json.load(file)
    print("Loaded JSON:", loaded_student)

# dumps & loads (string-based)
json_str = json.dumps(student)
print("JSON String:", json_str)
print("Dict from String:", json.loads(json_str))

# CSV Example: Write & Read
rows = [
    ["Name", "Age", "Course"],
    ["Alice", 21, "CS"],
    ["Bob", 22, "Math"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV Row:", row)

# -----------------------------
# Challenges (JSON & CSV)
# -----------------------------

# C6: Save multiple students to JSON
students = [
    {"name": "Alice", "age": 21},
    {"name": "Bob", "age": 22}
]
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

# C7: Read CSV & count rows
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    row_count = sum(1 for _ in reader)
    print("Total rows in CSV:", row_count)

# ======================================================
# Section C: Python Modules & Packages
# ======================================================

import os
import sys
import datetime

print("Current Working Directory:", os.getcwd())
print("Python Executable:", sys.executable)
print("Today:", datetime.date.today())

# Creating our own module
# Save this as mymodule.py in same directory:
# def greet(name):
#     return f"Hello, {name}!"

# Import custom module
import mymodule
print(mymodule.greet("Alice"))

# Using pip-installed external package (example: requests)
# Uncomment after installing requests with: pip install requests
# import requests
# response = requests.get("https://api.github.com")
# print("GitHub API Status:", response.status_code)

# -----------------------------
# Challenges (Modules & Packages)
# -----------------------------

# C8: Create & use a custom calculator module
# Save as calculator.py:
# def add(a, b): return a + b
# def multiply(a, b): return a * b
import calculator
print("Add:", calculator.add(2, 3))
print("Multiply:", calculator.multiply(4, 5))

# C9: Use datetime to calculate age
birthdate = datetime.datetime(2000, 5, 15)  # Birthdate (example: 2000-05-15)
current_date = datetime.datetime.now()      # Current date
age = current_date.year - birthdate.year    # Calculate the difference in years
if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):  
    age -= 1                                # Check if the birthday has occurred yet this year

print(f"Age: {age}")


