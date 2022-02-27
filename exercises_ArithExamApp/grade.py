#Determine the grade that a student will get based on the student's score and the maximum score.

student_score = float(input())
maximum_score = float(input())
A = 0.9
B = 0.8
C = 0.7
D = 0.6

scoring_grade = round(student_score / maximum_score, 3)

if scoring_grade < D:
    print('F')
elif scoring_grade >= D and scoring_grade < C:
    print('D')
elif scoring_grade >= C and scoring_grade < B:
    print('C')
elif scoring_grade >= B and scoring_grade < A:
    print('B')
else:
    print('A')

