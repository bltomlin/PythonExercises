#Given a string in quotes, print it out without quotation marks.

string = input()
length = len(string)
print(string[1:length - 1])