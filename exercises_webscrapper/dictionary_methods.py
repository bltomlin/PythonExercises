key = int(input())

try:
    del squares[key]      
except KeyError:
    print("There is no such key")
else:
    print(key * key)

print(squares)