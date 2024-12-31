def solution(names):
    answer,i = [], 0

    for name in names:
        if i%5 == 0:
            answer.append(name)
        i += 1
    return answer