#Locate a point on the Cartesian coordinate plane: which of four quadrants does a point belong to?

x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("It's the origin!")
elif (x == 0 and y != 0) or (x != 0 and y == 0):
    print("One of the coordinates is equal to zero!")
elif x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
else:
    print('IV')