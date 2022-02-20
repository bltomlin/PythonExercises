#The code below is supposed to find all website addresses (https://, http://, www.) in the input text. However, it is not finished and there are several mistakes in the code. Find the mistakes, fix them and print all the addresses in the order in which they appear in the text, each on a new line.

text = input()
words = text.split()
for word in words:
    if 'www.' in word and len(word) > 5:
        print(word)
    if 'WWW.' in word and len(word) > 5:
        print(word)
    if 'http://' in word and len(word) > 7:
        print(word)
    if 'HTTP://' in word and len(word) > 7:
        print(word)
    if 'https://' in word and len(word) > 8:
        print(word)
    if 'HTTPS://' in word and len(word) > 8:
        print(word)
