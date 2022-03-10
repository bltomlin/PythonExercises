#Create a function called check() that takes a string. First, check whether the string is a number. If it is not, print the message "It is not a number!" If it is, change the type of your input value to int and check whether the number is more than 202 or equal to 202. If so, print the number. Otherwise, print another message "There are less than 202 apples! You cheated me!"

def check(some_string):
    if some_string.isdigit():
        if int(some_string) >= 202:
            print(int(some_string))
        else:
            print("There are less than 202 apples! You cheated me!")
    else:
        print("It is not a number!")
