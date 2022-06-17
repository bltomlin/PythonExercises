"""
Write a code that takes a given number, converts it to a bytes object and outputs the sum of its bytes.

A little spoiler: the test numbers are going to be greater than 255, so you're going to need at least 2 bytes to encode them. 
"""

usr_input = (int(input())).to_bytes(2, byteorder='little')
ans = 0
for i in usr_input:
    ans += i
print(ans)
