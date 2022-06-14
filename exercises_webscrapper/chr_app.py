"""
Construct and output a single string by means of converting four given code points to Unicode characters. 
"""

word = ''
for i in range(4):
    word += chr(int(input()))
print(word)
