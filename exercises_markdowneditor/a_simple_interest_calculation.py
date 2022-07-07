"""
Below you can find a simple program that performs simple interest calculation. The part that asks a user for the needed data has already been written for you. Now you need to write the final parts that will do all the heavy lifting:

    calculate() should perform interest calculation and return the final interest amount and the total sum.
    print_result() should print out the final interest amount and the total sum, as shown in the Sample Output below.

Here is the formula for calculating the interest: interest=amount×interest  rate×time100 interest = \frac {amount \times interest\;rate \times time}{100}interest=100amount×interestrate×time​

In the Sample Input below, the first number is the starting amount, followed by the interest rate in % and the number of years.

You do NOT need to call the functions, just complete them!
"""
def calculate(amount, interest_rate, time):
    interest = (amount * interest_rate * time) / 100
    total_amount = interest + amount
    return interest, total_amount

def print_result(interest, total_amount):
    print(' '.join(['The interest is:', str(interest)]))
    print(' '.join(['The total amount is:', str(total_amount)]))
