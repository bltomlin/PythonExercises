"""
Write a program that prints keys for the minimum and maximum values of the dictionary.

You are supposed to work with the variable test_dict which is a dictionary.

Sample output for the dictionary {"a": 43, "b": 1233, "c": 8} should be as follows:

min: c
max: b
"""

dict = {"a": 43, "b": 1233, "c": 8}
min = ''
max = ''
for key, value in dict.items():
    for key_alt, value_alt in dict.items():
        if value_alt > value:
            max = key_alt
        if value_alt < value:
            min = key_alt
print('min: ' + min)
print('max: ' + max)
