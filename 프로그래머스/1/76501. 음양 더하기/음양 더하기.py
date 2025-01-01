def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if absolutes[i]*signs[i] != 0: sum += absolutes[i]
        else: sum -= absolutes[i]
    return sum