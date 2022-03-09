#FizzBuzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)