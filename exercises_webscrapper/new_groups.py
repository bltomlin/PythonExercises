"""
A kindergarten in Berlin may open a certain amount of new groups. Their names are in the list groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']. Children are divided into groups starting from 1A and ending with 3C. However, if there are not so many kids, only the first groups in the list will be filled up.

From the first line in the input, read the number of groups that will be filled. And in the next lines — the number of children in each group in the order in which they are listed in the groups. If the first number is less than 9 (and there are less than nine values after it), it means that the last groups are not starting this year.

Create a dictionary, where group names will be written as keys, and the number of kids in the group as values.
For unfilled groups, assign the value None. Finally, print the filled dictionary.
"""

groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

dict_group = dict.fromkeys(groups)
num = '1'
letter = 'A'
for i in range(int(input())):
    value = input()
    if i in (0, 3, 6):
        letter = 'A'
    if i in (1, 4, 7):
        letter = 'B'
    if i in (2, 5, 8):
        letter = 'C'
    if i == 3:
        num = '2'
    if i == 6:
        num = '3'
    dict_key = str(num) + letter
    another_dictionary = {dict_key: int(value)}
    dict_group.update(another_dictionary)
print(dict_group)



