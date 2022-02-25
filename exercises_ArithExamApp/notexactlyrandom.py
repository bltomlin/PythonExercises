#Write a program that takes an integer number n, sets a random number generator (the seed) to that number, and then prints a pseudo-random number from -100 to 100.

from random import seed, randint

n = int(input())
seed(n)
print(randint(-100, 100))
