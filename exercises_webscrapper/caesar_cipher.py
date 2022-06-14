usr_in = input()
new_string = ""
for i in usr_in:
    character = ord(i) + 1
    new_string += (chr(character))
print(new_string)
