"""
There are three predefined variables a, b, and c, and a predefined function func():

a = 1
b = 2
c = 3

def func(a, b, c):
    return (a + b) * c

Rewrite the function func() and call it with the a, b, c variables using the lambda function features. Assign the result to the variable result.
Report a typo
"""
a = 1
b = 2
c = 3

# Don't forget to make use of lambda functions in your solution
result = (lambda a, b, c: (a + b) * c)(a, b, c)
