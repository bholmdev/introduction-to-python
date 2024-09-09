#!/bin/python3

movies = ["Donnie Darko", "Transformers the Movie", "Pirates of the Carribbean", "Insidious"]
print(movies)
print(movies[1]) # Index starts at 0
print(movies[0])
print(movies[1:3])
print(movies[1:])
print(movies[:1])
print(movies[:2])
print(movies[-1])
print(movies[1:-1])

print(len(movies))
movies.append("Nightmare on Elm Street")
print(movies)
movies.insert(2, "Friday the 13th")
print(movies)
movies.pop()
print(movies)
movies.pop(2)
print(movies)

betty_movies = ["Ghostbusters", "Ghostbusters 2", "Ghostbusters: Afterlife", "Ghostbusters: Frozen Empire"]

all_movies = movies + betty_movies
print(all_movies)

# 2D Lists
grades = [["Bob", 82], ["Alic", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)