"""
A palindrome is a word or a text that reads the same backward as forward. Create a program that checks if the word is a palindrome.

The input format:

Word that needs to be checked. It is guaranteed that the word will be of even length.

The output format:

If the word is a palindrome, write Palindrome. Otherwise, write Not palindrome.
"""

user_input = str(input())
reverse_input = user_input[::-1] 
if user_input = reverse_input:
    print('Palindrome')
else:
    print('Not palindrome')
