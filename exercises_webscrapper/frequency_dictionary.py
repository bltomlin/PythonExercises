"""
When Anton finished reading "War and Peace", he decided to find out the number of specific words used in the book.

Help Anton write a simplified version of such a program, that will be capable of counting the words separated with space, and print the statistics.

The program should ask a user for a sentence and print out each unique word with the number of its usages in the line in the following format (case insensitive!): word amount, e.g. sun 3. The word order does not matter, each word must be printed only once.
"""

sentence = input().split()
dict = {}
holder = ''
count = 0
for word in sentence:
    holder = word.lower()
    for word in sentence:
        if holder == word.lower():
            count += 1
    dict[holder] = count
    count = 0
for key, value in dict.items():
    print(key, value)