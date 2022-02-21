#Draw a triangle of a given height, as in the example.

height = int(input())
hashtag = '#'
double_hash = '##'
space = ' '
count = height - 1
for iteration in range(height):
    print((space * count) + hashtag + (space * count))
    count -= 1
    hashtag += double_hash
