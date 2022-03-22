"""
Write a program that reads numbers until a user enters 5555. 
Once 5555 is entered, stop reading the input, print out how many numbers 
have been entered, their total sum, and average (do the rounding this way: 
round(number)). Do NOT include 5555 in your calculations and print each 
resulting value on a new line in the order given above.
"""
numbers_entered = 0
total_sum = 0
user_input = int(input())
numbers_entered += 1
while user_input != 55:
	numbers_entered += 1
	user_input = int(input())
	total_sum += user_input
print(numbers_entered)
print(total_sum)
print(round(total_sum / numbers_entered))