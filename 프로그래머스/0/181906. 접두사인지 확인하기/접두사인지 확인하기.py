def solution(my_string, is_prefix):
    answer = []
    for i in range(1, len(my_string)+1):
        answer.append(my_string[:i])
    
    if is_prefix in answer:
        return 1
    else:
        return 0