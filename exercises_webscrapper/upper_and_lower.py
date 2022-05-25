"""
A some_iterable stores words from a sentence. Use dictionary comprehension to create a new dictionary, in which keys will be words from some_iterable, written in uppercase letters, and values will be the same words written in lowercase letters. Print this dictionary.
"""

some_iterable = input().split()
dictionary = {}

for i in some_iterable:
    another_dictionary = {i.upper(): i.lower()}
    dictionary.update(another_dictionary)

print(dictionary)
