#Write a simple spellchecker that tells you if the word is spelled correctly. Use the dictionary in the code below: it contains the list of all correctly written words.

dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
word = input()
if word not in dictionary:
    print("Incorrect")
else:
    print("Correct")
