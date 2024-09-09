#!/bin/python3

# Boolean Expressions and Relational Operators

bool1 = True
bool2 = 3 * 3 == 9 # This is a true statement so makes it a bool true
bool3 = False
bool4 = 3 * 3 != 9 # This a false statement so makes it a bool false

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True" # This is a string
print(type(bool5)) # type() will show it as a string

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
test_and = (7 > 5) and (5 < 7)
test_and2 = (7 > 5) and (5 > 7) # Both statements must be true to return true
test_or = (7 > 5) or (5 > 7) # Only one statement must be true to return true
test_or2 = (7 < 5) or (5 > 7) # Both statements are false returns false

print(greater_than)
print(less_than)
print(greater_than_equal_to)
print(less_than_equal_to)
print(test_and)
print(test_and2)
print(test_or)
print(test_or2)

test_not = not True # False
print(test_not)