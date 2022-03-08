#Create a function called check() that takes no arguments. You should read an integer input inside the function. The function checks whether a number lies between 25 and 37. If the input is an expected or border value, print it. If it is out of the specified range or it is the ValueError, print the message "Correct the error!"

def check():
    try:
        x = int(input())
    except ValueError:
        print("Correct the error!")
    else:
        if 25 <= x <= 37:
            print(x)
        else:
            print("Correct the error!")