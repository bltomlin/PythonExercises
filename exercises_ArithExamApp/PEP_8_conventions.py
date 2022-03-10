#Write the function check_name() that checks if an input variable name is in accordance with PEP 8 conventions:

#Check if the variable name equals 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye). If it does, print "Never use the characters 'l', 'O', or 'I' as single-character variable names". If it does not, move to the next step.
#Check if the name is all lowercase or uppercase. If all of its characters are lowercase, print the message "It is a common variable". If all of its characters are uppercase, print the message "It is a constant". In other cases, print the message "You shouldn't use mixedCase".


def check_name(name):

    if name == 'l' or name == 'O' or name == 'I':
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif name.islower():
        print("It is a common variable")
    elif name.isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
