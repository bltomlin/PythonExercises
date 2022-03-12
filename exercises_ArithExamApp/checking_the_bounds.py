#Define a function bounds() that will take a number as an argument. Return the number if it lies between 50 and 70 inclusively. If it lies beyond the range, use the assert keyword with the message: "Your number is wrong!".

#You do not need to take any input or call the function yourself.

def bounds(x):
    message = "Your number is wrong!"
    assert 50 <= x <= 70, message
    return x
