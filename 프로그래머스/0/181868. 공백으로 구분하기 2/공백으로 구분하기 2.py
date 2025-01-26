def solution(my_string):
    string = my_string.split(' ')
    answer = [st for st in string if len(st) != 0]
    return answer