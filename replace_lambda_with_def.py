"""
Consider the following lambda function:

lambda x: -1 if x < 0 else 1

Can you see what it does? Define an equivalent 'normal' (non-anonymous) function.
"""
def my_function(x):
    if x < 0:
        return -1
    else:
        return 1
