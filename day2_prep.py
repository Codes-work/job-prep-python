# ---------------------------
# Day 2 - Python Job Prep (Strings, Lists, Dictionaries, Loops & Conditions)
# ---------------------------

# =========================================================
# Section A: Strings
# =========================================================

def reverse_string(s):
    """Return the reversed version of the given string."""
    return s[::-1]

def is_palindrome(s):
    """Check if the given string is a palindrome (case-insensitive)."""
    s = s.lower()
    return s == s[::-1]

def count_vowels(s):
    """Count the number of vowels in a given string."""
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)


# =========================================================
# Section B: Lists & Dictionaries
# =========================================================

def find_max_min(numbers):
    """Return the maximum and minimum from a list of numbers."""
    if not numbers:
        return None, None
    max_val = min_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return max_val, min_val

def sum_even_numbers(numbers):
    """Return the sum of all even numbers in a list."""
    return sum(num for num in numbers if num % 2 == 0)

def merge_lists_unique(list1, list2):
    """Merge two lists without duplicates, preserving order."""
    merged_list = []
    for item in list1 + list2:
        if item not in merged_list:
            merged_list.append(item)
    return merged_list

def element_frequency(lst):
    """Return a dictionary with frequency count of each element."""
    freq_dict = {}
    for item in lst:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict

def remove_duplicates(lst):
    """Remove duplicates from list while preserving order."""
    seen = set()
    new_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            new_list.append(item)
    return new_list

def merge_dicts(dict1, dict2):
    """Merge two dictionaries. Values from dict2 overwrite dict1."""
    return {**dict1, **dict2}

def average_score(students):
    """Return average score from a list of student dictionaries."""
    if not students:
        return 0
    return sum(s['score'] for s in students) / len(students)


# =========================================================
# Section C: Loops & Conditions
# =========================================================

def fizzbuzz(n):
    """Return a list of FizzBuzz strings from 1 to n."""
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def factorial(n):
    """Return factorial of a given non-negative integer. For n < 0, return None."""
    if n < 0:
        return None
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def sum_of_digits(n):
    """Return the sum of digits of an integer (handles negatives)."""
    n = abs(int(n))
    return sum(int(d) for d in str(n))

def fibonacci(n_terms):
    """Return a list containing the first n_terms of the Fibonacci sequence."""
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n_terms:
        seq.append(seq[-1] + seq[-2])
    return seq

def count_even_odd(numbers):
    """Count even and odd numbers in a list. Returns (even_count, odd_count)."""
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count

def count_even_odd_range(start, end):
    """Count even and odd numbers in the inclusive range [start, end]. Returns (even_count, odd_count)."""
    lo, hi = (start, end) if start <= end else (end, start)
    even = 0
    for x in range(lo, hi + 1):
        if x % 2 == 0:
            even += 1
    total = hi - lo + 1
    return even, total - even

def pattern_triangle(rows):
    """Return a right-angled triangle pattern as a list of strings (one row per line)."""
    return ["*" * i for i in range(1, rows + 1)]


# ---------------------------
# Test area (quick sanity checks)
# ---------------------------
if __name__ == "__main__":
    # Section A
    print("A:", reverse_string("hello"), is_palindrome("Madam"), count_vowels("hello world"))

    # Section B
    print("B:",
          find_max_min([10, 4, 67, 29, 5]),
          sum_even_numbers([10, 4, 67, 29, 5]),
          merge_lists_unique([1, 2, 3, 4], [3, 4, 5, 6]),
          element_frequency([1, 2, 2, 3, 4, 4, 4, 5]),
          remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]),
          merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}),
          round(average_score([{"name": "Alice", "score": 85}, {"name": "Bob", "score": 90}]), 2)
    )

    # Section C
    print("C:",
          fizzbuzz(15),
          factorial(5),
          sum_of_digits(-12345),
          fibonacci(8),
          count_even_odd([1, 2, 3, 4, 5]),
          count_even_odd_range(1, 10)
    )
    print("\n".join(pattern_triangle(5)))
