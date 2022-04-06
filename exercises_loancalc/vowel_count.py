import string

string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0
for i in string:
    if vowels in i:
        count += 1
print(count)