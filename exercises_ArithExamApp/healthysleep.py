#Ann watched a TV program about health and learned that it is recommended to sleep at least A hours per day, but oversleeping is also not healthy, and you should not sleep more than B hours. Now Ann sleeps H hours per day. If Ann's sleep schedule complies with the requirements of that TV program – print "Normal". If Ann sleeps less than A hours, output “Deficiency”, and if she sleeps more than B hours, output “Excess”.

#The input to this program is three strings with variables in the following order: A A A, B B B, H H H. A A A is always less than or equal to B B B.

#Please note the letter cases: the output should exactly correspond to what's required in the problem, i.e., if the program must output "Excess", outputs such as "excess", "EXCESS", or "ExCeSs" will not be graded as correct.

#You should carefully think about all the conditions which you need to use. Special attention should be paid to the strictness of the used conditional operators: remember the difference between < \lt < and ≤ \le ≤; > \gt > and ≥ \ge ≥. In order to understand which ones to use, please carefully read the problem statement.

A = int(input())
B = int(input())
H = int(input())

if H < A:
    print('Deficiency')
elif H >= A and H <= B:
    print('Normal')
else:
    print('Excess')
