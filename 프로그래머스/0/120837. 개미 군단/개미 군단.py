def solution(hp):
    count, answer = 0, 0
    list_ = [5,3,1]
    
    for i in list_:
        count = hp//i
        hp -= i*count
        answer += count
        
    return answer