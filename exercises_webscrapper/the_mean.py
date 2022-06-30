"""
Calculate the arithmetic mean of integer numbers and output it. You will receive the integers on separate lines. The numeric sequence ends with a period ., so stop reading the input on it.

Don't round your result before outputting it.

The input will always have at least one number. 
"""

import sys

num = input()
terms = 0
summ = 0
while num != '.':
    summ += int(num)
    terms += 1
    num = input()
if terms != 0:
    print(float(summ / terms))
else:
    sys.exit()
