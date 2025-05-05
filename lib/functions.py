#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")
    pass

greet("Naureen")



def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

greet_with_default()


def add(num1, num2):
    return num1 + num2

add(45,55)


def halve(number):
    return number / 2

halve(100)
