#Implement a function called check() that takes a number as an argument. The function checks whether the number lies between 120 and 137. If the input is as expected, print it. If it is border or invalid, print the message "That's a bad present!"

def check(x):
    if 120 < x < 137:
        print(x)
    else:
        print("That's a bad present!")