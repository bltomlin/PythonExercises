#Create a function called grades() that should take a grade as an argument (it can be 'A', 'B', 'C', 'D' or 'F'). If a correct parameter is given to the function, return the message "You have got <grade>", where <grade> is the given parameter. If there is something else as a parameter, use the assert keyword.

#You do not need to take any input or call the function yoursel.

def grades(x):
    assert x in "ABCDF"
    return "You have got " + x
