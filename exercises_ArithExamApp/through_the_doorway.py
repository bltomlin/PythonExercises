#Suppose you want to carry a box with dimensions A × B × C (length × width × height) through the doorway with dimensions X × Y (width × height). Write a program to check whether it is possible.

A = input()
B = input()
C = input()
X = input()
Y = input()

if int(A) <= (int(X) or int(Y)):
    print("The box can be carried") 
elif int(B) <= (int(X) or int(Y)):
    print("The box can be carried") 
elif int(C) <= (int(X) or int(Y)):
    print("The box can be carried") 
else:
    print("The box cannot be carried")