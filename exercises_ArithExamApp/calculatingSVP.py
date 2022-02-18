#Ask the user about parameters of a rectangular parallelepiped (3 integers representing the length, width, and height) and print the sum of edge lengths, its total surface area, and the volume, one answer per line.

a = int(input())
b = int(input())
c = int(input())

# put your python code here

s = 4 * (a + b + c)
S = 2 * ((a * b) + (a * c) + (b * c))
V = a * b * c

print(s)
print(S)
print(V)
