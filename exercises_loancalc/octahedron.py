import math

user_input = float(input())
area = 2 * math.sqrt(3) * pow(user_input, 2)
volume = (1/3) * math.sqrt(2) * pow(user_input, 3)
print(round(area, 2))
print(round(volume, 2))