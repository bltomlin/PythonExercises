#In this task, you have to make sure that the user entered the necessary amount of words and...

#If there are more or fewer words in the input, print an error: "You need to enter exactly 2 words. Try again!"
#If everything's good, greet the user personally.

name, surname = input().split()
try:
    if name.count() == 1 and surname.count == 1:
        print('Welcome to our party, ' + name + ' ' + surname)