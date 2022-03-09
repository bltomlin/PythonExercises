#FizzBuzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
number = int(input())

if number % 3 == 0 and number % 5 != 0:
	print("Fizz")
if number % 5 == 0 and number % 3 != 0:
	print("Buzz")
if number % 5 == 0 and number % 3 == 0:
	print("FizzBuzz")
print(range(number + 1, 100))