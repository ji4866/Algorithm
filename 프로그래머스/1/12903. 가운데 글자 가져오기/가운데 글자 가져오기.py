def solution(s):
    index_ = len(s)//2
    answer = s[index_]
    
    if len(s) % 2 ==0:
        answer = s[index_-1] + s[index_]
        
        
    
    
    
    return answer