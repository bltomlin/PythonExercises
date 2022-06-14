"""
Write a code that for the given integer code point checks whether this code point corresponds to a printable character (as opposed to a hexadecimal escape sequence), and if yes, outputs this character, otherwise outputs False.
"""

usr_input = int(input())
for i in chr(usr_input):
    if 32 <= usr_input <= 126:
        print(chr(usr_input))
    else:
        print('False')

