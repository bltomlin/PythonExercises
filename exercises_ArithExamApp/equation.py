#Write a function equation_writing() that will print the equation in the following format: a x + b = c. The function must take three arguments: a, b, c, these values are subject to change. The rest of the equation remains unchanged.

def equation_writing(a, b, c):
    x = 'x'
    plus = '+'
    equal = '='
    string = [a, x, plus, b, equal, c]
    answer = " ".join(string)
    print(answer)
