def solution(a, b, n):
    
    answer, get_ = 0, 0
    
    while n >= a:
        get_ = (n//a)*b
        n = get_ + n%a
        answer += get_
    
    return answer