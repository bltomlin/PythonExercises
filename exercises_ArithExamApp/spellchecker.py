#Write a spellchecker that tells you which words in the sentence are spelled incorrectly. Use the dictionary in the code below.

dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input()
sentence = sentence.split()
for word in sentence:
    if word in dictionary:
        sentence.remove(word)
print(sentence)
