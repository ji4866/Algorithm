def solution(my_string):
    my_string = my_string.lower()
    answer = [s for s in my_string]
    answer.sort()
    return ''.join(answer)