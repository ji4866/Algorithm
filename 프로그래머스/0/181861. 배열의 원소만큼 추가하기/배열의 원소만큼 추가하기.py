def solution(arr):
    answer = []
    for a in arr:
        answer.extend([ a for i in range(a) ])
    return answer