#Find all words that end in "s" and print them together separated by an underscore. 

print("_".join([element for element in input().split() if element.endswith("s")]))

