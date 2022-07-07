"""
In the code below, you can see a program that creates a full name from the first and last names for several people.

name1 = "John"
last_name1 = "Lennon"
full_name1 = name1 + " " + last_name1
        
name2 = "Hermione"
last_name2 = "Granger"
full_name2 = name2 + " " + last_name2

Wouldn't it be much easier if we had a function that could do the same?

Your task is to write the body of the function create_full_name that takes name and last_name (in this order) and returns the full name.

Do NOT change the variable names. You don't need to call the function yourself. 
"""

def create_full_name(name, last_name):
    return ' '.join([name, last_name])
