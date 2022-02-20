#Write a program that reads a sequence of numbers from the first line and the number x from the second line. Then it should output all positions of x in the numerical sequence.

#The position count starts from 0. In case x is not in the sequence, print the line "not found" (quotes omitted, lowercased).

#Positions should be displayed in one line, in ascending order of the value.

sequence = input()
number = input()
sequence = sequence.split(' ')
array = []
for count, value in enumerate(sequence):
    value = int(value)
    if value == int(number):
        array.append(count)
if array:
    print(*array)
else:
    print('not found')
