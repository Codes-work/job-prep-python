# Day 1 - Python Job Prep

This is **Day 1** of my **7-Day Python Job Preparation Challenge**.  
The goal is to brush up on Python fundamentals for junior developer and AI/ML roles.

## Topics Covered
- Variable swapping without a third variable
- Taking user input
- FizzBuzz problem
- Character frequency count
- Removing duplicates from a list (2 methods)
- Merging dictionaries
- Calculating averages from a list of dictionaries

## How to Run
1. Clone this repository
2. Run:
   ```bash
   python day1_prep.py
## Author- ALLEN ALEXANDER -aspiring python / AI-ML Developer

# Day 2 – Python Job Prep

Single-file solutions for **Day 2** of the 7-Day Python Job Prep series.  
Covers **Strings**, **Lists & Dictionaries**, and **Loops & Conditions** — all implemented as reusable functions.

## Sections & Problems

### A) Strings
- `reverse_string(s)`
- `is_palindrome(s)`
- `count_vowels(s)`

### B) Lists & Dictionaries
- `find_max_min(numbers)`
- `sum_even_numbers(numbers)`
- `merge_lists_unique(list1, list2)`
- `element_frequency(lst)`
- `remove_duplicates(lst)`
- `merge_dicts(dict1, dict2)`
- `average_score(students)`

### C) Loops & Conditions
- `fizzbuzz(n)`
- `factorial(n)`
- `sum_of_digits(n)`
- `fibonacci(n_terms)`
- `count_even_odd(numbers)` *(list-based)*
- `count_even_odd_range(start, end)` *(range-based)*
- `pattern_triangle(rows)`

> **Note on repetition:** Some problems also appeared in Day 1.  
> Day 1 focused on **direct scripting**; Day 2 refactors them into **clean, testable functions**.

## How to Run
```bash
python day2_prep.py
```
## Author- ALLEN ALEXANDER -aspiring python / AI-ML Developer

# Day 3 – Python Job Prep

This module covers **Functions & Functional Programming**, **File Handling**, and **Error Handling** in Python.  
Designed to strengthen practical coding skills for interviews and job readiness.

---

## **Section A – Functions & Functional Programming**
1. **Default Parameters**
   - `greet(name="Guest")`
2. **Keyword Arguments**
   - `order_pizza(size, crust, topping)`
3. **Lambda Functions**
   - Simple lambda: `triple = lambda x: x * 3`
   - Conditional lambda: `is_odd = lambda x: x % 2 != 0`
4. **Map & Filter**
   - Transform and filter lists in a chain.
5. **Reduce**
   - Aggregate list values into a single result.
6. **Combined Pipeline**
   - Map → Filter → Reduce in one expression.

---

## **Section B – File Handling**
1. **Write to a file** – `write_to_file(filename, text)`
2. **Read from a file** – `read_file(filename)`
3. **Append to a file** – `append_to_file(filename, text)`
4. **Count words in a file** – `count_words_in_file(filename)`

---

## **Section C – Error Handling**
1. **Division with zero handling** – `safe_division(a, b)`
2. **File not found handling** – `safe_file_read(filename)`
3. **Custom exception example**
   - `NegativeAgeError`
   - `check_age(age)`

---
## How to Run
```bash
python day2_prep.py
```
## Author- ALLEN ALEXANDER -aspiring python / AI-ML Developer

# Day 4 - Advanced OOP in Python

## Overview
This day covers **advanced Object-Oriented Programming concepts** in Python, split into 3 sections:

- **Section A**: Basic OOP (Class Attributes, Methods, Access Modifiers)
- **Section B**: Inheritance, Multiple Inheritance, and Polymorphism
- **Section C**: Operator Overloading (Special Methods)

---

## Section A: Basic OOP
1. **Book Class** - Basic attributes and instance methods.
2. **Laptop Class** - Class vs instance attributes.
3. **MathOps Class** - Instance methods, class methods, static methods.
4. **BankAccount Class** - Public, protected, private attributes.

---

## Section B: Inheritance & Polymorphism
1. **Vehicle & Car** - Single inheritance with method overriding.
2. **FlyingBoat** - Multiple inheritance example.
3. **Person & Student** - Method overriding.
4. **Dog & Cat** - Polymorphism via a function.
5. **BankAccount & SavingsAccount** - Real-world banking example.

---

## Section C: Operator Overloading
1. **Movie Class** - `__str__` method.
2. **Team Class** - `__len__` method.
3. **Book Class** - `__eq__` method for equality.
4. **Library Class** - `__getitem__` and `__setitem__` methods.

---

## How to Run
```bash
python day4_prep.py
```

Ensure you have Python 3.x installed.
## Author- ALLEN ALEXANDER -aspiring python / AI-ML Developer

