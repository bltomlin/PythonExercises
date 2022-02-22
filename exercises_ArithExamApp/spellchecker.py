#Write a spellchecker that tells you which words in the sentence are spelled incorrectly. Use the dictionary in the code below.

dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
array = []
for word in sentence:
    if word in dictionary:
        array.append(word)
if len(sentence) == len(array):
    print('OK')
else:
    for phrase in sentence:
        if phrase not in dictionary:
            print(phrase)
