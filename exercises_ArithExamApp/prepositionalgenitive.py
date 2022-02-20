#Advanced input() handling is used to read input directly into several variables, for example:

#x, y = input().split()

#Use it to print the next message with the two input values: "x of y"

x, y = input().split()
of = ' of '
sentence = x + of + y
print(sentence)

