"""
Write a program that reads integers from the console, one number per line.

For each input number you should check:

    if the number is less than 10, then skip this number;
    if the number is greater than 100, then stop reading numbers from the console;
    in other cases, print this number back to the console on a separate line.
"""

import sys

x = int(input())
while x <= 100:
    if x < 10:
        pass
    else:
        print(x)
    x = int(input())
sys.exit()
