def solution(my_string, index_list):
    answer = ''
    for index_ in index_list:
        answer += my_string[index_]
    return answer