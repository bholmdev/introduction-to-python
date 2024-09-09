#!/bin/python3

def drink(money):
    if money >= 2:
        return "You've got yourself a Mountain Dew!"
    else:
        return "No Mountain Dew for you!"
    
print(drink(1))
print(drink(2))

def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money <= 5):
        return "Come back with more money."
    elif (age <= 21) and (money >=5):
        return "Nice try, kid!"
    else:
        return "You're too young and too poor."
    
print(alcohol(22, 5))
print(alcohol(22, 4))
print(alcohol(20, 5))
print(alcohol(20, 4))