#Write a program that calculates the proportion of students who received grade A.

#A five-point rating system with grades A, B, C, D, F is used.

grades = input()
count_a = 0.0
places = 0.0
grades = grades.split()
for index in grades:
    places += 1.0
    for i in index:
        if i == 'A':
            count_a += 1.0
answer = count_a / places
print(round(answer, 2))
