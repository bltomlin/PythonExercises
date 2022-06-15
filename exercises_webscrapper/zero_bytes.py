"""
Read the integer number from the input. Create a bytes object of the length equal to the specified integer filled with zero bytes and print it.
"""

integer = int(input())
integer_bytes = (0).to_bytes(integer, byteorder='little')
print(integer_bytes)
