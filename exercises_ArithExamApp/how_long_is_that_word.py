#Write a program that calculates the length of a word from the input and prints it out together with the word in the format word has N letters. There will always be more than one letter in the word.

word = input()
word_length = len(word)
print(word + " has " + str(word_length) + " letters")
