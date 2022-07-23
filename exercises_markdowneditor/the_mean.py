some_iterable = input()
total = 0
new_list = [int(x) for x in some_iterable]
for num in new_list:
    total += num
print(total / len(some_iterable))