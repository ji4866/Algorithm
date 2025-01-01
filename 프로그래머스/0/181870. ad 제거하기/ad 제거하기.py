def solution(strArr):
    answer = strArr.copy()
    for st in strArr:
        if 'ad' in st:
            answer.remove(st)
    return answer