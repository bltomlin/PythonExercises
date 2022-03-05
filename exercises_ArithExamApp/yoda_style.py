#Everybody wants to speak like master Yoda sometimes. Let's try to implement a program that will help us with it. 

import random
forty_three = 43
sentence = input().split()
random.seed(forty_three)
random.shuffle(sentence)
print(' '.join(sentence))
