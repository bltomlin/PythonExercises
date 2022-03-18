#Write a program that takes a single integer number n and then performs the following operations in the following order:

#adds n to itself
#multiplies the result by n
#subtracts n from the result
#exactly divides the result by n (that means, you need to carry out integer division).

n = int(input())
n = (((n + n) * n) - n) / n
print(int(n))
