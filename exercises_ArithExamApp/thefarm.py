#Write a program that determines what is the most expensive animal that the user can buy with their money and how many of them they can buy. 

money = int(input())
if money < 23:
    print('None')
elif money > 23 and money < 678:
    answer = round(money/23)
    if answer >= 46:
        print(str(answer) + ' chicken')
    else:
        print(str(answer) + ' chickens')
elif money > 678 and money < 1296:
    answer = round(money/678)
    if answer >= 678:
        print(str(answer) + ' goat')
    else:
        print(str(answer) + ' goat')
elif money > 1296 and money < 3848:
    answer = round(money/1296)
    if answer >= 2592:
        print(str(answer) + ' pig')
    else:
        print(str(answer) + 'pigs')
elif money > 3848 and money < 6769:
    answer = round(money/3848)
    if answer >= 7696:
        print(str(answer) + ' cow')
    else:
        print(str(answer) + ' cows')
else:
    answer = round(money/6769)
    if answer >= 13538:
        print(str(answer) + ' sheep')
    else:
        print(str(answer) + ' sheeps')

