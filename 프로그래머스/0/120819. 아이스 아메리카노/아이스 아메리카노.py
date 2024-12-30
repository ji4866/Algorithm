def solution(money):
    coffee = 5500
    answer = []
    answer.append(money//coffee)
    answer.append(money%coffee)
    return answer