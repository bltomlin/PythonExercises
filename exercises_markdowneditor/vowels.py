"""
Read a string from the input and print a list of vowels that belong to that string.

All vowels are enlisted in a variable of the same name.
"""
vowels = ['a', 'e', 'i', 'o', 'u']
usr_input = input()
print([letter for letter in usr_input if letter in vowels])
