#Write the code that reads 2 numbers from the keyboard, a and b. As an output, it shows the mean of all numbers that lie on the interval between a and b, and can be divided by 3.

a = int(input())
b = int(input())
answer = 0
count = 0
for i in range(a, b+1):
    if i % 3 == 0:
        answer += i
        count += 1
answer = answer / count
print(answer)
