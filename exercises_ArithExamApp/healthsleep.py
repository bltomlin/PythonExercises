#Ann watched a TV program about health and learned that it is recommended to sleep at least AAA hours per day. Oversleeping is also unhealthy and you should not sleep more than BBB hours. Now, Ann sleeps HHH hours per day.

#Check if Ann's sleep schedule complies with the requirements of that TV program

A, B, H = int(input()), int(input()), int(input())
if H < A:
    print('Deficiency')
elif H > B:
    print('Excess')
else:
    print('Normal')

