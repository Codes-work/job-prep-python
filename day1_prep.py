# Day 1 - Python Job Prep
# Author: [Your Name]
# Part of a 7-Day Python Job Prep Challenge

# -----------------------------
# SECTION A-1: Swap two variables without using a third variable
a = 20
b = 10
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)

# -----------------------------
# SECTION A-2: Taking user input and printing it
name = input("Enter name: ")
age = int(input("Enter age: "))
print(f"Hello {name}, you are {age} years old.")

# -----------------------------
# SECTION A-3: FizzBuzz program (1 to 50)
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# -----------------------------
# SECTION B-4: Count character frequency in a string
s = "mississippi"
frequency = {}
for i in s:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)

# -----------------------------
# SECTION B-5: Remove duplicates from a list (method 1)
l = [1, 2, 2, 3, 4, 4, 5]
result = []
seen = set()
for i in l:
    if i not in seen:
        result.append(i)
        seen.add(i)
print(result)

# Method 2 using dict.fromkeys()
s = list(dict.fromkeys(l))
print(s)

# -----------------------------
# SECTION B-6: Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {**dict1, **dict2}
print(dict3)

# -----------------------------
# SECTION B-7: Calculate average score from a list of dictionaries
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 90}
]

# Print students with score > 80
for student in students:
    if student['score'] > 80:
        print(student['name'])

# Calculate average score
total = sum(student['score'] for student in students)
avg = total / len(students)
print(f"Average Score = {avg}")

# Add a new student to the list
new_student = {"name": "Blaah", "score": 75}
students.append(new_student)
print(students)
