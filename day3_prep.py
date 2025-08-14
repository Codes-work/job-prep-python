"""
Day 3 – Python Job Prep
Author: ALLEN ALEXANDER – Aspiring Python / AI-ML Developer

This script covers:
A) Functions & Functional Programming
B) File Handling
C) Error Handling
"""

from functools import reduce


# ==========================================
# SECTION A – FUNCTIONS & FUNCTIONAL PROGRAMMING
# ==========================================

# --- 1. Default Parameters ---
def greet(name="Guest"):
    """Greets a user with a default value if no name is provided."""
    print(f"Welcome {name}!")


# --- 2. Keyword Arguments ---
def order_pizza(size, crust, topping):
    """Displays pizza order details."""
    print(f"You ordered a {size} pizza with {crust} crust and {topping}.")


# --- 3. Lambda Functions ---
# Simple lambda
triple = lambda x: x * 3

# Conditional lambda (checks if a number is odd)
is_odd = lambda x: x % 2 != 0


# --- 4. Map & Filter ---
def map_and_filter_example(nums):
    """
    First divide each number by 3, then filter numbers greater than 5.
    Returns the resulting list.
    """
    return list(filter(lambda x: x > 5, map(lambda x: x / 3, nums)))


# --- 5. Reduce ---
def multiply_list(nums):
    """Multiplies all numbers in the list using reduce."""
    return reduce(lambda x, y: x * y, nums)


# --- 6. Combined Pipeline ---
def combined_pipeline(nums):
    """
    Example of combining map, filter, and reduce in one chain:
    - Multiply each number by 2
    - Keep only even numbers
    - Find the sum of the remaining numbers
    """
    return reduce(
        lambda x, y: x + y,
        filter(lambda n: n % 2 == 0, map(lambda n: n * 2, nums))
    )


# ==========================================
# SECTION B – FILE HANDLING
# ==========================================

# --- 1. Write text to a file ---
def write_to_file(filename, text):
    """Writes given text to a file (overwrites existing content)."""
    with open(filename, 'w') as file:
        file.write(text)


# --- 2. Read text from a file ---
def read_file(filename):
    """Reads and prints content from a file."""
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


# --- 3. Append text to a file ---
def append_to_file(filename, text):
    """Appends given text to an existing file."""
    with open(filename, 'a') as file:
        file.write(text)


# --- 4. Count words in a file ---
def count_words_in_file(filename):
    """Counts and prints the number of words in the file."""
    with open(filename, 'r') as file:
        words = file.read().split()
        print(f"Word count: {len(words)}")


# ==========================================
# SECTION C – ERROR HANDLING
# ==========================================

# --- 1. Division with zero handling ---
def safe_division(a, b):
    """Performs division and handles ZeroDivisionError."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


# --- 2. File not found handling ---
def safe_file_read(filename):
    """Reads file content and handles FileNotFoundError."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")


# --- 3. Custom exception example ---
class NegativeAgeError(Exception):
    """Custom exception for negative age values."""
    pass

def check_age(age):
    """Raises NegativeAgeError if age is negative."""
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")


# ==========================================
# MAIN DEMO
# ==========================================
if __name__ == "__main__":

    # --- SECTION A DEMO ---
    greet()
    greet("Allen")

    order_pizza(size="Large", crust="Thin", topping="Mushrooms")

    print("Triple of 5:", triple(5))
    print("Is 7 odd?", is_odd(7))

    nums = [3, 6, 9, 12, 15]
    print("Map + Filter result:", map_and_filter_example(nums))

    nums_for_reduce = [5, 10, 15, 20]
    print("Product using reduce:", multiply_list(nums_for_reduce))

    print("Combined pipeline sum:", combined_pipeline([1, 2, 3, 4, 5]))

    # --- SECTION B DEMO ---
    write_to_file("data.txt", "Hello World\n")
    append_to_file("data.txt", "New Line Added\n")
    read_file("data.txt")
    count_words_in_file("data.txt")

    # --- SECTION C DEMO ---
    print("Safe Division:", safe_division(10, 0))
    print("File Content:", safe_file_read("missing.txt"))

    try:
        check_age(-5)
    except NegativeAgeError as e:
        print("Custom Exception:", e)
