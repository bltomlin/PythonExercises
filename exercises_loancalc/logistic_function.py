import math

x = float(input())
result = 1 / (1 + pow(math.e, (-1 * x)))
print(round(result, 2))