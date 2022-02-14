#Find out if the result of dividing A by B is an odd number.

a = int(input())
b = int(input())
ans = ((a / b) % 2) == 1
print(ans)
