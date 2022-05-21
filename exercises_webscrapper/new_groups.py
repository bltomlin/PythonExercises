"""
A kindergarten in Berlin may open a certain amount of new groups. Their names are in the list groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']. Children are divided into groups starting from 1A and ending with 3C. However, if there are not so many kids, only the first groups in the list will be filled up.

From the first line in the input, read the number of groups that will be filled. And in the next lines — the number of children in each group in the order in which they are listed in the groups. If the first number is less than 9 (and there are less than nine values after it), it means that the last groups are not starting this year.

Create a dictionary, where group names will be written as keys, and the number of kids in the group as values.
For unfilled groups, assign the value None. Finally, print the filled dictionary.
"""

groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

dict_group = dict.fromkeys(groups)
for i in range(int(input())):
    value = input()
    dict_group = {key: value for key in groups}
print(dict_group)


