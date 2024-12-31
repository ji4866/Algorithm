def solution(num_list):
    answer = -1
    
    for num in num_list:
        answer += 1
    
        if num<0:
            return answer

    if answer+1 == len(num_list):
        return -1
    
    return answer