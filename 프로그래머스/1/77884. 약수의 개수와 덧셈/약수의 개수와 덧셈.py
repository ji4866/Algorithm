def solution(left, right):
    answer = 0
    num_list = [i for i in range(left, right+1)]
    
    for i in num_list:
        count = 0
    
        for j in range(1, i+1):
            if i % j == 0:count += 1
        
        if count % 2 == 0: answer += i
        else : answer -= i
    
    return answer