"""
James is hosting a party today. He decided to welcome all new guests personally. To remember their names, James kindly asks you to write them in a list. Read the names from the input, each on a new line, and stop at a single period . that denotes the end of the sequence.

Print your list and its length (the number of guests) for James.
"""

a_list = []
usr_input = input()
count = 0
while usr_input != '.':
    count += 1
    a_list.append(usr_input)
    usr_input = input()
print(a_list)
print(count)
