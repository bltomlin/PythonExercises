#Program to convert from camel case to snake case.

word = input()
new_word = ''
for char in word:
    if char.isupper():
        underscore = '_'
        char = char.lower()
        new_word += underscore
        new_word += char
    else:
        new_word += char
print(new_word)