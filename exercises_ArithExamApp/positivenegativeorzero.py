#Write a program that reads an integer number and prints:

 #   "negative" if the number is less than 0;
 #   "positive" if the number is greater than 0;
 #   "zero" if the number equals 0.

#Do not output double quotes.

number = int(input())
if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    print('zero')
