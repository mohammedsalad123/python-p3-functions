#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
print(greet_programmer())

def greet(name):
    print(f"Hello, {name}!")
print(greet("Guido"))
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
print(greet_with_default())
greet_with_default()
greet_programmer()
def add(num1, num2):
    return num1 + num2
add(2,3)
def halve(number):
    return number/2
halve(3)