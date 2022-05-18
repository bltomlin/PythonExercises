"""
In a standard deck of cards, there are 13 of each suit. There are numbered cards (from 2 to 10) and face cards (Jack, Queen, King, and Ace). If we were to rank the face cards, Jack would be 11, Queen 12, King 13, and the Ace 14.

Write a program that calculates the average rank of one hand of cards. Don't forget to consider the rank of the face cards.

The input format:

Six values of cards, each on a separate line.

The output format:

The average rank of the hand.
"""
total_count = 0
i = 0
while i != 6:
	user_input = input()
	try:
		user_input = int(user_input)
	except ValueError:
		if user_input == 'Jack':
			user_input = 11
		elif user_input == 'Queen':
			user_input = 12
		elif user_input == 'King':
			user_input = 13
		else:
			user_input = 14
	total_count += user_input
	i += 1
print(total_count / 6)
