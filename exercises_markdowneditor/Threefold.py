"""
Print a list of numbers from 1 to 1000 that can be divided by 3.
"""
new_list = [num for num in range(1, 1000) if num % 3 == 0]
print(new_list)
