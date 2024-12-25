def solution(sides):
    answer = 0
    max_ = max(sides)
    sides.remove(max_)

    if sum(sides) > max_:
        answer = 1
    else:
        answer = 2
    return answer