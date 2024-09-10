#!/bin/python3

# user_name = input("Enter your name: ")
# print("Hello " + user_name + "!")
# drink = input("What's your favorite drink?")
# print("Welcome " + user_name + "! Have a " + drink + "!")

x = float(input("Give me a number:  "))
y = float(input("Give me a second number:  "))
o = input("Give me an operator:  ")

if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "*":
    print(x * y)
elif o == "/":
    print(x / y)
elif o == "**" or o == "^":
    print(x ** y)
else:
    print("Please input a \"+\", \"-\", \"*\", \"/\", \"**\", or an \"^\"")