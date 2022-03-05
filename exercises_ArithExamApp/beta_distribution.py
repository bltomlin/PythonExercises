#Generate a number from the beta distribution with parameters alpha=0.9 and beta=0.1. Print your result.

import random

zero_nine, zero_one = 0.9, 0.1
random.seed(3)
print(random.betavariate(zero_nine, zero_one))
