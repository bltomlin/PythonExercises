#Alex wrote a program that reads a number and a word from the input to create phrases like "3 cats" and "1 dog". Unfortunately, the condition for plural nouns is currently missing. Alex doesn't know how to use if statements, but you do. Help Alex complete this program.

number = int(input())
word = input()

if number != 1:
    word += str("s")

print(number, word)