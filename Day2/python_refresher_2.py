# Object Oriented Programming 

class InsufficientFunds(Exception):
    pass

# Encapusulation
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder
        self.__balance = balance
        
    def deposit(self, amount):
        try:
            if amount > 0:
                self.__balance += amount
                return f"${amount} deposited. New balance: ${self.__balance}"
             
        except Exception as e:
            print({e})
    def withdraw(self, amount):
        try:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                return f"${amount} Withdrawn. Remaining balance: ${self.__balance}"
        except InsufficientFunds:
            print("Insufficient balance or invalid amount")
    
    def get_balance(self):
        return f"Account balance for {self.__account_holder}: ${self.__balance}"

#Usage 
# account = BankAccount("Josh", 10000)
# print(account.deposit(2000))
# print(account.withdraw(4000))
# print(account.get_balance())

""" Inheretance: Employee Management System """

class InfoNotFound(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_info(self):
        return f"Name: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def display_info(self):
        try:
            return f"{super().display_info()}, Department: {self.department}"
        except InfoNotFound:
            print("Information not found")

    """

    Returns:
        _type_: _description_
    """
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def display_info(self):
        return f"{super().display_info()}, Programming Language: {self.programming_language}"
    
# Usage
# manager = Manager("Alice", 20000, "HR")
# developer = Developer("Bob", 7000, "Python")

# print(manager.display_info())
# print(developer.display_info())

""" Polymorphism: Shape Area Calulator """
from math import pi

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__ (self, width, height):
        self.height = height
        self.width = width
        
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Usage
shapes = [Circle(5), Rectangle(4,8), Square(3)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
    
""" Abstraction: Payment System """
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing Credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processitn PayPal payment of ${amount}"

class PaymentError(Exception):
    pass
 
# Usage
try:
    def make_payment(processor, amount):
        print(processor.process_payment(amount))

except PaymentError:
    print("Inpute valid amount and Processsor")
    
credit_card = CreditCardProcessor
paypal = PaymentProcessor

make_payment(credit_card, 100)
make_payment(paypal, 200)