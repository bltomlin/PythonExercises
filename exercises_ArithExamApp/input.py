#Read a line from input and write it to the file input.txt.

user_input = input()
file = open('input.txt', 'w', encoding='utf-8')
file.write(user_input)
file.close()