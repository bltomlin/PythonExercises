#the reference time point is Tuesday, 10:30 in the morning in London (UTC+00:00) output the day of the week in the given time zone.

reference_time_point = 'Tuesday', '10.5'
utc = 0
input_string = input().split()
if input_string[0] == '+':
    input_string = int(input_string[1])
else:
    input_string = ''.join(input_string)
    input_string = int(input_string)
answer = float(reference_time_point[1]) + input_string
if answer > 24:
    print('Wednesday')
elif answer >= 0 and answer < 24:
    print('Tuesday')
else:
    print('Monday')
