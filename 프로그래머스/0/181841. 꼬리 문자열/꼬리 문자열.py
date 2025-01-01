def solution(str_list, ex):
    answer = ''
    for _ in str_list:
        if _.find(ex) != -1:
            continue
        answer += _

    return answer