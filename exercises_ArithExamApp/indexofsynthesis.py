#One way to clasify the languages of the world is by looking at their morphological systems. One classification is based on the index of synthesis that reflects the average number of morphemes in a word. The values vary between 1 and 4 and there are 3 types of languages according to that system. Here they aire:

value = float(input())

if value < 2:
    print('Analytic')
elif value >= 2 and value <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')
