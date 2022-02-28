#Operations are: +, -, /, *, mod, pow, div

first_number, second_number = float(input()), float(input())
command = input()

if command == 'mod':
    if second_number == 0:
        print('Division by 0!')
    else:
        mod = first_number % second_number
        print(mod)
elif command == 'pow':
    print(first_number ** second_number)
elif command == 'div':
    if second_number != 0:
        print(first_number // second_number)
    else:
        print('Division by 0!')
elif command == '*':
    print(first_number * second_number)
elif command == '+':
    print(first_number + second_number)
elif command == '/':
    if second_number != 0:
        print(first_number / second_number)
    else:
        print('Division by 0!')
elif command == '-':
    print(first_number - second_number)
else:
    print('Try again.')