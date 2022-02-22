#Let's try to reverse a numeric sequence. Read it from the input and print its numbers in reverse order separated by spaces.

numbers = input().split()
start_position = 0
end_position = len(numbers) - 1
holder = ''
while start_position < end_position:
    holder = numbers[start_position]
    numbers[start_position] = numbers[end_position]
    numbers[end_position] = holder
    start_position += 1
    end_position -= 1
print(' '.join(numbers))
