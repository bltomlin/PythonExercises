"""
Write a code that converts the given string to a bytes object and outputs its last item. 
"""

usr_input = bytes(input(), encoding='utf-8')
last_byte = ''
for i in usr_input:
    last_byte = i
print(last_byte)
