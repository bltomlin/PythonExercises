#Read a date from the input given in the following format: YYYY-MM-DD. Print the year, month and day on separate lines.

date = input()
year, month, day = date.split('-')
print(year)
print(month)
print(day)

