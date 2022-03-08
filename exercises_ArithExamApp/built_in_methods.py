#Create a function called check() that takes a string password. The function checks whether an imaginary password contains letters or digits. The letters may be lowercase, uppercase or a combination of both. If the string is a valid password, print it. If it contains anything else, print the message "There is a wrong string!"

def check(x):
    if x.isalnum():
        print(x)
    else:
        print("There is a wrong string!")