def solution(strArr):
    answer, index_ = [], 0
    
    for i in strArr:
        if index_ % 2 == 0:
            answer.append(i.lower())
        else:
            answer.append(i.upper())
        index_ += 1
        
    return answer 
