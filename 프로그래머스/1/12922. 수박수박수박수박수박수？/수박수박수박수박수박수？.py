def solution(n):
    answer = ''
    i = 0
    
    while i < n:
        answer += '수'
        
        i += 1
        
        if i == n:return answer
        else:answer += '박'
        
        i += 1
        
    return answer