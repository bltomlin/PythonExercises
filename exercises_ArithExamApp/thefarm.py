#Write a program that determines what is the most expensive animal that the user can buy with their money and how many of them they can buy. 

import math

money = int(input())
if money < 23:
    print('None')
elif money >= 23 and money < 678:
    answer = math.floor(money/23)
    if answer >= 2:
        print(str(answer) + ' chickens')
    else:
        print(str(answer) + ' chicken')
elif money >= 678 and money < 1296:
    answer = math.floor(money/678)
    if answer >= 2:
        print(str(answer) + ' goats')
    else:
        print(str(answer) + ' goat')
elif money >= 1296 and money < 3848:
    answer = math.floor(money/1296)
    if answer >= 2:
        print(str(answer) + ' pigs')
    else:
        print(str(answer) + ' pig')
elif money >= 3848 and money < 6769:
    answer = math.floor(money/3848)
    if answer >= 2:
        print(str(answer) + ' cows')
    else:
        print(str(answer) + ' cow')
else:
    answer = math.floor(money/6769)
    print(str(answer) + " sheep")
