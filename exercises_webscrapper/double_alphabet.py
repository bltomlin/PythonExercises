"""
Write a program that creates a dictionary, in which keys are latin letters, and values are their doubling:

{a: aa, b: bb, ..., z: zz}

Save this dictionary in the variable double_alphabet.
"""

import string

double_alphabet = {}
alphabet = string.ascii_lowercase
for i in alphabet:
    letter = i
    double = i + i
    combo = {letter: double}
    double_alphabet.update(combo)