def solution(a, b):
    days = ['FRI','SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day, day_30 = 0, [4, 6, 9, 11]
    for i in range(1, a):
        if i in day_30 : day += 30
        elif i == 2 : day += 29
        else : day += 31
    day += b
    return days[day%7-1]