#To find out if a word is a palindrome we would need to check if it reads the same forward and backward.

forward = word[:]
backward = word[::-1]

if forward == backward:
    print("Yes")
else:
    print("No")