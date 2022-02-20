#Find all words that end in "s" and print them together separated by an underscore. 

sentence = input()
array = []
answer = []
array = sentence.split()
for index in array:
    for character in index:
        if index[-1] == 's':
            answer.append(index)
            break
answer = '_'.join(answer)
print(answer)
