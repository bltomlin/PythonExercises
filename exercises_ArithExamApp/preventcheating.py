#On Hyperskill, sometimes we need to check that the student's code doesn't use a particular method. For instance, when the task is to implement the computation of factorial manually instead of using the function factorial() from the math module. How could we do that?

import math

def new_math_factorial(integer):
    integer = "Don't cheat!"
    print(integer)

math.factorial = new_math_factorial

a = 23
math.factorial(a)
