#You are playing a guessing game with a user. Imagine that you came up with an integer stored in a variable set_number.

#Check if set_number is equal to the product of two integers entered by the user.

set_number = 6557
int_one = int(input())
int_two = int(input())
ans = (int_one * int_two) == set_number
print(ans)
