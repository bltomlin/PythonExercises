"""
Write a program that reads a user's name from input and prints the following message: Dear <username>! It was really nice to meet you. Hopefully, you have a nice day! See you soon, <username>!. Change the word <username> with the word that is provided in the input. We recommend using string templates from the string module to complete the task.
"""

import string

my_template = string.Template("Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $username!")
my_str = my_template.substitute(username=input())
print(my_str)
