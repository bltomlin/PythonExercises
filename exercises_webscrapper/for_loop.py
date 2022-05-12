"""
Write a program that calculates the arithmetic mean. The arithmetic mean is a sum of all numbers divided by their total count.

The input format:

Read an integer number n. This is a number of integer values you will receive on the next n lines.

Your program should compute the mean value of those n integers.

The output format:

Print the mean as a float number.
"""

n = int(input())
total = 0

for i in range(n):
    number = int(input())
    total += number

print(total / n)