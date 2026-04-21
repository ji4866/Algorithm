def solution(my_string, m, c):
    idx = 0
    answer = ''

    while idx < len(my_string):
        answer += my_string[idx+c-1]
        idx += m
    
    return answer