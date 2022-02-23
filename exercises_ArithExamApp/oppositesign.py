#[200~Read an integer as input and print it with the opposite sign.

number = input()
if number[0] == '-':
    number = int(number) * -1
    print(number)
else:
    print('-' + number)
