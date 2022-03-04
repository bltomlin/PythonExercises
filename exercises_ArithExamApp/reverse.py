#With a negative step, your start index should be greater than the stop index. Choose the stop index carefully. Due to reverse order, you might want to decrease it by one in order to include the last element in your slice.

numbers = [int(num) for num in input().split()]

print(numbers[16:3:-1])