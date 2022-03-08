#Prevent ZeroDivisionError in the code below. When denominator is 0, print the message "Division by zero is not supported". In other cases, print n divided by denominator.

n = int(input())
denominator = int(input())
try:
   result = n // denominator
except ZeroDivisionError:
    print("Division by zero is not supported")
else:
    print(result)