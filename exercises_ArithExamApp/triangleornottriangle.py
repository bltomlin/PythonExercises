#Read three angles given on separate input lines and check whether they form a triangle. Print the answer in the following format: "The triangle is valid!" or "The triangle is not valid!".

x = input()
y = input()
z = input()
valid = 180
if int(x) + int(y) + int(z) == valid:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
