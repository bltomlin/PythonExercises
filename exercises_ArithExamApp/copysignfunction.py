#Write a program that takes two float numbers, x and y, and prints x with the sign of y. Use copysign function defined in the math module.

import math

x, y = map(float, input().split(' '))
print(math.copysign(x, y))
