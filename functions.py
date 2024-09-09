#!/bin/python3

def who_am_i():  # This is a function without parameters
    name= "Fredo" # Must indent!!!
    age = 42 # Variables within functiosn are scoped locally only in that function
    print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x, y):
    print(x + y)

add(7, 7)

def multiply(x, y):
    return x * y

multiply(7, 7)
print(multiply(7, 7))

def square_root(x):
    print(x ** 0.5)

square_root(64)

def new_line():
    print("\n")

print("line one")
new_line()
print("line 3")
