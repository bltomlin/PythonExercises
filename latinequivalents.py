# Imagine you're working at IMDb and your new task is to write a program that will replace all the letters with ligatures and diacritic marks with their equivalents from the Latin alphabet in the celebrities' names

name = input()

def normalize(name):

    # put your code here
    new_name = name.replace("é", "e")
    new_name = new_name.replace("ë", "e")
    new_name = new_name.replace("á", "a")
    new_name = new_name.replace("å", "a")
    new_name = new_name.replace("œ", "oe")
    new_name = new_name.replace("æ", "ae")

    return new_name

print(normalize(name))
