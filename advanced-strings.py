#!/bin/python3

my_name = "Fredo"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence)
print(sentence[:4])
print(sentence.split())

sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)
print(sentence_join)
sentence_join2 = ", ".join(sentence_split)
print(sentence_join2)

quote = "He said, 'give me all your money!'"
print(quote)
quote = "He said, \"Give me all your money!\""
print(quote)

too_much_space = "                   hello                "
print(too_much_space)
print(too_much_space.strip())

print("A" in "Apple")
print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower())
print(letter.lower() in word.lower())

movie = "The Hangover"
print("My favorite movei is " + movie + ".")
# or
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.") # String literal is preferred