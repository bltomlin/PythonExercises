#Here is your chance to write instructions for a text-to-speech system. Let's focus on reading phone numbers aloud. The input phone number will consist solely of digits. Print the name of each digit on a new line for the system to read them one by one.


numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for char in input():
    print(numbers[int(char)])
