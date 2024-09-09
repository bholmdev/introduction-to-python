#!/bin/python3

quote = "All is fair in love and war."
print(quote)

print(quote.upper())
print(quote.lower())
print(quote.title())
print(len(quote))

name = "Fredo"
age = 41
gpa = 3.7

print(age)
print(int(30.1))
print(int(30.9)) # Will it round?  NO
print(round(30.3)) # Will it round? YES
print(round(30.9))

age += 1

print("My name is " + name + ", I am " + str(age) + " years old, and have a gpa of " + str(gpa) + ".")

birthday = 1
age += birthday
print("Age: " + str(age))