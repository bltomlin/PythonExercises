#The string below has an encoded message. To find out what it is, take every 5th letter starting from the first one, and then reverse the sequence. Spaces are considered as symbols here. Don't forget to print what you've got!

string = "no clouds here to spy on pets"
string = string[::5]
print(string[::-1])
