def solution(rsp):
    answer = ''
    rsp = list(rsp)
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'

    return answer