#Write a program that reads an integer value from input and checks if it is less than 10 or greater than 250.

a = int(input().strip())
ans = a < 10 or a > 250
print(ans)
