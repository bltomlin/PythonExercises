#Write a program that recommends one of the following movies based on the age of a user:

#The user enters their age and the program outputs one title.

user_age = int(input())
lion_king = range(0, 17)
trainspotting = range(17, 26)
matrix = range(26, 41)
pulp_fiction = range(41, 61)


if user_age in lion_king:
    print('Lion King')
elif user_age in trainspotting:
    print('Trainspotting')
elif user_age in matrix:
    print('Matrix')
elif user_age in pulp_fiction:
    print('Pulp Fiction')
else:
    print("Breakfast at Tiffany's")