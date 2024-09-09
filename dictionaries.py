#!/bin/python3

# Dictionaries - classes or key/value pairs

drinks = {
    "White Russian": 7,
    "Old Fashioned": 10,
    "Lemon Drop": 8
}

print(drinks)

employees = {
    "Finance": [
        "Bog",
        "Linda",
        "Tina"
    ],
    "IT": [
        "Gene",
        "Louise",
        "Teddy"
    ],
    "HR": [
        "Jimmy Jr",
        "Mort"
    ]
}

print(employees)

employees["Legal"] = ["Mr. Frond"]
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})

print(employees)

drinks["White Russian"] = 8

print(drinks)

print(drinks.get("White Russian"))