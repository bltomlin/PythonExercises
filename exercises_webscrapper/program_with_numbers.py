"""
A school has decided to create three new math groups and equip three classrooms for them with new desks. Your task is to calculate the minimum number of desks to be purchased. To do so, you'll need the following information:

The number of students in each of the three groups is known: your program will receive three non-negative integers as the input. It is possible that one or more of them will be zero, so you should take it into account.
Each group will sit in its own classroom. It means that you should calculate the number of desks for each classroom separately, and only then add them up!
At most two students may sit at any desk. You are expected to output the minimum number of desks to buy, so there should be as many as possible desks taken by two students rather than one.
Most probably, you'll need operations // and % in your program!
"""

import math

num_students_classroom_1 = int(input())
num_students_classroom_2 = int(input())
num_students_classroom_3 = int(input())

total_desk_classroom_1 = math.ceil(num_students_classroom_1 / 2)
total_desk_classroom_2 = math.ceil(num_students_classroom_2 / 2)
total_desk_classroom_3 = math.ceil(num_students_classroom_3 / 2)

total_desk = total_desk_classroom_1 + total_desk_classroom_2 + total_desk_classroom_3
print(math.floor(total_desk))