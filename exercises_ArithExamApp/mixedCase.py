#Convert a text into lowerCamelCase, or mixedCase.

phrase = input()
temp = phrase.split(' ')
phrase = temp[0] + ''.join(element.title() for element in temp[1:])
print(str(phrase))
