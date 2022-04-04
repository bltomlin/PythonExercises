import math

user_input = float(input())
radians = math.radians(user_input)

print((math.cos(user_input) - math.sin(user_input)) * -1)