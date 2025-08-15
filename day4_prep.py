"""
Day 4 Preparation - Object-Oriented Programming (Advanced)
Sections: A (Basic OOP), B (Inheritance & Polymorphism), C (Operator Overloading)
"""

# ==========================
# SECTION A: BASIC OOP
# ==========================

# A.1: Basic Class and Instance Attributes
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


book1 = Book("Atomic Habits", "James Clear", 320)
book1.display_info()


# A.2: Class Attributes
class Laptop:
    brand = "Dell"  # Class attribute

    def __init__(self, model, price):
        self.model = model
        self.price = price


l1 = Laptop("XPS 13", 1200)
l2 = Laptop("Inspiron 15", 800)
print(l1.brand, l1.model, l1.price)
print(l2.brand, l2.model, l2.price)


# A.3: Instance Methods, Class Methods
class MathOps:
    def add(self, x, y):
        return x + y

    @classmethod
    def description(cls):
        print("MathOps Utility Class")

    @staticmethod
    def multiply(x, y):
        return x * y


math_ops = MathOps()
print(math_ops.add(5, 6))
math_ops.description()
print(MathOps.multiply(4, 6))


# A.4: Public, Protected, and Private Attributes
class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder  # public
        self._balance = balance               # protected
        self.__pin = pin                      # private

    def display_balance(self):
        print(f"Balance = {self._balance}")


holder = BankAccount("Yolo", 25000, 1234)
print(f"Account holder = {holder.account_holder}")
holder.display_balance()
print(f"Pin = {holder._BankAccount__pin}")  # Name mangling access


# ==========================
# SECTION B: INHERITANCE & POLYMORPHISM
# ==========================

# B.1: Single Inheritance with Method Overriding
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Doors: {self.doors}")


my_car = Car("Toyota", "Camry", 4)
my_car.display_info()


# B.2: Multiple Inheritance
class Flyable:
    def fly(self):
        print("This vehicle can fly")


class Sailable:
    def sail(self):
        print("This vehicle can sail")


class FlyingBoat(Flyable, Sailable):
    def describe(self):
        print("This is an amphibious vehicle")


fb = FlyingBoat()
fb.fly()
fb.sail()
fb.describe()


# B.3: Method Overriding
class Person:
    def greet(self):
        print("Hello")


class Student(Person):
    def greet(self):
        print("Hi, I’m a student!")


stu = Student()
stu.greet()


# B.4: Polymorphism Example
class Dog:
    def speak(self):
        print("Woof woof")


class Cat:
    def speak(self):
        print("Meow meow")


def animal_sound(animals):
    for animal in animals:
        animal.speak()


animal_list = [Dog(), Cat()]
animal_sound(animal_list)


# B.5: Banking Example with Inheritance
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}, Balance: {self.balance}")
        else:
            print("Amount must be greater than zero")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}, Balance: {self.balance}")


holder = SavingsAccount("John", 1000, 0.1)
holder.deposit(10000)
holder.withdraw(1000)
holder.add_interest()


# ==========================
# SECTION C: OPERATOR OVERLOADING
# ==========================

# C.1: __str__ Method
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"Movie: {self.title} ({self.year})"


m = Movie("Inception", 2010)
print(m)


# C.2: __len__ Method
class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


player_team = Team(['player1', 'player2', 'player3'])
print(len(player_team))


# C.4: __eq__ Method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.author == other.author and self.title == other.title


b1 = Book("Alice", "blah")
b2 = Book("Alice", "blah")
b3 = Book("Bob", "yoloo")

print(b1 == b2)  # True
print(b1 == b3)  # False


# C.5: __getitem__ and __setitem__
class Library:
    def __init__(self):
        self.books = {}

    def __setitem__(self, key, value):
        self.books[key] = value

    def __getitem__(self, key):
        return self.books.get(key, "Item not found")


cart = Library()
cart['blaah'] = 8
print(cart['blaah'])
print(cart['yoloo'])
