#The function closest_higher_mod_5 takes exactly one integer argument x and returns the smallest integer y such that:

#    y is greater than or equal to x,
#    y is divisible by 5.

#Correct the last line of the code below to make the function work.

def closest_higher_mod_5(x):
    y = x
    while y % 5 != 0:
        y += 1
    remainder = y % 5
    if remainder == 0 and y >= x:
        return y
    return "I don't know :("
