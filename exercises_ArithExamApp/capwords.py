#In Python, the names of classes follow the CapWords convention. Let's convert the input phrase accordingly by capitalizing all words and spelling them without underscores in-between.

phrase = input()
temp = phrase.split('_')
phrase = ''.join(element.title() for element in temp[0:])
print(str(phrase))

